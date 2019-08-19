from konlpy.corpus import kolaw
from konlpy.tag import Okt

text = kolaw.open('constitution.txt').read()
print(text[:500])
print()

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
            
# 많이 사용된 명사 출력하기 
keys = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
for word, count in keys[:50]:
    print("{0}({1}) ".format(word, count), end="")
print()
