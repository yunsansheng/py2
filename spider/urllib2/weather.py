
#获取天气网上，h1带天字的数据。
#coding :utf8
from __future__ import unicode_literals   #重要，没有这句运行出错
import re  
import urllib2 
from bs4 import BeautifulSoup 


url ='http://www.weather.com.cn/weather/101190201.shtml#7d' 
response=urllib2.urlopen(url)
html_doc=response.read()


soup =BeautifulSoup(html_doc,'html.parser',from_encoding ='utf-8')

weather=soup.find_all('h1',string=re.compile(u'\u5929'))
for i in weather:
	print i.name,i.get_text()
	
