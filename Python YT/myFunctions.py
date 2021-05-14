from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

from flags import Flag
from crement import Lever
import time
import random
import undetected_chromedriver.v2 as uc
import json
import requests


myFlag = Flag()
myLever = Lever()

PATH = r"C:\chromedriver.exe"
# driver = webdriver.Chrome(PATH)

#options = uc.ChromeOptions()
#options.add_extension("./extension_1_35_2_0.crx")
#driver = uc.Chrome()



#Options for the ChromeDriver

opt = webdriver.ChromeOptions()
caps = webdriver.DesiredCapabilities.CHROME.copy()

opt.add_argument("--no-sandbox")
opt.add_argument("--disable-gpu")
opt.add_argument("--allow-running-insecure-content")
opt.add_argument("--ignore-ssl-errors=yes")
opt.add_argument("--window-size=1280,720")
opt.add_argument("--ignore-certificate-errors")
opt.add_argument("--disable-dev-shm-usage")
opt.add_extension("./extension_1_35_2_0.crx")
caps['goog:loggingPrefs'] = { 'browser':'ALL' }


#Load the driver
#driver = webdriver.Chrome(PATH, options=opt, desired_capabilities=caps)
driver = uc.Chrome(PATH, options=opt, desired_capabilities=caps)

with open('bot.json') as jfile:
    file = json.load(jfile)["0"]



def YouTube_Google_Log_In(email, password):
    try:
        driver.find_element_by_css_selector("#buttons > ytd-button-renderer > a").click()
        emailInput = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#identifierId")))
        emailInput.send_keys(email)
        time.sleep(0.5)
        driver.find_element_by_css_selector("#identifierNext > div > button").click()
        passwordInput = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input")))
        passwordInput.send_keys(password)
        time.sleep(2)
        driver.find_element_by_css_selector("#passwordNext > div > button").click()
        time.sleep(0.5)
        driver.find_element_by_css_selector("#yDmH0d > c-wiz > div > div > div > div.L5MEH.Bokche.ypEC4c > div.lq3Znf > div.U26fgb.O0WRkf.oG5Srb.HQ8yf.C0oVfc.Zrq4w.WIL89.k97fxb.yu6jOd.M9Bg4d.j7nIZb > span > span").click()
    except:
        print("Error in YouTube_Google_Log_In(email, password)")

def YouTube_Google_Log_Out():
    try:
        driver.get(driver.current_url + "logout/")
    except:
        print("Error in YouTube_Google_Log_Out()")

def YouTube_Acces_Website():
    try:
        driver.get("https://www.youtube.com/")
    except:
        print("Error in YouTube_Acces_Website()")

def YouTube_Accept_Cookies():
    try:
        driver.find_element_by_css_selector("#yDmH0d > c-wiz > div > div > div > div.NIoIEf > div.G4njw > div.qqtRac > form > div.lssxud > div > button").click()
    except:
        print("Error in YouTube_Accept_Cookies()")

def YouTube_Deny_Log_In():
    try:
        driver.find_element_by_xpath("/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/yt-upsell-dialog-renderer/div/div[3]/div[1]/yt-button-renderer/a/tp-yt-paper-button/yt-formatted-string").click()
        time.sleep(1)
        driver.switch_to.default_content()
    except:
        print("Error in YouTube_Deny_Log_In()")

def YouTube_Toggle_AutoPlay():
    try:
        driver.find_element_by_css_selector("#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button:nth-child(1) > div > div").click()
    except:
        print("Error in YouTube_Toggle_AutoPlay()")

def YouTube_Get_Video_Id_From_Url(url):
    try:
        if url == "https://www.youtube.com/":
            return ''
        return url.split("=")[1].split("&")[0]
    except:
        print("Error in YouTube_Get_Video_Id_From_Url(url)")
        return ''

def YouTube_Music_No_Thanks():
    try:
        driver.find_element_by_css_selector("ytd-button-renderer#dismiss-button > a > tp-yt-paper-button > yt-formatted-string").click()
    except:
        print("Error in YouTube_Music_No_Thanks()")
        
def home_page():
    try:
        driver.find_element_by_css_selector("#logo > a > div > #logo-icon").click()
    except:
        print("Error in home_page()")

def scrollDown():
    try:
        driver.execute_script("window.scrollBy(0,1500);")
    except:
        print("Error in scrollDown()")

def find_caption():
    try:
        driver.find_element_by_xpath("//div[3]/div/ytd-menu-renderer/yt-icon-button/button/yt-icon").click()
        driver.find_elements_by_css_selector(".ytd-menu-popup-renderer > ytd-menu-service-item-renderer")[0].click()
        caption = "".join([e.get_attribute('innerHTML') for e in driver.find_elements_by_css_selector("div.cue-group > div > div")])
        return caption
    except:
        print("Error in find_caption()")
        return ''

