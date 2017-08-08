# -*- coding: utf-8 -*-



class UrlManager(object):
	
	def __init__(self):
		self.new_urls = set()#用set()方法作为存储单元，可以自动去重
		self.old_urls = set()
	
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

	def has_new_url(self):#判断是否有新的urls，如果new_urls的列表长度不为0就代表有新的
		return len(self.new_urls) != 0
		
	def get_new_url(self):
		new_url = self.new_urls.pop()#从urls管理器中取出一个url
		self.old_urls.add(new_url)#取出之后，就要将其放入old urls存储空间中
		return new_url
