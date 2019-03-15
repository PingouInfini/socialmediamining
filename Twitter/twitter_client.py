import os
import sys
from tweepy import API
from tweepy import OAuthHandler


def get_twitter_auth():
    """Setup Twitter authentication.

    Return: tweepy.OAuthHandler object
    """
    f = open("twitterCredentials.txt", "r")
    lines = f.readlines()
    consumer_key = str(lines[1]).replace("\n", "")
    consumer_secret = str(lines[2]).replace("\n", "")
    access_token = str(lines[3]).replace("\n", "")
    access_secret = str(lines[4]).replace("\n", "")
    f.close()

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth


def get_twitter_client():
    """Setup Twitter API client.

    Return: tweepy.API object
    """
    auth = get_twitter_auth()
    client = API(auth)
    return client
