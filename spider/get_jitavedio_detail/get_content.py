#coding :utf8
import re  
import urllib2 
from bs4 import BeautifulSoup 


url ='http://www.52jt.net/videosinger_253.html' 
response=urllib2.urlopen(url)
html_doc=response.read()

soup =BeautifulSoup(html_doc,'html.parser',from_encoding ='utf-8')

###get one 
'''
song = {}
div_node=soup.find('div',id="gtp_detail").find_all("span")
song['date'] =div_node[0].get_text()
song['website'] =div_node[1].get_text()
song['singer'] =div_node[2].get_text()
song['click'] =div_node[3].get_text()
print song
'''

###get more
'''
song = {}
div_nodes=soup.find_all('div',id="gtp_detail")
div_node=div_nodes[1].find_all('span')

song['date'] =div_node[0].get_text().encode('utf-8')
song['name'] =div_node[1].get_text().encode('utf-8')
song['href'] =div_node[1].find('a')['href']
song['singer'] =div_node[2].get_text().encode('utf-8')
song['click'] =div_node[3].get_text().encode('utf-8')

print song['date']
print song['name']
print song['href']
print song['singer'] 
print song['click']
'''
### for
song_list=[]
song = {}
div_nodes=soup.find_all('div',id="gtp_detail")

for div_node in div_nodes[1:]:
	song['date'] =div_node.find_all('span')[0].get_text().encode('utf-8')
	song['name'] =div_node.find_all('span')[1].get_text().encode('utf-8')
	song['href'] =div_node.find_all('span')[1].find('a')['href']
	song['singer'] =div_node.find_all('span')[2].get_text().encode('utf-8')
	song['click'] =div_node.find_all('span')[3].get_text().encode('utf-8')
	song_list.append(song)

print song_list 



