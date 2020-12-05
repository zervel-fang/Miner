clear
clc
data = load('IDs_only_tweets_ID_user_tweet_datetime_2018_WalkAway_2018-07-05.tsv') ;
data1 = load('IDs_only_tweets_ID_user_tweet_datetime_2018_WalkAway_2018-07-06.tsv') ;
data2 = load('IDs_only_tweets_ID_user_tweet_datetime_2018_WalkAway_2018-07-07.tsv') ;
data3 = load('IDs_only_tweets_ID_user_tweet_datetime_2018_WalkAway_2018-07-08.tsv') ;
data4 = load('IDs_only_tweets_ID_user_tweet_datetime_2018_WalkAway_2018-07-09.tsv') ;
data5 = load('IDs_only_tweets_ID_user_tweet_datetime_2018_WalkAway_2018-07-10.tsv') ;
data6 = load('IDs_only_tweets_ID_user_tweet_datetime_2018_WalkAway_2018-07-11.tsv') ;
len = length(data) + length(data1)+length(data2)+length(data3)+length(data4)+length(data5)+length(data6)