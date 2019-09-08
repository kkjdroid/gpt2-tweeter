#!/usr/bin/env python
# -*- coding: utf-8 -*-

import twitter

def tweets(name = 'realdonaldtrump', filename = 'timeline.txt', concatenate = False):
    twitter_api = twitter.api.Api(consumer_key = 'lrIeOgqWbu3gFOOwUKZyunQrq',
                          consumer_secret = 'H0VTYTTnoTjV9igYaUqfOBGKiLCyLtDEdKNml0lPVE4MIp3OTs',
                          access_token_key = '44289486-wLpkICjbjlRs1J40yPTqv6tZX78agqnsVUR2N8S6g',
                          access_token_secret = 'JvGt9ihCF7YWMkyMtggwCwuHQvNwblQdoiF01EyvA09Yc')
    t = get_tweets(twitter_api, name)
    to_file(t, filename, concatenate)

def get_tweets(api=None, screen_name=None):
    timeline = api.GetUserTimeline(screen_name=screen_name, count=200)
    earliest_tweet = min(timeline, key=lambda x: x.id).id
    print("getting tweets before:", earliest_tweet)

    while True:
        tweets = api.GetUserTimeline(
            screen_name=screen_name, max_id=earliest_tweet, count=200
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
    with open(f'examples/{filename}', f'w{concatenate * "+"}') as f:
        for tweet in timeline:
            f.write(tweet.text)
            f.write('\n')
    return(f'examples/{filename}.txt')
