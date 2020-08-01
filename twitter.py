import tweepy
import time

auth = tweepy.OAuthHandler('API KEY GOES HERE', 'API KEY SECRET GOES HERE ')

auth.set_access_token('ACCESS TOKEN GOES HERE', 'ACCESS TOKEN SECRET GOES HERE')

api = tweepy.API(auth, wait_on_rate_limit=  True, wait_on_rate_limit_notify=True)

user = api.me()

search1 = 'Twitch Streamer OR Streaming on Twitch OR Live on Twitch'


for tweet in tweepy.Cursor(api.search, search1).items(500):
    try:
        print('Tweet Liked')
        print('Tweet Retweeted')
        tweet.retweet()
        tweet.favorite()
        time.sleep(1500)
    except tweepy.TweepError as error:
        print(error.reason)
    except StopIteration:
        break

