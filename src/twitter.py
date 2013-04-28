# This class will interface with twitter
# It Will post new tweets and gather results
# from @reply tweets
# Uses the python-twitter library from github

import sys
import pytwitter.twitter as twitter

class Twitter:
	def __init__(self,c_key,c_secret,a_key,a_secret):
		self.twapi = twitter.Api(consumer_key=c_key, consumer_secret=c_secret, access_token_key=a_key, access_token_secret=a_secret)
		valid = self.twapi.VerifyCredentials()
	
	def post(self,msg):
		status = self.twapi.PostUpdate(msg)
		return status
	'''
		Will tally the responses of anyone in the correct geographic region.
	'''
	def tallyResponses(hashtag):
		return None
			
		
def main():
	t = Twitter('',
		'',
		'',
		'')
	t.post('Test')
	
if __name__ == '__main__':
	main()
