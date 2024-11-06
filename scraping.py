import requests
import bs4
import lxml

res=requests.get('https://en.wikipedia.org/wiki/Art')
soup=bs4.BeautifulSoup(res.text,'lxml')
print(soup)
selector=soup.select('.title')