#coding :utf8
import re  
import urllib2 
from bs4 import BeautifulSoup 

####这段代码无法运行，会被网站拦截
song_list=[]# init songlist of list
song = {} # init song of dict
all_urls=[] #init all_urls

# get all urls
or_url ='http://www.52jt.net/videopic-index.asp' 
response_url=urllib2.urlopen(or_url)
url_html_doc=response_url.read()
soup_url =BeautifulSoup(url_html_doc,'html.parser',from_encoding ='utf-8')

urls=soup_url.find_all('a',class_="graya12")[2:]
for i in urls:
	all_urls.append(i['href'])

# for in ---all urls get data
for url in all_urls:
	response=urllib2.urlopen(url)
	html_doc=response.read()

	soup =BeautifulSoup(html_doc,'html.parser',from_encoding ='utf-8')

	### for

	div_nodes=soup.find_all('div',id="gtp_detail")

	for div_node in div_nodes[1:]:
		song['date'] =div_node.find_all('span')[0].get_text().encode('utf-8')
		song['name'] =div_node.find_all('span')[1].get_text().encode('utf-8')
		song['href'] =div_node.find_all('span')[1].find('a')['href']
		song['singer'] =div_node.find_all('span')[2].get_text().encode('utf-8')
		song['click'] =div_node.find_all('span')[3].get_text().encode('utf-8')
		song_list.append(song)



print song_list


