import tweepy
import json
from pprint import pprint
from time import sleep
from pyshorteners import Shortener
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

shortener = Shortener('Isgd')

with open('punten.json') as data_file:
    data = json.load(data_file)

count_read = open("count.txt", "r")
count = int(count_read.read())
count_read.close()

def update_status():
    if count <= len(data):
        item = data[count]
        text = item["tekst"][:118]
        base_long_url = 'https://programma.gl/'
        slug = item["slug"]
        long_url = base_long_url + slug
        short_url = shortener.short(long_url)
        tweet = text + '…—' + short_url
        try:
            api.update_status(tweet)
            new_count = count + 1
            count_write = open("count.txt", "w")
            count_write.truncate()
            count_write.write(str(new_count))
            count_write.close()
        except tweepy.TweepError as e:
            print(e.reason)

update_status()
