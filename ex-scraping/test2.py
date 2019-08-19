html = '''
<html> 
    <head> 
    </head> 
    <body> 
        <h1> 시장  
            <p id='fruits1' class='name' title='바나나'> 바나나 
                <span class = 'price'> 3000원 </span> 
                <span class = 'inventory'> 500개 </span> 
                <span class = 'store'> 가가가 </span> 
                <a href = 'http://test1'> url1 </a> 
            </p> 

            <p id='fruits2' class='name' title='귤'> 귤 
                <span class = 'price'> 2000원 </span> 
                <span class = 'inventory'> 100개 </span> 
                <span class = 'store'> 나나나</span> 
                <a href = 'http://test2'> url2 </a> 
            </p> 
            <p id='fruits3' class='name' title='파인애플'> 파인애플 
                <span class = 'price'> 5000원 </span> 
                <span class = 'inventory'> 10개 </span> 
                <span class = 'store'> 가가가</span> 
                <a href = 'http://test1'> url1 </a> 
            </p> 
        </h1> 
    </body> 
</html>
'''

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
soup.select('p')
soup.select('.price')
soup.select('span.price')
soup.select('#fruits2')
soup.select('p > span')
soup.select('p span')
soup.select('p.name > span.price')
soup.select('h1 .name > span.store')
soup.select("a[href='http://test1']")
soup.select('p > span.price')[0].text
prices = soup.select('p > span.price')
for price in prices:       
    print(price.text)
soup.select('a')[0]['href']

