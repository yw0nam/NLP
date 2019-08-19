import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Okt

fp = codecs.open("2BEXXX01.txt", "r", encoding="utf-16")
soup = BeautifulSoup(fp, "html.parser")
body = soup.select_one("text > body")
text = body.getText()

# 텍스트를 한 줄씩 처리하기 
twitter = Okt()
word_dic = {}

lines = text.split("\r\n")
for line in lines:
    malist = twitter.pos(line)
    for taeso, pumsa in malist:
        if pumsa == "Noun": #  명사 확인 
            if not (taeso in word_dic):
                word_dic[taeso] = 0
            word_dic[taeso] += 1
            
# 많이 사용된 명사 50개 출력
keys = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
for word, count in keys[:50]:
    print("{0}({1}) ".format(word, count), end="")
print()
