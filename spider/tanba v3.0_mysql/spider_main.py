# -*- coding: utf-8 -*-
import url_manager,html_downloader,html_parser,html_outputer


class SpiderMain(object):
	
	#构造函数，初始化各类管理器，解析器，下载器等
	def __init__(self):
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()
	
	def craw(self,root_url):
		#将入口url添加进url管理器，url管理器中有一个待爬取的url,就可以启动循环了
		count = 1 #用于计数，计算当前爬取的是第几个url
		#self.urls.add_new_url(root_url)
		while self.urls.has_new_url():
			try:#加入异常处理，有的网页打开没有数据

				new_url = self.urls.get_new_url()#从url管理器获取一个url
				
			
				print 'crawl %d: %s' % (count,new_url)
				html_cont  = self.downloader.download(new_url)#获取完url，就要去下载它
				
				new_data = self.parser.parse(new_url,html_cont)#下载url，就会得到新的url列表，和新的数据，那么我们就要去处理它
				print new_url
				#print new_data
				#self.urls.add_new_urls(new_urls)#将新的urls 添加到url管理器中
				self.outputer.collect_data(new_data)


				if count ==20:
					break
				#将新的数据收集起来		
				count = count +1
				
			except:
				print 'craw_fail'

		self.outputer.output_html()
		

if __name__ == "__main__":

	root_url = "http://www.tan8.com/yuepu-20883.html"
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)






####爬虫架构
'''
spider_main.py：爬虫主程序
        html_downloader.py：网页下载器
        html_outputer.py：内容输出器
        html_parser.py：网页内容解析器
        url_manager.py：url管理器
'''
