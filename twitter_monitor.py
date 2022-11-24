# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 12:43:40 2019

@author: Minh
"""

import json
import requests
import tweepy
import base64
import sys
import time
import os
import csv
from AlarmDialogUtil import showAlertDialog

class TwitterMonitor():
    twitter_public = twitter_private = access_token = access_token_secret =  ''
    
    def __init__(self):
        #fill out with keys
        self.twitter_public = 'CONSUMER_KEY'
        self.twitter_private = 'CONSUMER_SECRET'
        self.access_token = 'ACCESS_TOKEN'
        self.access_token_secret = 'ACCESS_SECRET'
        
    def monitor(self):
        twitter_ids = list(123432, 32423432, 23432423) #random examples
        
        auth = tweepy.OAuthHandler(self.twitter_public, self.twitter_private)
        auth.set_access_token(self.access_token, self.access_token_secret)
            
        api = tweepy.API(auth)
        streamListener = self.AlertStreamListener()
        stream = tweepy.Stream(auth = api.auth, listener=streamListener)
        stream.filter(follow=twitter_ids)
        
    class AlertStreamListener(tweepy.StreamListener):
        
        def on_status(self, status):
            if(not hasattr(status, 'retweeted_status') and status.in_reply_to_status_id_str == None
               and status.in_reply_to_user_id_str == None):
                title = status.user.name
                text = "text: {} \n\n url:{}".format(status.text, status.entities['urls'])
                showAlertDialog(title, text)
                with open("twitter/TwitterMonitorLog", "a") as file:
                    file.write(json.dumps(status._json) + "\n\n")
            
        def on_error(self, status_code):
            if status_code == 420:
                print("error on connecting to stream: 420 ; time: {}".format(time.time()))
                #returning False in on_error disconnects the stream
                return False
        
if __name__ == "__main__":
   while True:
       try:
           TwitterMonitor().monitor()
       except Exception as e:
           showAlertDialog("Error", "Program exited:\n" + str(e))
           time.sleep(60)
    
    
    