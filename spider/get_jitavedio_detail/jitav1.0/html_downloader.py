# -*- coding: utf-8 -*-
import urllib

class HtmlDownloader(object):
	
	def download(self,url):
		if url is None:
			return None
		response = urllib.urlopen(url)
		
		if response.getcode()!=200 :
			return None
			  
		return response.read()
##################################
#下载网页，默认不需要修改
##################################