def find_video():
    try:
        l = []
        #for x in driver.find_elements_by_css_selector("#thumbnail"):
        for x in driver.find_elements_by_css_selector("#dismissible > ytd-thumbnail > a#thumbnail"):
            url = x.get_attribute("href")
            if url == None:
                continue
            idVideo = YouTube_Get_Video_Id_From_Url(url)
            l.append(idVideo)
        return l
    except:
        print("Error in find_video")

def select_video(n=0):
    try:
        currUrl = driver.current_url
        if currUrl == "https://www.youtube.com/":
            # From homepage
            print("homepage")
            driver.find_elements_by_css_selector("#contents > ytd-rich-item-renderer")[n].click()
        elif "watch?v=" in currUrl:
            # From a watching video
            print("video")
            driver.find_elements_by_css_selector("#items > ytd-compact-video-renderer")[n].click()
        elif "results?search_query=" in currUrl:
            # From a search
            print("search")
            driver.find_elements_by_css_selector("#contents > ytd-video-renderer > #dismissible > ytd-thumbnail")[n].click()
        else:
            # From a video tab from a channel
            print("channel")
            driver.find_elements_by_css_selector("#items > ytd-grid-video-renderer")[n].click()
    except:
        print("Error in select_video()")

        
def find_video_length_in_seconds():
    try :
        strTime = driver.find_element_by_css_selector("#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > div.ytp-time-display.notranslate > span.ytp-time-duration").text
        listTime = strTime.split(":")[::-1]
        res = 0
        for i in range(len(listTime)):
            res += int(listTime[i]) * (60**i)
        return res
    except :
        print("Error in find_video_length_in_seconds()")

def watch_the_video_for(n=0):
    try:
        time.sleep(n)
    except:
        print("Error in watch_the_video_for()")

def dislike_video():
    try:
        driver.find_element_by_css_selector(".ytd-video-primary-info-renderer > #top-level-buttons > .style-scope:nth-child(2) #button > #button > .style-scope").click()
    except:
        print("Error in dislike_video()")
    
def like_video():
    try:
        driver.find_element_by_css_selector(".ytd-video-primary-info-renderer > #top-level-buttons > .style-scope:nth-child(1) #button > #button > .style-scope").click()
    except:
        print("Error in like_video()")

def go_to_channel():
    try:
        driver.find_element_by_css_selector("#top-row > ytd-video-owner-renderer > a").click()
        videoTab = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#tabsContent > tp-yt-paper-tab")))
        time.sleep(1)
        videoTab[1].click()
    except:
        print("Error in go_to_channel()")

def search_with_url(url):
    try:
        driver.get(url)
    except:
        print("Error in search_with_url()")

def search_bar(text):
    try:
        # Query
        driver.find_element_by_css_selector("#search-input > #search").clear()
        driver.find_element_by_css_selector("#search-input > #search").send_keys(text)
        driver.find_element_by_css_selector("#search-icon-legacy").click()
    except:
        print("Error in search_bar()")

def robot(file):
    for x in file:
        if x["action"] == 'settings':
            #Envoyer à Sylvain les settings modifés
            currentAction = 1
            if "autoPlay" in x["options"]:
                toggle_auto_play_bool = True
        elif x["action"] == 'search':
            #Envoyer à Sylvain les mots clefs
            currentAction = 2
            search_bar(x["toSearch"])
        elif x["action"] == 'watch':
            #Envoyer à Sylvain l'id de la vidéo et les id de toutes les vidéos
            currentAction = 3
            if "url" in x:
                search_with_url(x["url"])
            elif "index" in x :
                select_video(x["index"])
            if "watchContext" in x:
                if x["watchContext"]["stopsAt"] == "never":
                    watch_the_video_for(find_video_length_in_seconds())
                else :
                    watch_the_video_for(int(x["watchContext"]["stopsAt"]))
                if "social" in x["watchContext"]:
                    if x["watchContext"]["social"] == 'like':
#                        Envoyer à Sylvain le like de cette vidéo
                        like_video()
                    else :
#                        Envoyer à Sylvain le dislike de cette vidéo
                        currentAction = 5
                        dislike_video()
            if toggle_auto_play_bool:
                YouTube_Toggle_AutoPlay()
                toggle_auto_play_bool = False
            # Send video id + all videos id
            currentVideo = driver.current_url
            listVideos = find_video()
    #        requests.post("http://test.netops.fr/api/log/new", headers={"accept":"application/ld+json","Content-Type": "application/ld+json"}, json={"session":thisSession,"currentVideo":YouTube_Get_Video_Id_From_Url(currentVideo),"action":currentAction, "videos":listVideos})
        elif x["action"] == 'goToChannel':
            currentAction = 6
            go_to_channel()
        print(YouTube_Get_Video_Id_From_Url(driver.current_url))
        time.sleep(1)            
        







