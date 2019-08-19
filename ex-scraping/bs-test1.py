from bs4 import BeautifulSoup

html = """
<html><body>
  <h1>스크레이핑이란?</h1>
  <p>웹 페이지를 분석하는 것</p>
  <p>원하는 부분을 추출하는 것</p>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')   # 파서 종류 지정

h1 = soup.html.body.h1
p1 = soup.html.body.p

# 첫 번째 next_sibling은 </p> 뒤 줄바꿈 문자
# 두 번째 next_sibling은 2번째 <p> 태그
p2 = p1.next_sibling
p22 = p1.next_sibling.next_sibling

print("h1 = " + h1.string)
print("p1 = " + p1.string)
print("p2 = " + p2.string)
print("p22 = " + p22.string)
