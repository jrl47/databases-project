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
![ERD](ERD.png)

##List of Database tables
*Player(id, first_name, last_name)* key:*id*

*Team(id, name)* key:*id*

*Season(year, champion)* key:*year*

*Game(id, season_year, location, home_team, away_team, date)* key:*id*

*PlayerInGame(player_id, game_id, team_id, is_home, points, assists, rebounds, blocks, steals)* key:*player_id, game_id*

*TeamInSeason(team_id, season_year, wins, losses)* key:*team_id, season_year*

##Description of web interface
The web interface will allow users to graphically build a broad class of queries regarding players, teams, games, and seasons. The user will be given a drop down menu to choose whether they would like information primarily associated with players, teams, games, or seasons, and will then offer a selection of queries for the user to ask. If the player wishes to make a query about a specific player, team, game, or season, they may either select the object of interest from a table it is being displayed in to specify it as the subject of the next query (by way of auto-filling an id box), or look up the object of interest in a "find a specific entity" search bar. If an id is specified, then the drop-down boxes listing possible queries will populate themseves with different questions (more suited queries to make about individuals) to reflect this.