# -*- coding: utf-8 -*-

import MySQLdb

class UrlManager(object):
	
	def __init__(self):
		self.new_urls=set({})
		
		conn= MySQLdb.connect(
		        host='qdm17544119.my3w.com',
		        port = 3306,
		        user='qdm17544119',
		        passwd='yunfei1314',
		        db ='qdm17544119_db',
		        charset ='utf8'
		        )
		cursor= conn.cursor()
	
		cursor.execute("select url from song_detail")
		

		#rs =cursor.fetchmany(2)
		#print rs[1][0]
		rs = cursor.fetchall()
		for i in rs:
			#print i[0]
			self.new_urls.add(i[0])
		
		cursor.close()
		conn.close()


		


		self.old_urls = set()
	'''
	def add_new_url(self,url):
		if url is None:#新进来的url要对其做检查，是空就不管，然后还得不在new和old两个列表中才行
			return
		if url not in self.new_urls and url not in self.old_urls:
			self.new_urls.add(url)
		
	def add_new_urls(self,urls):#新来的urls不能为空
		if urls is None or len(urls) ==  0:
			return
		for url in urls:
			self.add_new_url(url)
	'''

	def has_new_url(self):#判断是否有新的urls，如果new_urls的列表长度不为0就代表有新的
		return len(self.new_urls) != 0
		
	def get_new_url(self):
		new_url = self.new_urls.pop()#从urls管理器中取出一个url
		self.old_urls.add(new_url)#取出之后，就要将其放入old urls存储空间中
		return new_url
##################################
#url方法，一般默认不需要修改
##################################
#myurl= UrlManager()
#print myurl.new_urls