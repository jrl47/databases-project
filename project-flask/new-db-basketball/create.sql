CREATE TABLE Team(id INT,
		conf_titles INT,
		div_titles INT,
		start_year INT,
		end_year INT,
		games INT,
		league_titles INT,
		wins INT,
		losses INT,
		po_appearances INT,
		team_city VARCHAR(25),
		team_id VARCHAR(15) NOT NULL PRIMARY KEY,
		team_name VARCHAR(15),
		win_pct FLOAT,
		years INT);

CREATE TABLE Player(id INT,
		first_last VARCHAR(30) NOT NULL,
		from_year INT,
		to_year INT,
		player_id VARCHAR(10) NOT NULL PRIMARY KEY,
		team_city VARCHAR(25),
		team_id VARCHAR(15) REFERENCES Team(team_id),
		team_name VARCHAR(15));

CREATE TABLE Game(id INT,
		pts FLOAT,
		ast FLOAT,
		blk FLOAT,
		stl FLOAT,
		reb FLOAT,
		oreb FLOAT,
		dreb FLOAT,
		tov FLOAT,
		fg3a FLOAT,
		fg3m FLOAT,
		fg3_pct FLOAT,
		fga FLOAT,
		fgm FLOAT,
		fg_pct FLOAT,
		fta FLOAT,
		ftm FLOAT,
		ft_pct FLOAT,
		min FLOAT,
		pf FLOAT,
		plus_minus FLOAT,
		game_date VARCHAR(20),
		game_id VARCHAR(20) NOT NULL,
		matchup VARCHAR(20),
		player_id VARCHAR(20) NOT NULL REFERENCES Player(player_id),
		wl CHAR(1),
		PRIMARY KEY(player_id,game_id));
