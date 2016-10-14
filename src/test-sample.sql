-- Who had a quadruple-double in 2015
SELECT Player.first_name, Player.last_name FROM Player, PlayerInGame, Game 
WHERE Player.id=PlayerInGame.player_id AND Game.id=PlayerInGame.game_id
AND Game.season_year='2015' 
AND ((PlayerInGame.points>9 AND PlayerInGame.assists>9 AND PlayerInGame.rebounds>9 AND PlayerInGame.blocks>9)
	OR (PlayerInGame.points>9 AND PlayerInGame.assists>9 AND PlayerInGame.rebounds>9 AND PlayerInGame.steals>9)
	OR (PlayerInGame.points>9 AND PlayerInGame.assists>9 AND PlayerInGame.steals>9 AND PlayerInGame.blocks>9)
	OR (PlayerInGame.points>9 AND PlayerInGame.steals>9 AND PlayerInGame.rebounds>9 AND PlayerInGame.blocks>9)
	OR (PlayerInGame.steals>9 AND PlayerInGame.assists>9 AND PlayerInGame.rebounds>9 AND PlayerInGame.blocks>9));
-- Who won 2015 scoring title
WITH PointsInSeason(first,last,points) AS 
(SELECT Player.first_name, Player.last_name, 
	(SELECT SUM(points) FROM PlayerInGame, Game WHERE player_id=Player.id AND game_id=Game.id AND Game.season_year='2015')
FROM Player)
SELECT * FROM PointsInSeason
WHERE points=(SELECT MAX(points) FROM PointsInSeason); 
-- Who had the most double-doubles and how many
SELECT * FROM
(SELECT player_id,
SUM(CASE WHEN temp.doubleCount >= 2 THEN 1 ELSE 0 END) AS doubleDoubles
FROM
(SELECT *,
(CASE WHEN points >= 10 THEN 1 ELSE 0 END) +
(CASE WHEN assists >= 10 THEN 1 ELSE 0 END) +
(CASE WHEN rebounds >= 10 THEN 1 ELSE 0 END) +
(CASE WHEN blocks >= 10 THEN 1 ELSE 0 END) +
(CASE WHEN steals >= 10 THEN 1 ELSE 0 END) AS doubleCount
FROM PlayerInGame) temp
GROUP BY player_id) AS playerDoubleDoubles
WHERE doubleDoubles >= ALL(SELECT doubleDoubles FROM playerDoubleDoubles);
-- Which players have more letters in their last name than highest career points scored in a game
SELECT first_name, last_name, points FROM Player, (SELECT player_id, MAX(points) FROM PlayerInGame GROUP BY player_id) WHERE player_id = id AND LEN(last_name) > points;
-- Which players have scored the most points in San Antonion in their career and how many
SELECT * FROM
(SELECT player_id,
SUM(temp.points) AS san_antonion_points
FROM
(SELECT *
FROM PlayerInGame, Game
WHERE PlayerInGame.game_id = Game.id AND game.location = 'San Antonion') temp
GROUP BY player_id) AS playerSanAntonionPoints
WHERE san_antonion_points >= ALL(SELECT san_antonion_points FROM playerSanAntonionPoints);
-- Which players have the most rebounds in January and how many
SELECT * FROM
(SELECT player_id,
SUM(temp.points) AS january_points
FROM
(SELECT *
FROM PlayerInGame, Game
WHERE PlayerInGame.game_id = Game.id AND CHARINDEX(game.date, 'January') > 0) temp
GROUP BY player_id) AS playerJanuaryPoints
WHERE january_points >= ALL(SELECT january_points FROM playerJanuaryPoints);