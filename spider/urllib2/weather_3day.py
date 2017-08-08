#coding :utf8
#encoding: utf8  
from __future__ import unicode_literals
import re  
import urllib2 
from bs4 import BeautifulSoup 


url ='http://www.weather.com.cn/weather/101190201.shtml#7d' 
response=urllib2.urlopen(url)
html_doc=response.read()


soup =BeautifulSoup(html_doc,'html.parser',from_encoding ='utf8')

weather=soup.find_all('p',class_='wea')[0:3]
print('======今明后天气情况：======')
for i in weather:
        print (i.get_text())

script=soup.find_all('script')
hour_wea_str=script[6].get_text()[15:]#get weather data string 
hour_wea =eval(hour_wea_str)['1d'] #transfer to dict and get value data
print('====未来数小时天气情况：====')

list_num =len(hour_wea)

for i in range(list_num):
       print ( hour_wea[i].split(',')[0]+','+hour_wea[i].split(',')[2])

'''
hour_wea1 =eval(hour_wea_str)['1d'][0]
hour_sp1=hour_wea1.split(',')  # to a list
print hour_sp1[0]+','+hour_sp1[2]
'''
#输出结果
'''
======今明后天气情况：======
中雨转大雨
大雨转中雨
阵雨转阴
====未来数小时天气情况：====
15日08时,中雨
15日11时,中雨
15日14时,中雨
15日17时,中雨
15日20时,中雨
15日23时,大雨
16日02时,中雨
16日05时,中雨
16日08时,大雨
'''

