#Milestone 1
##Brief description
Overall description: sports stats application that allows users to query a sports (eg basketball) database. Example use cases: 1. Input a stat line, return players from previous games with same/similar stats. 2. Input a formula based on stats, return table of players sorted by value associated with the formula

##Plan for getting data
We will get our data directly from the National Basketball Association via the APIs on its webiste, stats.nba.com. We plan to leverage an existing Python module, py-Goldsberry, to scrape data from the site into a form that we can enter into our database.

##List of assumptions
The number & team of a player cannot change midgame.
Games only belong to one season.
Each game is played by only 2 teams.
Team names do not change.
Each season has exactly one champion.
##E/R Diagram
![alt text](https://lh4.googleusercontent.com/JZkypcmfl9Tz7eaulNReaPZv-xKcPvPcg_JlXqPU-VaIVbtHB55zq9HbhyiI9crStz6bPTkwLmyCIp4=w1920-h811-rw "E/R Diagram")
##List of Database tables
Player(id, first_name, last_name) key:id
Team(id, name) key:id
Season(year, champion) key:year
Game(id, season_year, location, home_team, away_team, date) key:id
PlayerInGame(player_id, game_id, team_id, is_home, points, assists, rebounds, blocks, steals) key:player_id, game_id
TeamInSeason(team_id, season_year, wins, losses) key:team_id, season_year
##Description of web interface
