#coding :utf8
#encoding:utf8  
from __future__ import unicode_literals
import re  
import urllib2 
from bs4 import BeautifulSoup 
import smtplib  
from email.mime.text import MIMEText  
mailto_list=['shanandone@qq.com'] 
mail_host="smtp.163.com"  #设置服务器
mail_user="passions_one@163.com"    #用户名
mail_pass="yunfei1314"   #口令 
mail_postfix="163.com"  #发件箱的后缀



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

rain_str='未来三天将有雨，详情如下：'+'\n'+'   ||   '.join(wea_full_list)
	
    

def send_mail(to_list,sub,content):  
    me="rob_assist"+"<"+mail_user+"@"+mail_postfix+">"  
    msg = MIMEText(content,_subtype='plain',_charset='gb2312')  
    msg['Subject'] = sub  
    msg['From'] = me  
    msg['To'] = ";".join(to_list)  
    try:  
        server = smtplib.SMTP()  
        server.connect(mail_host)  
        server.login(mail_user,mail_pass)  
        server.sendmail(me, to_list, msg.as_string())  
        server.close()  
        return True  
    except Exception, e:  
        print str(e)  
        return False

if len(wea_list) != 0:
    if __name__ == '__main__':
        if send_mail(mailto_list,"weather",rain_str):
            print "发送成功"
        else:
            print '发送失败'



