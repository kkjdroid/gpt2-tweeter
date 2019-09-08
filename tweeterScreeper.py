import twitter
import random

def tweets(name = 'realdonaldtrump', filename = 'timeline.txt', concatenate = False):
    twitter_api = twitter.api.Api(consumer_key = 'lrIeOgqWbu3gFOOwUKZyunQrq',
                          consumer_secret = 'H0VTYTTnoTjV9igYaUqfOBGKiLCyLtDEdKNml0lPVE4MIp3OTs',
                          access_token_key = '44289486-wLpkICjbjlRs1J40yPTqv6tZX78agqnsVUR2N8S6g',
                          access_token_secret = 'JvGt9ihCF7YWMkyMtggwCwuHQvNwblQdoiF01EyvA09Yc',
                          tweet_mode = 'extended')
    t = get_tweets(twitter_api, name)
    to_file(t, filename, concatenate)

def tweet(message):
	twitter_api = twitter.api.Api(consumer_key = 'lrIeOgqWbu3gFOOwUKZyunQrq',
                          consumer_secret = 'H0VTYTTnoTjV9igYaUqfOBGKiLCyLtDEdKNml0lPVE4MIp3OTs',
                          access_token_key = '44289486-wLpkICjbjlRs1J40yPTqv6tZX78agqnsVUR2N8S6g',
                          access_token_secret = 'JvGt9ihCF7YWMkyMtggwCwuHQvNwblQdoiF01EyvA09Yc')
	twitter_api.PostUpdate(message)

def get_tweets(api=None, screen_name=None):
    timeline = api.GetUserTimeline(screen_name=screen_name, count=200, include_rts = False, exclude_replies = True)
    earliest_tweet = min(timeline, key=lambda x: x.id).id
    print("getting tweets before:", earliest_tweet)

    while True:
        tweets = api.GetUserTimeline(
            screen_name=screen_name, max_id=earliest_tweet, count=200, include_rts = False, exclude_replies = True
        )
        new_earliest = min(tweets, key=lambda x: x.id).id

        if not tweets or new_earliest == earliest_tweet:
            break
        else:
            earliest_tweet = new_earliest
            print("getting tweets before:", earliest_tweet)
            timeline += tweets

    return timeline

def to_file(timeline, filename = 'timeline.txt', concatenate = False):
    with open(f'examples/{filename}', f'{"a+" if concatenate else "w+"}') as f:
        for tweet in timeline:
            text = deEmojify(tweet.full_text)
            f.write(text)
            f.write('\n\n')
    return(f'examples/{filename}.txt')

def deEmojify(inputString):
    if(inputString is None):
        inputString = ''
    return inputString.encode('ascii', 'ignore').decode('ascii')

def parseTweets(file_path):
	twits=[]
	with open(f'{file_path}', 'r') as f:
		for a in f:
			if(a != '\n' and len(a) < 300):
				if(a.find('http') != -1):
					twits.append(a[:a.find('http')])
				else:
					twits.append(a)
	return twits

def rand_tweet(file_path):
	tweeters = parseTweets(file_path)
	try:
		tweet(tweeters[random.randrange(len(tweeters))])
	except:
		tweet(tweeters[random.randrange(len(tweeters))])
