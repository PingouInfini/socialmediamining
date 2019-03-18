Twitter
=======

###### 1° Prérequis
create an app & get twitter tokens from https://developer.twitter.com/en/apps 

    /!\ activer l'env virtualisé Twitter /!\
    pip install tweepy
###### 2° Autres modules
- 2D plotting  
        
      pip install matplotlib

- wordcloud 

      pip install wordcloud
        
- nltk

      pip install nltk
      python
      >>> import nltk
      >>> nltk.download()
      /!\ add NLTK_DATA varEnv qui cible le répertoire du download /!\

- Others  

      pip install stop-words
      pip install folium
      pip install geopy

 
 =

### Get tweets

- from user account *timeline* (ie: @realDOnaldTrump)   
    ###### twitter_custom_CLI
      twitter_custom_CLI.py -u realDOnaldTrump -c 10 -o "json_output_directory"
    ###### twitter_get_user_timeline (hard coded: -3200 tweets) > *"user_timeline_realDonaldTrump.jsonl"*    
      twitter_get_user_timeline.py realDonaldTrump 

- from user account *stream* (ie: @realDOnaldTrump)  
    ###### twitter_streaming > *"stream___RWC2015___RWCFinal_rugby.jsonl"*  
      twitter_streaming.py \#RWC2015 \#RWCFinal rugby


### WordCloud
###### twitter_get_wordcloud_from_user_timeline > hard coded: -3200_tweets // -outputDirectotry: imgwordcloud > *realDonaldTrump_1552691908.829363.png*
    twitter_get_wordcloud_from_user_timeline.py realDonaldTrump

### Plot in map + cluster
    twitter_map_plot_user_timeline.py <username> <filename.html>
###### example
    twitter_map_plot_user_timeline.py bobjouy mymap.html

###Remember

timeline: tweets of the past\
streaming : future tweets from now

<=====|========>\
timeline | streaming\
......present