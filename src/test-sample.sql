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
WITH playerDoubleDoubles AS (
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
  GROUP BY player_id)
)
SELECT *
FROM playerDoubleDoubles
WHERE doubleDoubles >= ALL(SELECT doubleDoubles FROM playerDoubleDoubles);

-- Which players have more letters in their last name than highest career points scored in a game
SELECT first_name, last_name, points
FROM Player, (SELECT player_id, MAX(points) AS points FROM PlayerInGame GROUP BY player_id) as r
WHERE player_id = id AND LENGTH(last_name) > points;

-- Which players have scored the most points in San Antonion in their career and how many
WITH playerSanAntonionPoints AS (
  SELECT player_id,
  SUM(temp.points) AS san_antonion_points
  FROM
  (SELECT *
   FROM PlayerInGame, Game
   WHERE PlayerInGame.game_id = Game.id AND game.location = 'San Antonio') temp
  GROUP BY player_id
)
SELECT *
FROM playerSanAntonionPoints
WHERE san_antonion_points >= ALL(SELECT san_antonion_points FROM playerSanAntonionPoints);

-- Which players have the most rebounds in January and how many
SELECT * FROM
(SELECT player_id,
SUM(temp.points) AS january_points
FROM
(SELECT *
FROM PlayerInGame, Game
WHERE PlayerInGame.game_id = Game.id AND strpos(game.date, 'January') > 0) temp
GROUP BY player_id) AS playerJanuaryPoints
WHERE january_points >= ALL(SELECT january_points FROM playerJanuaryPoints);

-- Which team had the duo of players with the most combined assists in a season?
WITH SeasonDuos AS (
  -- pairs of players on the same team with their combined assists in a single season
  SELECT player1, player2, SUM(assists) AS season_assists, team, season
  FROM (
      -- pairs of players on the same team with their combined assists in a single game
      SELECT p1.player_id AS player1, p2.player_id AS player2, p1.assists + p2.assists AS assists, p1.team_id AS team, Game.season_year as season
      FROM PlayerInGame AS p1, PlayerInGame AS p2, Game
      WHERE p1.team_id = p2.team_id
      AND p1.game_id = p2.game_id
      AND p1.game_id = Game.id
      AND p1.player_id < p2.player_id
  ) AS GameDuos
  GROUP BY player1, player2, team, season
)
SELECT DISTINCT Team.name
FROM SeasonDuos
INNER JOIN (
    -- best duo from any team in any season
    SELECT MAX(season_assists) AS max_assists
    FROM SeasonDuos
) BestDuos
ON SeasonDuos.season_assists = BestDuos.max_assists
INNER JOIN Team
ON SeasonDuos.team = Team.id;

-- Which players played on the championship team this season?
SELECT first_name, last_name
FROM Player
INNER JOIN (
    SELECT DISTINCT player_id
    FROM PlayerInGame AS p
    INNER JOIN Team
    ON p.team_id = Team.id
    INNER JOIN (
        SELECT champion
        FROM Season
        INNER JOIN (
            SELECT MAX(year) AS year
            FROM Season
        ) CurrentSeason
        ON Season.year = CurrentSeason.year
    ) c
    ON name = c.champion
) ids
ON Player.id = ids.player_id;
