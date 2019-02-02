import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import tweepy
from bs4 import BeautifulSoup
from pprint import pprint
import sys
import subprocess
import urllib.request
import traceback

link=sys.argv[1]
print(sys.argv[2])
browser = webdriver.Chrome(executable_path = "C:\\Programs\\Twitter\\chromedriver.exe" )
browser.maximize_window()
browser.get(link)
browser.set_script_timeout(6)
pyautogui.click(pyautogui.size()[0]/2, pyautogui.size()[1]*2/10)
i=0
while i<int(sys.argv[2]):
        scroll = browser.find_element_by_tag_name('body').send_keys(Keys.END)
        time.sleep(1)
        i+=1
html = browser.page_source
soup = BeautifulSoup(html, "html.parser")
browser.quit()
Images=[]
i=0
for image in soup.findAll('img'):
        try:
                urllib.request.urlretrieve(str(image['src']), str(i)+".jpg")
        except:
                pass
        i+=1
print(len(Images))