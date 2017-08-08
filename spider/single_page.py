#coding :utf8
import re  
import urllib2 
from bs4 import BeautifulSoup 


url ='http://www.tan8.com/yuepu-20883.html' 
response=urllib2.urlopen(url)
html_doc=response.read()


soup =BeautifulSoup(html_doc,'html.parser',from_encoding ='utf-8')

div_node=soup.find('div',class_="yuepu_name_0421")


res_data = {}
try:

    res_data['name'] = div_node.find('h1',class_="title_color").get_text()
    res_data['eye'] =  div_node.find('span',class_="brief_color eyes").get_text()
    res_data['likenum'] = div_node.find('span',class_="brief_color xin c-num").get_text()
    hard = div_node.find('span',class_="brief_color xin c-num")
    res_data['hardnum'] = hard.find_next_sibling('span',class_="brief_color").get_text()[3:]

    #return res_data
except:
    
    pass

