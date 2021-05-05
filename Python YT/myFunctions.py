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


myFlag = Flag()
myLever = Lever()

PATH = r"C:\chromedriver.exe"
# driver = webdriver.Chrome(PATH)
driver = uc.Chrome()


def YouTube_Google_Log_In(email, password):
    try:
        driver.find_element_by_css_selector("#buttons > ytd-button-renderer > a").click()
        emailInput = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#identifierId")))
        emailInput.send_keys(email)
        time.sleep(0.5)
        driver.find_element_by_css_selector("#identifierNext > div > button").click()
        passwordInput = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input")))
        passwordInput.send_keys(password)
        time.sleep(0.5)
        driver.find_element_by_css_selector("#passwordNext > div > button").click()
    except:
        print("Error in YouTube_Google_Log_In(email, password)")

def YouTube_Google_Log_Out():
    try:
        driver.find_element_by_css_selector("#img").click()
        time.sleep(1)
        signOut = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#label")))
        signOut.click()
        noTx = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-channel-warm-welcome-renderer/div/div[2]/div[3]/div[2]/ytd-button-renderer/a/tp-yt-paper-button/yt-formatted-string")))
        noTx.click()
        driver.switch_to.default_content()
    except:
        print("Error in YouTube_Google_Log_Out()")

def YouTube_Acces_Website():
    try:
        driver.get("https://www.youtube.com/")
    except:
        print("Error in YouTube_Acces_Website()")

def YouTube_Accept_Cookies():
    try:
        driver.find_element_by_xpath("/html/body/div/c-wiz/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button").click()
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
        print(url.split("=")[1].split("&")[0])
    except:
        print("Error in YouTube_Get_Video_Id_From_Url(url)")

def scrollDown():
    try:
        driver.execute_script("window.scrollBy(0,1500);")
    except:
        print("Error in scrollDown()")

def find_video():
    try:
        l = []
        d = dict()
        i = 0
        for x in driver.find_elements_by_css_selector("#thumbnail"):
            print(x.get_attribute("href"))
            l.append(x.get_attribute("href"))
            i += 1
        print(i)
        #return d[driver.current_url] = l
    except:
        print("Error in find_video")

def select_video(n=1):
    print(n)
    try:
        if driver.current_url == "https://www.youtube.com/":
            # From homepage
            # TODO : Tous ce qui est dans des sections est inselectionnable
            print("homepage")
            driver.find_elements_by_xpath('//ytd-app/div[@id="content"]/ytd-page-manager[@id="page-manager"]/ytd-browse/ytd-two-column-browse-results-renderer/div[@id="primary"]/ytd-rich-grid-renderer/div[@id="contents"]/ytd-rich-item-renderer')[n].click()
        elif "watch?v=" in driver.current_url:
            # From a watching video
            print("video")
            driver.find_elements_by_xpath('//div[@id="primary-inner"]/div[@id="related"]/ytd-watch-next-secondary-results-renderer/div[@id="items"]/ytd-compact-video-renderer')[n].click()
        elif "results?search_query=" in driver.current_url:
            # From a research
            print("research")
            driver.find_elements_by_xpath('//div[@id="content"]/ytd-page-manager[@id="page-manager"]/ytd-search/div[@id="container"]/ytd-two-column-search-results-renderer/div[@id="primary"]/ytd-section-list-renderer/div[@id="contents"]/ytd-item-section-renderer/div[@id="contents"]/ytd-video-renderer')[n].click()
        else:
            print("channel")
            videoTab = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#tabsContent > tp-yt-paper-tab:nth-child(4) > div")))
            videoTab.click()
            driver.find_elements_by_xpath('//*[@id="items"]/ytd-grid-video-renderer')[n].click()
        
    except (NoSuchElementException, ElementNotInteractableException, IndexError):
        if myLever.get() == 0:
            print(str(myLever.get()))
            myLever.incr()
            # Scroll down
            select_video(n+1)
        else:
            print("Error in select_video()")
    finally:
        myLever.setLever(0)

def watch_the_video_for(n=0):
    try:
        time.sleep(n)
    except:
        print("Error in watch_the_video_for()")

def dislike_video():
    try:
        driver.find_element_by_xpath("//ytd-toggle-button-renderer[2]/a/yt-icon-button/button/yt-icon").click()
    except:
        print("Error in dislike_video()")
    
def like_video():
    try:
        driver.find_element_by_xpath("//ytd-toggle-button-renderer/a/yt-icon-button/button/yt-icon").click()
    except:
        print("Error in like_video()")

def go_to_channel():
    try:
        driver.find_element_by_xpath("//ytd-video-owner-renderer/a/yt-img-shadow/img").click()
    except:
        print("Error in go_to_channel()")

def search_with_url(url):
    try:
        driver.get(url)
    except:
        print("Error in search_with_url()")

def search_bar(text):
    try:
        driver.find_element_by_id("search").send_keys(text)
        driver.find_element_by_id("search-icon-legacy").click()
    except:
        print("Error in search_bar()")
