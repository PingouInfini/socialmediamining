#!/usr/bin/env python
# encoding: utf-8

import tweepy  # https://github.com/tweepy/tweepy
import io, json
import sys, getopt
import logging
import os


# refere to http://docs.tweepy.org/en/v3.5.0/api.html for new implementation

def get_all_tweets(argv):
    # INIT PARAMS
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    count = 9999999999
    data = ""
    getimage = False
    nb_TW_already_get = 0
    jsonoutput = "json/"
    mediaoutput = " media/"
    twitter_user_name = ""
    alltweets = []

    # read_options from command line

    try:
        opts, args = getopt.getopt(argv, "hviu:d:c:o:m:",
                                   ["verbose", "image", "user=", "data=", "count=", "output", "media"])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print_help()
            sys.exit()
        elif opt in ("-v", "--verbose"):
            logging.getLogger().setLevel(logging.DEBUG)
        elif opt in ("-i", "--image"):
            getimage = True
        elif opt in ("-u", "--twitter_user_name"):
            logging.debug("twitter_user_name: " + twitter_user_name)
            twitter_user_name = arg
        elif opt in ("-d", "--data"):
            data = arg
            logging.debug("data: " + data)
        elif opt in ("-c", "--count"):
            count = arg
            logging.debug("count: " + str(count))
        elif opt in ("-o", "--output"):
            jsonoutput = arg
            logging.debug("output: " + jsonoutput)
        elif opt in ("-m", "--media"):
            mediaoutput = arg
            logging.debug("media: " + mediaoutput)

    # get_credentials_from_file (used for twitter connection)
    consumer_key, consumer_secret, access_key, access_secret = get_credentials_from_file()

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweets
    alltweets = []
    nb_TW_to_get = min(int(count), 100)

    if twitter_user_name != "":
        new_tweets = api.user_timeline(screen_name=twitter_user_name, count=nb_TW_to_get, tweet_mode="extended")
    if data != "":
        new_tweets = api.search(q=data, count=nb_TW_to_get, tweet_mode="extended")

    # save most recent tweets
    alltweets.extend(new_tweets)
    nb_TW_already_get += nb_TW_to_get
    # save tweets as json files
    save_tweets_as_json(new_tweets, jsonoutput)
    # save media if asked
    if (getimage):
        save_media(new_tweets, mediaoutput)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while (int(count) - nb_TW_already_get > 0):
        logging.debug("getting tweets before %s" % (oldest))

        nb_TW_to_get = min((int(count) - nb_TW_already_get), 100)

        # all subsiquent requests use the max_id param to prevent duplicates
        if twitter_user_name != "":
            new_tweets = api.user_timeline(screen_name=twitter_user_name, count=nb_TW_to_get, max_id=oldest,
                                           tweet_mode="extended")

        if data != "":
            new_tweets = api.search(q=data, count=nb_TW_to_get, max_id=oldest, tweet_mode="extended")

        # save most recent tweets
        alltweets.extend(new_tweets)
        nb_TW_already_get += nb_TW_to_get

        # save tweets as json files
        save_tweets_as_json(new_tweets, output)
        # save media if asked
        if (getimage):
            save_media(new_tweets, mediaoutput)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        logging.debug("...%s tweets downloaded so far" % (len(alltweets)))

    # transform the tweepy tweets into a 2D array that will populate the csv
    # outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

    pass


def print_help():
    print ('NAME')
    print('\ttwitter_custom_CLI.py - get tweet from twitter account or specific data')
    print ('\nSYNOPSIS')
    print('\ttwitter_custom_CLI.py -u <twitter_user_name> [OPTION]...')
    print('\ttwitter_custom_CLI.py -d <data> [OPTION]...')
    print ('\nDESCRIPTION')
    print ('\t-c, --count')
    print ('\t\tmaximum number of tweet to get')
    print ('\t-d, --data')
    print ('\t\tspecific data to find in json tweet (data or metadata)')
    print ('\t-h, --help')
    print ('\t\tshow help')
    print ('\t-o, --output')
    print ('\t\toutput directory to store json of tweet (default=\'json/\')')
    print ('\t-u, --user')
    print ('\t\tget a tweet from a specific account (without \'@\')')
    print ('\t-v, --verbose')
    print ('\t\tshow log in DEBUG')


def get_credentials_from_file():
    f = open("twitterCredentials.txt", "r")
    lines = f.readlines()
    consumer_key = str(lines[1]).replace("\n", "")
    consumer_secret = str(lines[2]).replace("\n", "")
    access_key = str(lines[3]).replace("\n", "")
    access_secret = str(lines[4]).replace("\n", "")
    f.close()
    return consumer_key, consumer_secret, access_key, access_secret


def save_tweets_as_json(tweetslist, output):
    if not os.path.exists(output):
        os.makedirs(output)

    for eachtweet in tweetslist:
        with io.open(output + '/' + eachtweet.id_str + '.json', 'w', encoding='utf-8') as jfile:
            jfile.write(json.dumps(eachtweet._json, ensure_ascii=False))


def save_media(tweetslist, output):
    if not os.path.exists(output):
        os.makedirs(output)


if __name__ == '__main__':
    get_all_tweets(sys.argv[1:])
