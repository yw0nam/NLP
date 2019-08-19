import urllib.request
import urllib.parse

#API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
API = "http://www.kma.go.kr/wid/queryDFSRSS.jsp"
values = {		# dictionary 자료형 : key-value 쌍
    'zone': '2818582000'
}
params = urllib.parse.urlencode(values)

url = API + "?" + params	# GET 형식으로 매개변수 전송
print("url = ", url)

data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)
