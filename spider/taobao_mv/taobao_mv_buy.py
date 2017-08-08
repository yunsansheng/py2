#coding:utf-8
#only can work well in python2
import urllib2
import urllib
from bs4 import BeautifulSoup 
import re  

import MySQLdb

conn= MySQLdb.connect(
                host='localhost',
                port =3306,
                user='root',
                passwd='123',
                db ='test',
                charset ='utf8'
                )
cursor= conn.cursor()

# 需要三个参数，日期，还有cinemaid,还有showid
# http://dianying.taobao.com/showDetailSchedule.htm?n_s=new&showId=158865&date=2016-12-14&cinemaId=31018
data={}
data['showId']=158865  #血战钢锯岭
data['cinemaId']=17307  #无锡海岸影城
data['date']=u'2016-12-13'
url="http://dianying.taobao.com/showDetailSchedule.htm?n_s=new"
post_data=urllib.urlencode(data)
response=urllib.urlopen(url,post_data)
html_doc=response.read()
soup =BeautifulSoup(html_doc,'html.parser',from_encoding ='utf8')


# tr=soup.find('tbody').find_all('tr')[0]

# halltime=tr.find('td',class_='hall-time').find('em').get_text().strip().encode('utf-8')
# halltype=tr.find('td',class_='hall-type').get_text().strip().encode('utf-8')
# hallprice=tr.find('td',class_='hall-price').find('em',class_='now').get_text().strip().encode('utf-8')
# print halltime

trs=soup.find('tbody').find_all('tr')



for tr in trs:
	try:
		showid=data['showId']
		cinemaid=data['cinemaId']
		date=data['date']

		halltime=tr.find('td',class_='hall-time').find('em').get_text().strip().encode('utf-8')
		halltype=tr.find('td',class_='hall-type').get_text().strip().encode('utf-8')
		hallname=tr.find('td',class_='hall-name').get_text().strip().encode('utf-8')
		hallprice=tr.find('td',class_='hall-price').find('em',class_='now').get_text().strip().encode('utf-8')

		cursor.execute('insert into movie_price(showid,cinemaid,date,halltime,halltype,hallname,hallprice) values (%s,%s,%s,%s,%s,%s,%s)', [showid,cinemaid,date,halltime,halltype,hallname,hallprice])
		conn.commit()
	except:
		pass





cursor.close()
conn.close()
print 'over!'