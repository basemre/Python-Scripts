import tweepy

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#check program is running
user = api.me()
print (user.name)

keywords = ["java", "medium", "javascript", "react", "python"]
numberOfTweets = 25

for tweet in tweepy.Cursor(api.search, keywords).items(numberOfTweets):
    try:
        tweet.favorite()
        print("Favorited.")
    except tweepy.TweepError as e:
        print(e.reason)
    except:
        StopIteration
