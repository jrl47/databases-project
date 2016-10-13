CREATE TABLE Player(id INT NOT NULL PRIMARY KEY,
		first_name VARCHAR(30) NOT NULL,
		last_name VARCHAR(30) NOT NULL);

CREATE TABLE Game(id INT NOT NULL PRIMARY KEY,
		season_year VARCHAR(20) NOT NULL REFERENCES Season(year),
		location VARCHAR(30) NOT NULL,
		home_team VARCHAR(30) NOT NULL REFERENCES Team(name),
		away team VARCHAR(30) NOT NULL REFERENCES Team(name),
		date VARCHAR(30) NOT NULL);

CREATE TABLE Team(id INT NOT NULL PRIMARY KEY,
		name VARCHAR(30) NOT NULL);

CREATE TABLE Season(year VARCHAR(20) NOT NULL PRIMARY KEY);

CREATE TABLE PlayerInGame(player_id INT NOT NULL REFERENCES Player(id),
		game_id INT NOT NULL REFERENCES Game(id),
		team_id INT NOT NULL REFERENCES Team(id),
		is_home BOOLEAN NOT NULL,
		points INT NOT NULL,
		assists INT NOT NULL,
		rebounds INT NOT NULL,
		blocks INT NOT NULL,
		steals INT NOT NULL,
		PRIMARY KEY(player_id, game_id));

CREATE TABLE TeamInSeason(team_id  INT NOT NULL REFERENCES Team(id),
		season_year VARCHAR(20) NOT NULL REFERENCES Season(year),
		is_champion BOOLEAN NOT NULL,
		wins INT NOT NULL,
		losses INT NOT NULL,
		PRIMARY KEY(team_id, season_year));

CREATE TABLE PlayerInSeason(player_id INT NOT NULL REFERENCES Player(id),
		season_year VARCHAR(20) NOT NULL REFERENCES Season(year),
		points INT NOT NULL,
		assists INT NOT NULL,
		rebounds INT NOT NULL,
		blocks INT NOT NULL,
		steals INT NOT NULL,
		PRIMARY KEY(player_id, season_year));
