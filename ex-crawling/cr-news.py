import urllib.request
from bs4 import BeautifulSoup
import time
                   
url = "https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=100"
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, "html.parser")
newslist = soup.select("#main_content div div._persist div.cluster_body ul div.cluster_text a")
if newslist == []:
    print("newlist is null")
else:
    print("newlist is Not null")
    for a in newslist:
        print(a.string)
