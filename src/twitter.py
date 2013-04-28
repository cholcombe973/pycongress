# This class will interface with twitter
# It Will post new tweets and gather results
# from @reply tweets
# Uses the python-twitter library from github

import ConfigParser
import sys
import pytwitter.twitter as twitter

class Twitter:
	def __init__(self, c_key, c_secret, a_key, a_secret):
		self.twapi = twitter.Api(consumer_key=c_key, consumer_secret=c_secret, access_token_key=a_key, access_token_secret=a_secret)
		valid = self.twapi.VerifyCredentials()
	
	def post(self, msg):
		status = self.twapi.PostUpdate(msg)
		return status
	'''
		Will tally the responses of anyone in the correct geographic region.
		Searches for all tweets up until when the time when the bill goes up 
		for a vote.  Searches by hashtag of twitterid+hashtag

		Returns (hashtag, number for, number against)
	'''
	def tallyResponses(self, hashtag):
		#This can return paged results. Rewrite this loop
		approve = 0
		oppose = 0 
		stats = self.twapi.GetSearch('pycongress'+hashtag, include_entities=True)
		for s in stats:
			if 'yay' or 'approve' in s.text:
				approve = approve + 1
			if 'nay' or 'deny' in s.text:
				oppose = oppose + 1
		return (hashtag, approve, oppose)
			
		
def main():
	config = ConfigParser.RawConfigParser()
	config.readfp(open('props.txt'))
	config.get("mysqld", "user")
	t = Twitter(config.get("twitter","consumer_key"),
		config.get("twitter","consumer_secret"),
		config.get("twitter","access_token"),
		config.get("twitter","access_secret")
	t.post('Test')
	
if __name__ == '__main__':
	main()
