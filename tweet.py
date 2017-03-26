import got

def receiveBuffer(tweets):
	for t in tweets:
		print ('\n')
		print ('time: %s' % t.date.strftime("%Y-%m-%d %H:%M"))
		print "Tweet: %s" % t.text
		print "permalink: %s" %t.permalink
	print ('\n')
	print ('More %d printed to screen...\n' % len(tweets))

variable = ""
while variable != 'quit':

	variable = raw_input('Lookup last 10 tweets on something, type something in: ')
	tweetCriteria = got.manager.TweetCriteria().setQuerySearch(variable).setMaxTweets(10)
	got.manager.TweetManager.getTweets(tweetCriteria, receiveBuffer)
	
		