YouTube_Acces_Website()
time.sleep(2)
YouTube_Accept_Cookies()
time.sleep(2)
YouTube_Deny_Log_In()

thisSession = str(int(time.time()))
toggle_auto_play_bool = False
was_done = False
currentAction = 0

#requests.post("http://test.netops.fr/api/session/new", headers={"accept":"application/ld+json","Content-Type": "application/ld+json"}, json={"id":thisSession})
print(thisSession)

#for x in file:
#    if x["action"] == 'settings':
#        currentAction = 1
#        if "autoPlay" in x["options"]:
#            toggle_auto_play_bool = True
#    elif x["action"] == 'search':
#        currentAction = 2
#        search_bar(x["toSearch"])
#    elif x["action"] == 'watch':
#        currentAction = 3
#        if "url" in x:
#            search_with_url(x["url"])
#        elif "index" in x :
#            select_video(x["index"])
#        if "watchContext" in x:
#            # LA : le paramètre doit être un nombre qui indique le nombre de seconde
#            if x["watchContext"]["stopsAt"] == "never":
#                watch_the_video_for(find_video_length_in_seconds())
#            else :
#                watch_the_video_for(int(x["watchContext"]["stopsAt"]))
#            if "social" in x["watchContext"]:
#                if x["watchContext"]["social"] == 'like':
#                    currentAction = 4
#                    like_video()
#                else :
#                    currentAction = 5
#                    dislike_video()
#        if toggle_auto_play_bool:
#            YouTube_Toggle_AutoPlay()
#        # Send video id + all videos id
#        currentVideo = driver.current_url
#        listVideos = find_video()
##        requests.post("http://test.netops.fr/api/log/new", headers={"accept":"application/ld+json","Content-Type": "application/ld+json"}, json={"session":thisSession,"currentVideo":YouTube_Get_Video_Id_From_Url(currentVideo),"action":currentAction, "videos":listVideos})
#    elif x["action"] == 'goToChannel':
#        currentAction = 6
#        go_to_channel()
#    print(YouTube_Get_Video_Id_From_Url(driver.current_url))
#    time.sleep(1)

fin = 1
#Envoyer les données d'actions à chaque pas ; discuter avec Sylvain
#Ajouter adblock
#Verifier l'integrité des données avec un screenshot de la page ; faire un plan de test :
#    Enregister le code affiché de la page avant d'exécuter une fonction
#    Pour un select_video() :
#        S'assurer que l'url ouverte par le robot correspond bien à la n-ième url dans le code de la page enregistré
#    Pour find_video() :
#        S'assurer que toutes les vidéos de la page ont bien été chargés dans la liste
#    Pour go_to_channel() :
#        S'assurer que la chaine ouverte par le robot correspond bien à la chaine de la page d'avant
#    Pour search_bar() :
#        S'assurer que l'url coresponde bien aux mots tapés, avec correction URL Special encoding : https://secure.n-able.com/webhelp/NC_9-1-0_SO_en/Content/SA_docs/API_Level_Integration/API_Integration_URLEncoding.html
#    Pour like_video() :
#        Vérifier que le driver.find_element_by_css_selector(".ytd-video-primary-info-renderer > #top-level-buttons > .style-scope:nth-child(1) #button > #button").get_attribute("aria-pressed") == True
#    Pour dislike_video() :
#        Vérifier que le driver.find_element_by_css_selector(".ytd-video-primary-info-renderer > #top-level-buttons > .style-scope:nth-child(2) #button > #button").get_attribute("aria-pressed") == False
#    Pour find_video_length_in_seconds() :
#        Vérifier que dans le code de la page enregistré, la longueure convertie correspond bien
#    Pour scroll_down :
#        Vérifier que le code de la page est plus long que le code enregistré
#    Pour YouTube_Toggle_AutoPlay() :
#        Vérifier que driver.find_element_by_css_selector("#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button:nth-child(1) > div > div").get_attribute("href") est différent entre le code de la page enregistré et le code actuel
#    Pour YouTube_Google_Log_Out :
#        Vérfier que len(driver.find_element_by_css_selector("yt-formatted-string#text.style-scope.ytd-button-renderer.style-suggestive.size-small")) == 1
#    Pour YouTube_Google_Log_In(email, password) :
#        Vérifier que len(driver.find_element_by_css_selector("yt-formatted-string#text.style-scope.ytd-button-renderer.style-suggestive.size-small")) == 0
#    Pour YouTube_Acces_Website() :
#        Vérifier que driver.current_url = 'https://www.youtube.com/'
#    Pas de tests pour :
#        YouTube_Accept_Cookies()
#        YouTube_Deny_Log_In()
#        YouTube_Get_Video_Id_From_Url()
#        watch_the_video_for()

#Verifier sur un serveur
    
#Envoyer toutes les données à Sylvain
#Corriger les bugs
#Faire le plan de test
#A moi de faire l'index