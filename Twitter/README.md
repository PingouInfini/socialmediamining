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
=== Others ===  
    
    pip install Pillow
    pip install nltk
    python
    >>> import nltk
    >>> nltk.download()
    /!\ add NLTK_DATA varEnv qui cible le répertoire du download /!\
    pip install stop-words
    pip install folium
 
 =

### Get tweets
###### from user account *timeline* (ie: @realDOnaldTrump)
| Command line | complement | output |
| --- | --- | --- |
| twitter_custom_CLI.py -u realDOnaldTrump -c 10 -o "json_output_directory" |  --- |jsons in output directory
| twitter_get_user_timeline.py realDonaldTrump |  hard coded: -3200 tweets |user_timeline_realDonaldTrump.jsonl |  

###### from user account *stream* (ie: @realDOnaldTrump)
| Command line | complement | output |
| --- | --- | --- |
| twitter_streaming.py \#RWC2015 \#RWCFinal rugby |  --- |stream___RWC2015___RWCFinal_rugby.jsonl


### WordCloud
| Command line | complement | output |
| --- | --- | --- |
| twitter_get_wordcloud_from_user_timeline.py realDonaldTrump |  hard coded: -3200_tweets -outputDirectotry: imgwordcloud|realDonaldTrump_1552691908.829363.png

### Plot in map + cluster
    twitter_map_plot_user_timeline.py <username>
###### example
    twitter_map_plot_user_timeline.py bobjouy

###Remember

timeline: tweets of the past\
streaming : future tweets from now

<=====|========>\
timeline | streaming\
......present