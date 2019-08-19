from bs4 import BeautifulSoup
import urllib.request as req

url = "http://finance.naver.com/marketindex/"
res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

#prices = soup.select_one("div.head_info > span.value").string
#prices = soup.select("div.head_info > span.value")
prices = soup.select("span.value")

print("달러: " + prices[0].string)
print("엔: " + prices[1].string)
print("유로: " + prices[2].string)

#for price in prices:
#    print(price + "원")





