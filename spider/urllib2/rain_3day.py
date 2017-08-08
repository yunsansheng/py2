

#coding :utf8
#encoding:utf8  
from __future__ import unicode_literals
import re  
import urllib2 
from bs4 import BeautifulSoup 

###未来三天有雨的提醒
url ='http://www.weather.com.cn/weather/101190201.shtml#7d' 
response=urllib2.urlopen(url)
html_doc=response.read()


soup =BeautifulSoup(html_doc,'html.parser',from_encoding ='utf8')

weather=soup.find_all('p',class_='wea')[0:3]

wea_list=[]

for i in weather:
    wea_str= i.get_text().encode('utf8')
    resl =re.search(u'雨'.encode('utf8'), wea_str).group()
    if resl is not None:
        #print i.get_text()
        wea_list.append(i.get_text())

if len(wea_list) != 0:
    print '三天内有雨，详情如下：'
    for i in weather:
        print i.get_text()
    

'''  
message = u'天人合一'.encode('utf8')
print(re.search(u'人'.encode('utf8'), message).group())
'''
