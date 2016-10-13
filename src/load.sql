\COPY Player(id,first_name,last_name) FROM 'data/Player.dat' WITH DELIMITER ',' NULL '' CSV
\COPY Team(id,name) FROM 'data/Team.dat' WITH DELIMITER ',' NULL '' CSV
\COPY Season(year,champion) FROM 'data/Season.dat' WITH DELIMITER ',' NULL '' CSV
\COPY Game(id,season_year,location,home_team,away_team,date) FROM 'data/Game.dat' WITH DELIMITER ',' NULL '' CSV
\COPY PlayerInGame(player_id,game_id,team_id,is_home,points,assists,rebounds,blocks,steals) FROM 'data/PlayerInGame.dat' WITH DELIMITER ',' NULL '' CSV
\COPY TeamInSeason(team_id,season_year,wins,losses) FROM 'data/TeamInSeason.dat' WITH DELIMITER ',' NULL '' CSV

-- THE THIRD INSERT SHOULD FAIL DUE TO TWO TEAMS IN GAME TRIGGER
--INSERT INTO Player VALUES(10,'new','player');
--INSERT INTO Team VALUES(3,'NEW');
--INSERT INTO PlayerInGame VALUES(10,1,3,FALSE,5,5,5,5,5);