from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import time

consumer_key="a7vdFgIeOzMtv5SEf5Nw7euEy"
consumer_secret="FUeuYbCK3oatQ2zcUP4st7JvUZeVRCvFtChe9i4YOZgZPFS7k8"

access_token="2547796078-NukRjzi5dVONtf0H44KXoVwvVWINQ1q2PLCBsea"
access_token_secret="XIwJdgZsKZ5Dq8NlYsq4h7lrRmjyJJr9rCnC2uQTshGeS"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print data
        print type(data)
        f = open('a_status.json','wb')
        print >> f, data
        f.close()
        raise Exception('error')
        #time.sleep(1)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)

    stream.sample()
