import urllib
from bs4 import BeautifulSoup
import html5lib
response = urllib.urlopen('http://php.net/')
html = response.read()
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip=True)
tokens = [t for t in text.split()] 
print (tokens)