from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flags import Flag
import time
import os
from googleapiclient.discovery import build
import googleapiclient.errors

myAPIYouTubeKey = 'AIzaSyBEkQeSVr0S0kh0OAj5PR4EexFbb-e6fSk'
myClientId = '708274977995-a6olhaq2oqf661uulukfl1tgl80m2pc3.apps.googleusercontent.com'
myClientSecret = 'SyUtUZBKTO2DeSASooc9c1Zv'
mySecretFileName = 'client_secret_708274977995-a6olhaq2oqf661uulukfl1tgl80m2pc3.apps.googleusercontent.com'


myFlag = Flag()

PATH = "C:\chromedriver.exe"
driver = webdriver.Chrome(PATH)

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

driver.find_elements_by_id("channel-name")[0].
'''
TODO

search_bar(text)       -- Validate
search_with_url(url)   -- Validate
go_to_channel()        -- Validate
#select_video()
like_the_video()       -- Validate
dislike_the_video()    -- Validate
watch_the_video_for() --> time.sleep(random.randint(0,"max video length")
'''

def dislike_video():
    driver.find_element_by_xpath("//ytd-toggle-button-renderer[2]/a/yt-icon-button/button/yt-icon").click()
	
def like_video():
    driver.find_element_by_xpath("//ytd-toggle-button-renderer/a/yt-icon-button/button/yt-icon").click()

def go_to_channel():
    driver.find_element_by_xpath("//ytd-video-owner-renderer/a/yt-img-shadow/img").click()
    """
    myUrl = driver.find_elements_by_id("channel-name")[0].find_element_by_class_name("yt-simple-endpoint").get_attribute("href")
    search_with_url(myUrl)
    """

def search_with_url(url):
    driver.get(url)

def search_bar(text):
    driver.find_element_by_id("search").send_keys(text)
    driver.find_element_by_id("search-icon-legacy").click()



def YouTube_Find_First_Video_Link():
    driver.get("https://www.youtube.com/")
    time.sleep(1)
    driver.find_element_by_xpath("//yt-button-renderer/a/paper-button/yt-formatted-string").click()
    time.sleep(1)
    driver.switch_to.frame("iframe")
    driver.find_element_by_css_selector("div#introAgreeButton").click()
    time.sleep(1)
    driver.switch_to.default_content()
    print(driver.find_element_by_xpath("//a[@id='video-title-link']").get_attribute("href"))

def YouTube_Deny_Log_In():
    # Probably not working
    driver.find_element_by_xpath("//yt-button-renderer/a/paper-button/yt-formatted-string").click()
    time.sleep(1)
    driver.switch_to.default_content()

def YouTube_Acces_Website():
    driver.get("https://www.youtube.com/")

def YouTube_Deny_Log_In_And_Validate_General_Condition():
    driver.find_element_by_xpath("//yt-button-renderer/a/paper-button/yt-formatted-string").click()
    time.sleep(1)
    driver.switch_to.frame("iframe")
    driver.find_element_by_css_selector("div#introAgreeButton").click()
    time.sleep(1)
    driver.switch_to.default_content()
  
def YouTube_Get_First_Video_Link():
    # You need to be on YouTube home page to call
    print(driver.find_element_by_xpath("//a[@id='video-title-link']").get_attribute("href"))

def YouTube_Click_On_First_Video_From_Home_Page():
    driver.find_element_by_xpath("//a[@id='video-title-link']").click()
  
  
def YouTube_Get_Video_Title_From_Url(url):
    # You need to have validate the 2 pop up before using it
    driver.get(url)
    print(driver.find_element_by_xpath("//h1[@class='title style-scope ytd-video-primary-info-renderer']").text)

def YouTube_Get_Video_Title_From_Page():
    print(driver.find_element_by_xpath("//h1[@class='title style-scope ytd-video-primary-info-renderer']").text)
    
def YouTube_Get_Current_Url():
    print(driver.current_url)
    
def YouTube_Get_Current_Video_Id():
    print(driver.current_url.split("=")[1].split("&")[0])

