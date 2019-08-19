import sys
import urllib.request as req	# 모듈 이름을 원하는 이름으로 변경해서 사용(alias)
import urllib.parse as parse

if len(sys.argv) <= 1:		# argv[0] : 스크립트 이름, argv[1]: 매개변수 
    print("USAGE: download-forecast-argv <Region Number>")
    sys.exit()			# python 실행 중단. quit()도 사용 가능
regionNumber = sys.argv[1]

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stnId': regionNumber
}
params = parse.urlencode(values)	# 한국어 매개변수일 경우에는 인코딩이 필요

url = API + "?" + params
print("url = ", url)

data = req.urlopen(url).read()
text = data.decode("utf-8")
print(text)
