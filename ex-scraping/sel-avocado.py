from bs4 import BeautifulSoup
fp = open("fruits-vegetables.html", encoding="cp949")
soup = BeautifulSoup(fp, "html.parser")

sel = lambda q : print(soup.select_one(q).string)
sel2 = lambda q2 : print(soup.select(q2)[1].string)

# 한 개의 list에만 적용 가능. list 범위 초과.
# run-time error 발생.
#sel("li:nth-of-type(8)")

sel("#ve-list > li:nth-of-type(4)")
sel2("#ve-list > li[data-lo='us']")
sel2("#ve-list > li.black")

#print(soup.select("#ve-list > li[data-lo='us']")[1].string)  
#print(soup.select("#ve-list > li.black")[1].string)

cond = {"data-lo":"us", "class":"black"}
print(soup.find("li",cond).string)

print(soup.find(id="ve-list")
          .find("li",cond).string)
