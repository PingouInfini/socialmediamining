import sys
import re
import time;
from tweepy import Cursor
from twitter_client import get_twitter_client
from wordcloud import WordCloud
from stop_words import get_stop_words

def usage():
    print("Usage:")
    print("python {} <username>".format(sys.argv[0]))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
    user = sys.argv[1]
    client = get_twitter_client()

    all_tweets=""

    for page in Cursor(client.user_timeline, screen_name=user, count=20).pages(16):
        for status in page:
            all_tweets += ''.join(re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', status.text, flags=re.MULTILINE))
            lang = status.lang

    # Generate a word cloud image
    wordcloud = WordCloud(background_color="white",
                          height=800,
                          width=1600,
                          max_words=100,
                          stopwords= get_stop_words(lang))\
                .generate(all_tweets)

    import matplotlib.pyplot as plt
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(user+"_"+time.time()+".png")
    plt.show()