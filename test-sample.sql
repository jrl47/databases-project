-- Who had a Double-double in 2015
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
