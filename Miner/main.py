# Use shebang here

import pandas as pd
import tweepy
import csv
import requests
from urllib.request import getproxies
import emoji
import re
# x=getproxies()
# print(x)
# consumer_key = 'dInH5F3UO5PDTmzRI6cQVSznb'
# consumer_secret = 'gtGxgajVb9VaNLSAnyOJBpfH25owKXjqLsA1BJYIhDKN2xoiQC'
# access_token = '1274599686733586432-9cYhfa8gOj5IiRYBtMpmHDQs3kRDh7'
# access_secret = 'Px96vFMq608Bdhm6BzfgtDokxDonuQeu9mUMmwXh4f6rR'
# def retrieve_tweets(input_file,outputfile):
#     """
#     Takes an input filename/path of tweetIDs and outputs the full tweet data to a csv
#     """
#
#     # Authorization with Twitter
#
#     auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#     auth.set_access_token(access_token, access_secret)
#     api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=10, retry_delay=5,
#                      retry_errors=set([401, 404, 500, 503]),proxy=x['https'])
#
#     df = pd.read_csv(input_file)
#
#     # Create output file
#     i  = 0
#     sumv = 0
#     tweet_id_list = []
#     fid = open(outputfile,'w',encoding='utf-8')
#     for j in df.iloc[:, 0]:
#         #print(j)
#         tweet_id_list.append(j)
#         i = i + 1
#         if i==100:
#             #print(tweet_id_list)
#             sumv = sumv + i
#             print(sumv)
#             tag=1
#             while tag==1:
#                 try:
#                     tweets = api.statuses_lookup(tweet_id_list)
#                     tw_list =list(tweets)
#                     for ii in tw_list:
#                         text = re.sub('(\:.*?\:)', '', emoji.demojize(ii.text))
#                         text = text.replace("\n"," ")
#                         text1 = re.sub('(\:.*?\:)', '', emoji.demojize(ii.user.name))
#                         fid.write(text1+' '+str(ii.user.id)+' '+str(ii.created_at)+' '+text+'\n')
#                     i = 0
#                     tag = 0
#                 except Exception as e:
#                     print(e)
#             del tweet_id_list
#             tweet_id_list = []
#
#     ## deal with the remaining parts
#     tag = 1
#     while tag == 1:
#         try:
#             tweets = api.statuses_lookup(tweet_id_list)
#             tw_list = list(tweets)
#             for ii in tw_list:
#                 text = re.sub('(\:.*?\:)', '', emoji.demojize(ii.text))
#                 text = text.replace("\n", " ")
#                 text1 = re.sub('(\:.*?\:)', '', emoji.demojize(ii.user.name))
#                 fid.write(text1 + ' ' + str(ii.user.id) + ' ' + str(ii.created_at) + ' ' + text + '\n')
#             i = 0
#             tag = 0
#         except Exception as e:
#             print(e)
#
# retrieve_tweets('clean_data/IDs_only_tweets_ID_user_tweet_datetime_2018_WalkAway_2018-07-05.tsv','results/retweets1.txt')
# retrieve_tweets('clean_data/IDs_only_tweets_ID_user_tweet_datetime_2018_WalkAway_2018-07-06.tsv','results/retweets2.txt')
# retrieve_tweets('clean_data/IDs_only_tweets_ID_user_tweet_datetime_2018_WalkAway_2018-07-07.tsv','results/retweets3.txt')
# retrieve_tweets('clean_data/IDs_only_tweets_ID_user_tweet_datetime_2018_WalkAway_2018-07-08.tsv','results/retweets4.txt')
# retrieve_tweets('clean_data/IDs_only_tweets_ID_user_tweet_datetime_2018_WalkAway_2018-07-09.tsv','results/retweets5.txt')
# retrieve_tweets('clean_data/IDs_only_tweets_ID_user_tweet_datetime_2018_WalkAway_2018-07-10.tsv','results/retweets6.txt')
# retrieve_tweets('clean_data/IDs_only_tweets_ID_user_tweet_datetime_2018_WalkAway_2018-07-11.tsv','results/retweets7.txt')
fid = open('clean_data/1.txt',encoding='utf-8')
for line in fid:
    line = line.strip()
    line = line.split('::')
    print(line)
