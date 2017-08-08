#coding :utf8
import re  
import urllib2 
from bs4 import BeautifulSoup 


url ='http://www.52jt.net/videopic-index.asp' 
response=urllib2.urlopen(url)
html_doc=response.read()

soup =BeautifulSoup(html_doc,'html.parser',from_encoding ='utf-8')

urls=soup.find_all('a',class_="graya12")[2:]

all_urls=[]

for i in urls:
	all_urls.append(i['href'])
print len(all_urls)

