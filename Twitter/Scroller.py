import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import tweepy
from bs4 import BeautifulSoup
from pprint import pprint
import sys

link=sys.argv[1]
#Add your twitter api details
auth = tweepy.OAuthHandler("SRlQpFisWbTpxh21kZVbLmmJa" , "BcTLet3NoXGCINwxMIYFvRpripwMpKB9epFt9XF543J6wsVNix") 
auth.set_access_token("4258423223-R19B09iB3TQVKc8SpasTZeAUt3ziRTBOZ2RzjwH","ZVcFnQsBI16ypnT7xsPsiATyvrSR6AdSHfwQUkcsusfUi") 
api = tweepy.API(auth) 
tweet = api.get_status(int(link.split("/")[-1]))
OverkillFactor=int(tweet._json["retweet_count"])
MainTweet=tweet._json["text"]
print(OverkillFactor)
#ScrollTime is amount of page down you want to click on that tweet
if(OverkillFactor>1000):
    ScrollTime=15
    print("Wont scrape Whole post")
else:
    ScrollTime=OverkillFactor/100
    print("Wait for Scrolling Time of"+str(ScrollTime))

#Add your chromedriver location
browser = webdriver.Chrome(executable_path = "C:\\Programs\\Twitter\\chromedriver.exe" )
browser.maximize_window()
browser.get(link)
time.sleep(3)
pyautogui.click(pyautogui.size()[0]/2, pyautogui.size()[1]*2/10)
i=0
while i<ScrollTime:
        scroll = browser.find_element_by_tag_name('body').send_keys(Keys.END)
        time.sleep(1)
        i+=1
html = browser.page_source
soup = BeautifulSoup(html, "html.parser")
browser.quit()
Dict={}
Dict["MainTweet"]=MainTweet
for i in soup.find_all("li",{"class":"ThreadedConversation--loneTweet"}):
    Dict[i.find("span",{"class":"username u-dir u-textTruncate"}).text]=i.find("div",{"class":"js-tweet-text-container"}).text.strip()
j=0
for i in soup.find_all("li",{"class":"ThreadedConversation"}):
    Thread=[]
    for singleTweet in i.find_all("div",{"class":"ThreadedConversation-tweet"}):
        Thread.append({singleTweet.find("span",{"class":"username u-dir u-textTruncate"}).text:singleTweet.find("div",{"class":"js-tweet-text-container"}).text.strip()})
    Dict[j]=Thread
    j+=1
with open('output.txt', 'w',encoding='utf-8') as out:
    pprint(Dict, stream=out)
