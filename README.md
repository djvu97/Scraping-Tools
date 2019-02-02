# Scraping Tools
Requirement:-  
pip install bs4  
pip install selenium  
pip install pyautogui  
pip install tweepy(For Twitter)  
https://chromedriver.storage.googleapis.com/index.html?path=2.46/ (Download any one according to your OS)  

Twitter:-
python Scroller.py <tweetlink> 
Eg:- 
  python Scroller.py https://twitter.com/ILMentoring/status/1086010115151540224

This will make a output.txt where a python dictionary type data will be stored  
If the key is a number then inner list will be replies threads in that comments  
If the key is a twitter handle then there is only one reply from that person no one else replied to that reply
If the key is MainTweet then that tweet is the main Tweet of the Post
  
Instagram:-  
python Instagram.py <profile> <Number of scrolls you want to make(to load new pictures also)>  
Eg:-
  python Instagram.py https://www.instagram.com/instagram/ 7  
After the execution, you will get all the picture downloaded(which were loaded due to those many page down clicks)  
