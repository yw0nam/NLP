from bs4 import BeautifulSoup
import urllib.request as req
from xml.etree import ElementTree   # xml parsing module

url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=2818582000"
res = req.urlopen(url)

tree = ElementTree.parse(res) # parsing the XML file
root = tree.getroot()         # get the root element 

title = root.find("channel/title").text
print(title)

ref = "channel/item/description/body/data"

print('시간대별 날씨 예보')
last_index = len(root.findall(ref))
for data in root.findall(ref):
    hour = data.find("hour").text
    temp = data.find("temp").text
    wf = data.find("wfKor").text
    print("시간="+hour, ",\t온도="+temp, ",\t예보="+tmEf)

    