def YouTube_Get_Video_Id_From_Url(url):
    print(url.split("=")[1].split("&")[0])
    

## Changer la fonction pour qu'elle prenne en paramètre l'ID de la vidéo
def YouTube_Get_Comments_From_Video_Id():
    # Ne fonctionne pas ; peuit-être faut-il être owner de la vidéo pour pouvoir récupérer les commentaires
    with build('youtube','v3',developerKey='AIzaSyDQpIOHBpjzWLy2iZCWJHbCNAmXi_Fcyt0') as youtube_API:
        myRequest = youtube_API.comments().list(
            part='id',
            id='WUvTyaaNkzM'
        )
        myResponse = myRequest.execute()
        print(type(myResponse))
        print(myResponse)
        print(myResponse['items'])

def YouTube_Get_Captions_From_Video_Id():
    # Ajouter les autorisations pour récupérer les captions
    with build('youtube','v3',developerKey='AIzaSyDQpIOHBpjzWLy2iZCWJHbCNAmXi_Fcyt0') as youtube_API:
        myRequest = youtube_API.captions().download(
            id='WUvTyaaNkzM',
        )
        myResponse = myRequest.execute()
        print(type(myResponse))
        print(myResponse)

#YouTube_Get_Captions_From_Video_Id()

def a():
    driver.get("https://www.youtube.com/")
    time.sleep(1)
    driver.find_element_by_xpath("//yt-button-renderer/a/paper-button/yt-formatted-string").click()
    time.sleep(1)
    driver.switch_to.frame("iframe")
    driver.find_element_by_css_selector("div#introAgreeButton").click()
    time.sleep(1)
    driver.switch_to.default_content()
    driver.find_element_by_xpath("//a[@id='video-title-link']").click()

a()

def lastChance():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"
    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)
    request = youtube.captions().list(part="snippet",videoId="M7FIvfx5J10")
    response = request.execute()
    print(myResponse)



'''
# Flag 0
myFlag.plantFlag()

driver.get("https://www.youtube.com/")

# Flag 1
myFlag.plantFlag()

time.sleep(1)
driver.find_element_by_xpath("//yt-button-renderer/a/paper-button/yt-formatted-string").click()
# Flag 2
myFlag.plantFlag()
time.sleep(1)

#driver.find_element_by_xpath("//div[@id='introAgreeButton']/span/span").click()



#driver.switch_to_frame("iframe")
driver.switch_to.frame("iframe")
driver.find_element_by_css_selector("div#introAgreeButton").click()




# Flag 3
myFlag.plantFlag()
time.sleep(1)

driver.switch_to.default_content()
#print(driver.page_source)
#driver.find_element_by_xpath("//div[@id='introAgreeButton']/span/span").click()
print(driver.find_element_by_xpath("//a[@id='video-title-link']").get_attribute("href"))
'''

'''
button
text
label-container
thumbnail
'''

'''
try:
    a = driver.find_elements_by_xpath("//div[@id='thumbnail']")
    print(a)
    a.click()
    
    print("Guacamole")
finally:
    # Flag 2
    myFlag.plantFlag()





'''





'''
# Flag 0
myFlag.plantFlag()



# Flag 1
myFlag.plantFlag()

driver.get("https://www.youtube.com/")

# Flag 2
myFlag.plantFlag()
time.sleep(7)

"""
try:
    validate = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//paper-button[@id='button' and @aria-label='Non merci'"))
    )
    print(validate.text)
    accept = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "introAgreeButton"))
    )
    accept.click()
    
finally:
    # Flag 3
    myFlag.plantFlag()
    
"""
try:
    firstVid = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "yt-simple-endpoint inline-block style-scope ytd-thumbnail"))
    )
    print(firstVid)
    print(firstVid.find_element_by_xpath('//a[contains(@href,"href")]'))
finally:
    # Flag 4
    myFlag.plantFlag()
#    driver.quit()
    
    
    
    
    
    
    
    
    
    
NB = """
search = driver.find_element_by_id("search")
search.send_keys("Coronavirus")
search.send_keys(Keys.RETURN)

driver.page_source
"""
'''

