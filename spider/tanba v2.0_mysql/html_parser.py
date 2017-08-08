# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import urlparse

class HtmlParser(object):
        
        def _get_new_urls(self,page_url,soup):
                new_urls = set()
                #links = soup.find_all('a',href =re.compile(r"/view/\d+\.htm"))
                links = soup.find_all('a',href=re.compile(r"tan8.com/album-\d+.html"))
                for link in links:
                        new_url = link['href']
                        new_urls.add(new_url)
                return new_urls
        
        def _get_new_data(self,page_url,soup):
                song_list=[]
                try:
                        #song={}take this will all be same shold be in for in
                        singer_name=soup.find('h1',class_='title_color').get_text().encode('utf-8').strip()
                        li_nodes=soup.find('ul',class_="zj_list_0422").find_all('li')
                        for li in li_nodes:
                                song={}
                                song['singer_name'] =singer_name.decode('utf-8')[3:].encode('utf-8')
                                song['name'] =li.find('div',class_='text').find('h3').find('i').next_sibling.encode('utf-8')
                                song['author'] =li.find('div',class_='text').find('p').find('span').get_text().encode('utf-8')
                                song['clicknum'] =li.find('div',class_='text').find('p').find('span',class_='sanjiao').get_text().encode('utf-8')
                                song['like'] =li.find('div',class_='text').find('p').find('span',class_='xin').get_text().encode('utf-8')
                                song['url']= 'http://www.tan8.com/'+li.parent['href']
                                song_list.append(song)
                        return song_list
                
                except:
                        pass
                



        
        def parse(self,page_url,html_cont):
                if page_url is None or html_cont is None:
                        return

                soup = BeautifulSoup(html_cont,'html.parser',from_encoding = 'utf-8')

                new_urls  = self._get_new_urls(page_url,soup)
                new_data = self._get_new_data(page_url,soup)
                return new_urls,new_data
