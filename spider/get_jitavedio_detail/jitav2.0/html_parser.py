# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import urlparse

class HtmlParser(object):
	
	def _get_new_urls(self,page_url,soup):
		new_urls = set()
		#links = soup.find_all('a',href =re.compile(r"/view/\d+\.htm"))
		links = soup.find_all('a',class_="graya12",href=re.compile(r"http://www.52jt.net/videosinger_\d+.html"))[2:]

		for link in links:
			new_url = link['href']
			new_urls.add(new_url)
		return new_urls
		
	def _get_new_data(self,page_url,soup):
                '''
		song = {}
		div_nodes=soup.find_all('div',id="gtp_detail")
		song['date']='this is date'
		song['name']='this is name'
		song['href']='this is href'
		song['singer']='this is singer'
		song['click']='this is click'
		


		return song 

		'''
                song_list=[]
                try:
                        
                        div_nodes=soup.find_all('div',id="gtp_detail")
                        for div_node in div_nodes[1:]:
                                song={}
                                song['date'] =div_node.find_all('span')[0].get_text().encode('utf-8')
                                song['name'] =div_node.find_all('span')[1].get_text().encode('utf-8')
                                song['href'] =div_node.find_all('span')[1].find('a')['href']
                                song['singer'] =div_node.find_all('span')[2].get_text().encode('utf-8')
                                song['click'] =div_node.find_all('span')[3].get_text().encode('utf-8')
                                song_list.append(song)
			return song_list
		except:
                        pass
                        
              


                
		'''
		res_data = {}
		

		res_data['url'] = page_url
		#<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
		title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")
		res_data['title'] = title_node.get_text()
		
		#<div class="lemma-summary" label-module="lemmaSummary">
		summary_node =soup.find('div',class_="lemma-summary")
		res_data['summary'] = summary_node.get_text()
		


		return res_data

		'''

	
	def parse(self,page_url,html_cont):
		if page_url is None or html_cont is None:
			return

		soup = BeautifulSoup(html_cont,'html.parser',from_encoding = 'utf-8')

		new_urls  = self._get_new_urls(page_url,soup)
		new_data = self._get_new_data(page_url,soup)
		return new_urls,new_data
