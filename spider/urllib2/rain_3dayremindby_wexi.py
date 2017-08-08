#!/usr/bin/python
# coding: utf-8
# encoding: utf-8
#from __future__ import unicode_literals  #此文档加了会出错
import urllib,urllib2
import json
import sys
import re
from bs4 import BeautifulSoup 
reload(sys)
sys.setdefaultencoding('utf-8')



url ='http://www.weather.com.cn/weather/101190201.shtml#7d' 
response=urllib2.urlopen(url)
html_doc=response.read()

soup =BeautifulSoup(html_doc,'html.parser',from_encoding ='utf8')
weather=soup.find_all('p',class_='wea')[0:3]

wea_list=[]
wea_full_list=[]

for i in weather:
    wea_str= i.get_text().encode('utf8')
    resl =re.search(u'雨'.encode('utf8'), wea_str).group()
    wea_full_list.append(i.get_text())
    if resl is not None:
        #print i.get_text()
        wea_list.append(i.get_text())

#rain_str=(u'未来三天将有雨，详情如下：'+'\n'+'\n'.join(wea_full_list))
rain_str=(u'未来三天将有雨，详情如下：'+'\n'
          +'今天： '+wea_full_list[0]+'\n'
          +'明天： '+wea_full_list[1]+'\n'
          +'后天： '+wea_full_list[2])

def gettoken(corpid,corpsecret):
    gettoken_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corpid + '&corpsecret=' + corpsecret
    try:
        token_file = urllib2.urlopen(gettoken_url)
    except urllib2.HTTPError as e:
        print e.code
        print e.read().decode("utf8")
        sys.exit()
    token_data = token_file.read().decode('utf-8')
    token_json = json.loads(token_data)
    token_json.keys()
    token = token_json['access_token']
    return token
 
def senddata(access_token,user,content):
    send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + access_token
    send_values = {
        "touser":user,   
        "toparty":"1",    # departmentid
        "msgtype":"text",  
        "agentid":"2", #applycation id
        "text":{
            "content":content
           },
        "safe":"0"
        }
    send_data = json.dumps(send_values, ensure_ascii=False)
    send_request = urllib2.Request(send_url, send_data)
    response = json.loads(urllib2.urlopen(send_request).read())
    print str(response)
 
if __name__ == '__main__':
    user = 'sandy' #str(sys.argv[1])  
    content =  str(rain_str) #str(sys.argv[2])  #不加str这边就出错
    corpid = 'wx812ae8d875711da7'   
    corpsecret = 'sayc0NWKZ8p-sFIasvL0oTJbQipW9habOR5nMXvbBiQBdxBeqtavrG3va58ts33J' 
    accesstoken = gettoken(corpid,corpsecret)
    senddata(accesstoken,user,content)
