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


# 获取所有影城
all_region=[u'北塘区',u'滨湖区',u'崇安区',u'惠山区',u'江阴市',u'南长区',u'新区',u'锡山区',u'宜兴市']
select_region=[u'滨湖区',u'崇安区',u'南长区',u'新区']
#http://dianying.taobao.com/showDetailSchedule.htm?showId=158865&regionName=滨湖区&n_s=new
#"http://dianying.taobao.com/showDetailSchedule.htm?&regionName"
url="http://dianying.taobao.com/showDetailSchedule.htm?"
data={}
for i in all_region:
	data['regionName']=i
	post_data=urllib.urlencode(data)
	response=urllib.urlopen(url,post_data)
	html_doc=response.read()
	soup =BeautifulSoup(html_doc,'html.parser',from_encoding ='utf8')
	a_node=soup.find_all('div',class_='select-tags')[1].find_all('a')

	for node in a_node:
		try:
			node_id=node['data-param']
			cinemaid= re.findall(r'cinemaId=([0-9]*)',node_id)[0].encode('utf-8')		
			cinema= node.get_text().encode('utf-8')
			region=data['regionName'].encode('utf-8')

			cursor.execute('insert into cinema_all(cinemaid,cinema,region) values (%s,%s,%s)', [cinemaid,cinema,region])
			conn.commit()

		except:
			pass



cursor.close()
conn.close()
print 'over!'