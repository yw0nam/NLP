import urllib.request

url = "http://www.python.org/"

#f = urllib.request.urlopen(url)
#print(f.read(300)

with urllib.request.urlopen(url) as f:	
    print(f.read(300))
