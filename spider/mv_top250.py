#coding:utf-8
import MySQLdb
import urllib2

import json

import string

html = r'https://api.douban.com/v2/movie/top250?start={page}'

#html = urllib2.urlopen(r'https://api.douban.com/v2/movie/top250?start=1')


conn= MySQLdb.connect(
                host='localhost',
                port =3306,
                user='root',
                passwd='123',
                db ='test',
                charset ='utf8'
                )

cursor= conn.cursor()

print 'begin...'
p = 1
while p <=13:   
    try:
        hjson = json.loads(urllib2.urlopen(html.format(page=(p-1)*20)).read())
        # list数据集中提取数据
        for key in hjson['subjects']:
            mvid=int(key['id'].encode('utf-8'))
            title=key['title'].encode('utf-8')
            year=int(key['year'])
            average=key['rating']['average']
            collect =int(key['collect_count'])
            genres=','.join(key['genres']).encode('utf-8')  #lst 会有多个  影片类型
           
            cursor.execute('insert into mv_top250(mvid, title,year,average,collect,genres) values (%s,%s,%s,%s,%s,%s)', [mvid, title,year,average,collect,genres])    
            
            conn.commit()



    except Exception as e:
        print e
    
    # for key in hjson['subjects']:
    #     print i,':',key['title'],'--',key['original_title'],'(',key['year'],')'
    #     i+=1
    
        
    p+=1
    print p

cursor.close()
conn.close()
print 'over!'
