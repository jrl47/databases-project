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
-- Which team had the duo of players with the most combined assists in a season?
WITH SeasonDuos AS (
  -- pairs of players on the same team with their combined assists in a single season
  SELECT p1.player_id AS player1, p2.player_id AS player2, SUM(assists) AS season_assists, team, Game.season_year AS season
  FROM (
      -- pairs of players on the same team with their combined assists in a single game
      SELECT p1.player_id, p2.player_id, p1.assists + p2.assists AS assists, p1.team_id AS team, Game.season_year
      FROM PlayerInGame AS p1, PlayerInGame AS p2, Game
      WHERE p1.team_id = p2.team_id
      AND p1.game_id = p2.game_id
      AND p1.game_id = Game.id
      AND p1.player_id < p1.player_id
  )
  GROUP BY p1.player_id, p2.player_id, team, Game.season_year
)
SELECT team, player1, player2, season_assists, season
FROM SeasonDuos
INNER JOIN (
    -- best duo from any team in any season
    SELECT MAX(season_assists) AS season_assists
    FROM SeasonDuos
) BestDuos
ON SeasonDuos.season_assists = BestDuos.season_assists