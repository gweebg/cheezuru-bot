# Libraries used #

from bs4 import BeautifulSoup
import requests
import time
import tweepy
import schedule
import os
from os import environ
from threading import Thread

ep_num = 10             #MAKE ENVIRONMENTAL VARIABLE
chapter_num = 155       #MAKE ENVIRONMENTAL VARIABLE
ANIME_LOOP = 0
MANGA_LOOP = 0

# Debug message function #

def debug_msg(msg):

    print("-"*100)
    print(msg)
    print("-"*100)

# Anime requesting function #

def request_anime():

    url = "https://nyaa.si/?f=0&c=0_0&q=Kanojo+Okarishimasu"
    watch_url = "https://www.crunchyroll.com/rent-a-girlfriend"

    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    mydivs = soup.find_all('div', {'class':'table-responsive'})
    title = "[HorribleSubs]"

    global ep_num
    global ANIME_LOOP

    for div in mydivs:

        link_shows = div.find_all('a')

        for link in link_shows:

            name_raw = link.text

            if title in name_raw:

                if str(ep_num) in name_raw:

                    debug_msg("episode {} has released".format(ep_num))
                    send_tweet("Episode {} of Kanojo Okarishimasu has released!\n Go watch it:\n {}!".format(ep_num,watch_url))
                    ep_num += 1
                    debug_msg("looking for {}".format(ep_num))

                    time.sleep(0.8)
                    break

                else:

                    time.sleep(0.8)
                    continue

            else:

                continue

    r.close()
    ANIME_LOOP += 1 
    print("anime looped {} time(s)".format(ANIME_LOOP))

        
# Manga requesting function #

def request_manga():

    url = "https://mangadex.org/title/22151/kanojo-okarishimasu"

    r = requests.get(url)

    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    mydivs = soup.find_all('div', {'class':'row no-gutters'})
    title = "Black Cat Scanlations"
    global chapter_num
    global MANGA_LOOP
        
    for div in mydivs:

        chap_found = div.find_all('div',{'class':'col'})
                
        for chap in chap_found:

            chap_name = chap.text
               
            if title in chap_name:

                if str(chapter_num) in chap_name:

                    debug_msg("chapter {} has released".format(chapter_num))
                    send_tweet("Chapter {} of Kanojo Okarishimasu has released!\n Go read it in:\n {}!".format(chapter_num,url))
                    chapter_num += 1
                    debug_msg("looking for chapter {}".format(chapter_num))

                    time.sleep(0.8)
                    break

                else:

                    time.sleep(0.8)
                    continue
            else:

                continue
        
    r.close() 
    MANGA_LOOP += 1 
    print("anime looped {} time(s)".format(MANGA_LOOP))
        
# Tweeting function #

def send_tweet(tweet):

    consumer_key = environ['CONSUMER_KEY']
    consumer_secret = environ['CONSUMER_SECRET']
    access_token = environ['ACCESS_TOKEN']
    access_token_secret = environ['ACCESS_TOKEN_SECRET']

    def OAuth():

        try: 
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            return auth

        except Exception as e:
            return e

    oauth = OAuth()
    api = tweepy.API(oauth)

    api.update_status(tweet)

# Run parallel functions function #

def run_thread():

    Thread(target = request_anime).start()
    Thread(target = request_manga).start()

# Shedule when to run # 

schedule.every(10).minutes.do(run_thread)

# Main #

while True:

    schedule.run_pending()
    time.sleep(1)


          
    






 

