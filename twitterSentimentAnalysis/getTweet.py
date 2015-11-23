
import tweepy 
import json

consumer_key="Q5v9xOBKEQsAAYyWt6Hg"
consumer_key_secret="Y8op2C2ZNOHbtuNtFU2vpDMRJ9S7dlviKPNdbpC4"
access_token = "100223246-25Be2q6xqc50fbMENhUdLNaOlWWimQc8CA6ue8sD"
access_token_secret = "cXDE5ZxwxQaH9DcIfBpuiKT8NG84krZyhVaPeBtCexG0p"
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
