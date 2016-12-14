import goldsberry
import pandas


plist = {}
players=goldsberry.PlayerList(IsOnlyCurrentSeason=0).players()
for player in players:
	if player[u'PERSON_ID'] not in plist:
		plist[player[u'PERSON_ID']] = player[u'DISPLAY_FIRST_LAST']
#print plist
#print len(plist)
players=pandas.DataFrame(players)
players=pandas.DataFrame(players,columns=['DISPLAY_FIRST_LAST','FROM_YEAR','TO_YEAR','PERSON_ID','TEAM_CITY','TEAM_ID','TEAM_NAME'])
players.to_csv('playerstest.csv')

teamsa=goldsberry.league.franchise_history().current_teams()
teamsb=goldsberry.league.franchise_history().defunct_teams()
teamsa=pandas.DataFrame(teamsa,columns=['CONF_TITLES','DIV_TITLES','START_YEAR','END_YEAR','GAMES','LEAGUE_TITLES','WINS','LOSSES','PO_APPEARANCES','TEAM_CITY','TEAM_ID','TEAM_NAME','WIN_PCT','YEARS'])
teamsb=pandas.DataFrame(teamsb,columns=['CONF_TITLES','DIV_TITLES','START_YEAR','END_YEAR','GAMES','LEAGUE_TITLES','WINS','LOSSES','PO_APPEARANCES','TEAM_CITY','TEAM_ID','TEAM_NAME','WIN_PCT','YEARS'])
teams=pandas.concat([teamsa,teamsb])
teams.to_csv('teamstest.csv')

year1=2001#1946
year2=2002#1947

games = pandas.DataFrame()

for i in range(0,50):
	start=year1-i
	end=year2-i
	if (end%100<10):
		season=str(start)+'-0'+str(end%100)
	else:
		season=str(start)+'-'+str(end%100)
	print season
	j=1
	for id, name in plist.items():
		plogs = goldsberry.player.game_logs(id,Season=season)
		plogs = pandas.DataFrame(plogs.logs())
		plogs = pandas.DataFrame(plogs,columns=['PTS','AST','BLK','STL','REB','OREB','DREB','TOV','FG3A','FG3M','FG3_PCT','FGA','FGM','FG_PCT','FTA','FTM','FT_PCT','MIN','PF','PLUS_MINUS','GAME_DATE','Game_ID','MATCHUP','Player_ID','WL'])
		games = pandas.concat([games,plogs])
		print j
		j=j+1
	games.to_csv('gamestest.csv')