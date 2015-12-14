
import tweepy 
import json

consumer_key="Consumer Key from Twitter"
consumer_key_secret="Secret from Twitter"
access_token = "Access Token"
access_token_secret = "Access Token Secret"
twts = open("tweets","w")


class StdOutListener(tweepy.StreamListener):
    counter=0
    def on_data(self, data):
	twts.write(data)
	self.counter+=1
	if(self.counter%500)==0:
		self.counter=0
		twts.seek(0)
		twts.truncate()
        return True
    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = tweepy.Stream(auth, l)
    stream.filter(track=['MockingjayPart2'])
