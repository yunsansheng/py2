#coding:utf-8
#only can work well in python2
import urllib2
import urllib
from bs4 import BeautifulSoup 
import re
import time  

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

# ��Ҫ�������������ڣ�����cinemaid,����showid
# http://dianying.taobao.com/showDetailSchedule.htm?n_s=new&showId=158865&date=2016-12-14&cinemaId=31018
data={}  #����post����
url="http://dianying.taobao.com/showDetailSchedule.htm?n_s=new"

cinemaids=[] #��ӰԺ����
showids=[]#��Ӱ����

# =========����������ȡ��Ҫ�ĵ�ӰԺ===========
# cursor.execute("select cinemaid from cinema_all where  region_en in ('binhu','xinqu')")
cursor.execute("select cinemaid from cinema_all ")
rs_cin = cursor.fetchall()
for cin in rs_cin:
	# print cin[0]
	cinemaids.append(cin[0])
# =========����������ȡ��Ҫ�ĵ�Ӱ===========
cursor.execute("select showid from taobao_mv where  average >=8.8 ")
rs_show = cursor.fetchall()
for show in rs_show:
	# print cin[0]
	showids.append(show[0])
# =========������������===========
data['date']=u'2016-12-14'

print cinemaids
print showids

# # �����Ȱ������ڣ��ٰ��յ�Ӱ���ٰ���ӰԺ��
for item in cinemaids:
	data['cinemaId']=item

	
	for show_item in showids:
                time.sleep(1)
		data['showId']=show_item
		post_data=urllib.urlencode(data)
		response=urllib.urlopen(url,post_data)
		html_doc=response.read()
		soup =BeautifulSoup(html_doc,'html.parser',from_encoding ='utf8')
		try:
			trs=soup.find('tbody').find_all('tr')
		except:
			pass

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