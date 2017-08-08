#coding:utf-8
#only can work well in python2
import urllib2
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



#input url
url="http://dianying.taobao.com/showList.htm?spm=a1z21.3046609.w2.3.33Zl77&n_s=new"




response=urllib2.urlopen(url)
html_doc=response.read()
soup =BeautifulSoup(html_doc,'html.parser',from_encoding ='utf8')

# div_node=soup.find_all('div',class_="movie-card-wrap")[0]

# name=div_node.find('span',class_="bt-l").get_text().encode('utf-8')
# average=div_node.find('span',class_="bt-r").get_text().encode('utf-8')
# mv_url=div_node.find('a')['href'].encode('utf-8')
# img_url=div_node.find('div',class_="movie-card-poster").find('img')['src'].encode('utf-8')
# region=div_node.find('div',class_="movie-card-list").find_all('span')[3].get_text().encode('utf-8')
# mv_type=div_node.find_all('a')[1]['class'][0].encode('utf-8')
# data_inline=div_node.find_all('a')[1].get_text().encode('utf-8')
# print data_inline


div_nodes=soup.find_all('div',class_="movie-card-wrap")


res=[]
for div_node in div_nodes:
	try:
		
		name=div_node.find('span',class_="bt-l").get_text().encode('utf-8')
		average=div_node.find('span',class_="bt-r").get_text().encode('utf-8')
		#mv_url=div_node.find('a')['href'].encode('utf-8')
		img_url=div_node.find('div',class_="movie-card-poster").find('img')['src'].encode('utf-8')
		region=div_node.find('div',class_="movie-card-list").find_all('span')[3].get_text().encode('utf-8')
		mv_type=div_node.find_all('a')[1]['class'][0].encode('utf-8')
		data_inline=div_node.find_all('a')[1].get_text().encode('utf-8')
		showid=re.findall(r'showId=([0-9]*)',div_node.find('a')['href'])[0].encode('utf-8')

		cursor.execute('insert into taobao_mv(name,showid,average,img_url,region,mv_type,data_inline) values (%s,%s,%s,%s,%s,%s,%s)', [name,showid,average,img_url,region,mv_type,data_inline])
		conn.commit()
		
	except:
		pass


cursor.close()
conn.close()
print 'over!'