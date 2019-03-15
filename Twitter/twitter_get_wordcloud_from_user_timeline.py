import sys
import re
import time
import os
import matplotlib.pyplot as plt
from tweepy import Cursor
from twitter_client import get_twitter_client
from wordcloud import WordCloud
from stop_words import get_stop_words
from collections import Counter


def usage():
    print("Usage:")
    print("python {} <username>".format(sys.argv[0]))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
    user = sys.argv[1]
    client = get_twitter_client()

    all_tweets = ""
    languages = Counter()

    for page in Cursor(client.user_timeline, screen_name=user, count=20).pages(1):
        for status in page:
            all_tweets += ''.join(
                re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', status.text, flags=re.MULTILINE))
            languages.update([status.lang])

    most_used_lang = [x[0] for x in languages.most_common(1)][0]

    # Generate a word cloud image
    wordcloud = WordCloud(background_color="white",
                          height=800,
                          width=1600,
                          max_words=100,
                          stopwords=get_stop_words(most_used_lang)) \
        .generate(all_tweets)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")

    if not os.path.exists("imgwordcloud"):
        os.makedirs("imgwordcloud")
    plt.savefig("imgwordcloud/" + user + "_" + str(time.time()) + ".png")
    plt.show()
