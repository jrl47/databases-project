import goldsberry
import operator

plist = {}
for player in goldsberry.PlayerList(IsOnlyCurrentSeason=0).players():
	if player[u'PERSON_ID'] not in plist:
		plist[player[u'PERSON_ID']] = player[u'DISPLAY_FIRST_LAST']
sorted_plist = sorted(plist.items(), key=operator.itemgetter(1))
for id, name in sorted_plist:
	print str(id) + ": " + name
print len(plist)

#players = goldsberry.PlayerList(IsOnlyCurrentSeason=0)
#playersAllTime=pd.DataFrame(players.players())

'''
for id, name in plist.items():
	plogs = goldsberry.player.gamelogs(id).logs()
	for log in plogs:
		#do something with the data (add to SQL relation)
		print "player id = " + id
		print "points" = + log[u'PTS']
'''
