# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import urlparse

class HtmlParser(object):
        

        
        def _get_new_data(self,page_url,soup):
        	div_node=soup.find('div',class_="yuepu_name_0421")
        	res_data = {}
        	try:

        	    res_data['name'] = div_node.find('h1',class_="title_color").get_text()
        	    res_data['eye'] =  div_node.find('span',class_="brief_color eyes").get_text()
        	    res_data['likenum'] = div_node.find('span',class_="brief_color xin c-num").get_text()
        	    hard = div_node.find('span',class_="brief_color xin c-num")
        	    res_data['hardnum'] = hard.find_next_sibling('span',class_="brief_color").get_text()[3:]

        	    return res_data
        	except:
        	    
        	    pass




        
        def parse(self,page_url,html_cont):
                #if page_url is None or html_cont is None:
                        #return

                soup = BeautifulSoup(html_cont,'html.parser',from_encoding = 'utf-8')

                
                new_data = self._get_new_data(page_url,soup)
                return new_data
