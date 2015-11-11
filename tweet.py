#!/usr/local/bin/python2.7

from twython import Twython
from config import consumer_key, consumer_secret, access_token, access_token_secret
from index import new_tweet
import logging

twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

with open('./past_tweets.log', 'r') as f:
    reader = f.readlines()
    scraped_tweets = new_tweet()
    past_tweets = []

    for row in reader:
        past_tweets.append(row)

    for row in scraped_tweets:
        for report_tweet in row:
            duplicate = [s for s in past_tweets if report_tweet in s]

            if duplicate:
                print "Already been tweeted."
            else:
                logging.basicConfig(filename='past_tweets.log', level=logging.INFO)
                logging.info(report_tweet)
                # twitter.update_status(status=report_tweet)
                print report_tweet
                print "New tweet tweeted."
