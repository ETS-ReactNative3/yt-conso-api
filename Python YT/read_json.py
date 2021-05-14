import json
from myFunctions import YouTube_Google_Log_In, YouTube_Google_Log_Out, YouTube_Acces_Website, YouTube_Accept_Cookies, YouTube_Deny_Log_In, YouTube_Toggle_AutoPlay, YouTube_Get_Video_Id_From_Url, scrollDown, find_video, select_video,watch_the_video_for, dislike_video, like_video, go_to_channel, search_with_url, search_bar, find_video_length_in_seconds, Launch_ChromeDriver
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from flags import Flag
from crement import Lever
import time
import random
import undetected_chromedriver.v2 as uc


# SE LOGER SUR COMPTE GOOGLE

# Faire que les x["watchContext"]["stopsAt"] soient des nombres ou "never"
# Le paramètre doit être un nombre qui indique le nombre de seconde
# Comment gérer currentAction (dans la configuration actuelle, le comportement executé n'est pas celui attendu
# Il faut se login ;; ça sera dans les settings
# ajouter l'adblock



myFlag = Flag()
myLever = Lever()


driver = Launch_ChromeDriver()
time.sleep(2)

with open('bot.json') as jfile:
    file = json.load(jfile)["0"]

YouTube_Acces_Website()
time.sleep(2)
YouTube_Accept_Cookies()
time.sleep(2)
YouTube_Deny_Log_In()

thisSession = str(int(time.time()))
toggle_auto_play_bool = False
currentAction = 0

requests.post("http://test.netops.fr/api/session/new", headers={"accept":"application/ld+json","Content-Type": "application/ld+json"}, json={"id":thisSession})

with open("sessionURL--"+time.strftime("%d-%m-%y@%Hh%Mm%Ss",time.localtime()) + ".txt",'w+') as urlFile:
    for x in file:
        if x["action"] == 'settings':
            currentAction = 1
            if "autoPlay" in x["options"]:
                toggle_auto_play_bool = True 
        elif x["action"] == 'search':
            currentAction = 2
            search_bar(x["toSearch"])
        elif x["action"] == 'watch':
            currentAction = 3
            if "url" in x:
                search_with_url(x["url"])
            elif "index" in x :
                select_video(x["index"])
            if "watchContext" in x:
                # LA : le paramètre doit être un nombre qui indique le nombre de seconde
                if x["watchContext"]["stopsAt"] == "never":
                    watch_the_video_for(find_video_length_in_seconds())
                else :
                    watch_the_video_for(x["watchContext"]["stopsAt"])
                if "social" in x["watchContext"]:
                    if x["watchContext"]["social"] == 'like':
                        currentAction = 4
                        like_video()
                    else :
                        currentAction = 5
                        dislike_video()
            if toggle_auto_play_bool:
                YouTube_Toggle_AutoPlay()
                toggle_auto_play_bool = False
            # Send video id + all videos id
            currentVideo = driver.current_url
            listVideos = find_video()
            requests.post("http://test.netops.fr/api/log/new", headers={"accept":"application/ld+json","Content-Type": "application/ld+json"}, json={"session":thisSession,"currentVideo":YouTube_Get_Video_Id_From_Url(currentVideo),"action":currentAction, "videos":listVideos})
        elif x["action"] == 'goToChannel':
            currentAction = 6
            go_to_channel()
    
