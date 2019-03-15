Twitter
=======

###### 1° Prérequis
create an app & get twitter tokens from https://developer.twitter.com/en/apps 

    /!\ activer l'env virtualisé Twitter /!\
    pip install tweepy
###### 2° Autres modules
- 2D plotting [twitter_get_wordcloud_from_user_timeline]  
    
        pip install matplotlib

- wordcloud [twitter_get_wordcloud_from_user_timeline]

        pip install wordcloud
    
    pip install Pillow
    pip install nltk
    python
    >>> import nltk
    >>> nltk.download()
    /!\ add NLTK_DATA varEnv qui cible le répertoire du download /!\
    pip install stop-words


###Remenber

timeline: tweets of the past
streaming : future tweets from now

<=====|========>\
timeline | streaming\
......present