import got
from textblob import TextBlob

def receiveBuffer(tweets):
	for t in tweets:
		print ('\n')
		print ('time: %s' % t.date.strftime("%Y-%m-%d %H:%M"))
		print "Tweet: %s" % t.text
		analysis = TextBlob(t.text)
		#print(analysis)
		# set sentiment
		if analysis.sentiment.polarity > 0:
			print("positive")
		
		elif analysis.sentiment.polarity == 0:
			#print("neutral" , analysis)
			print ("neutral")
			
		else:
			print ("negative")
		
		print "permalink: %s" %t.permalink
	print ('\n')
	print ('More %d printed to screen...\n' % len(tweets))

variable = ""
while variable != 'quit':

	variable = raw_input('Lookup last 10 tweets on something, type something in: ')
	tweetCriteria = got.manager.TweetCriteria().setQuerySearch(variable).setMaxTweets(10)
	got.manager.TweetManager.getTweets(tweetCriteria, receiveBuffer)
	
		


