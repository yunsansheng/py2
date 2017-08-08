from urllib import request
from bs4 import BeautifulSoup 
import re  
import json
from datetime import datetime, timedelta


req = request.Request("http://note.youdao.com/yws/api/group/24762761/message?channel=all&cstk=ff2uX5II&keyfrom=web&length=30&method=list&orgId=0" )
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
req.add_header('Accept','application/json, text/plain, */*')
req.add_header('Referer','http://note.youdao.com/group/')
req.add_header('Cookie','OUTFOX_SEARCH_USER_ID_NCOO=211754636.31522006; YOUDAO_EAD_UUID=b75d468c-8d80-4693-98a7-9a775da60da0; OUTFOX_SEARCH_USER_ID=-1451180433@61.160.96.234; __yadk_uid=QyqZUxm7NcDwbtQXxsRwBR9Xnfbf0hPl; P_INFO=passions_one@163.com|1479176927|0|other|00&99|jis&1479090077&other#jis&320200#10#0#0|&0||passions_one@163.com; YNOTE_PERS=v2|urstoken||YNOTE||web||-1||1479352338633||61.160.96.234||passions_one@163.com||gBOLPB64g40lEOLU5nfk5RYm0Mpy6Lkf0gFRHOf0MkEROE0LJ4RLkA0UM6MJLOfPyRUGnfTB6M6S06LnMUm6MwK0; _ga=GA1.2.654069098.1465884659; Hm_lvt_4566b2fb63e326de8f2b8ceb1ec367f2=1478756833,1479351855,1479352249,1479352411; Hm_lvt_30b679eb2c90c60ff8679ce4ca562fcc=1478756825,1479351818,1479352238,1479352408; connect.sid=s"%"3AEPOvkAK7nbn8gGAVV6fu2IP7t9nUdxle.ErF"%"2BQDRyWF98sWG"%"2FvYNw59XTyQYYfLOTf1u9QwtQpG4; YNOTE_SESS=v2|Y3EMRfLDjBwFkfzm6LzW0zfh4UfRHpF0wLOfOERLq40JLRHQ4OfTFRYMnH6uPMqB0QL0fUAO4kGRwK0LeF0LYWRYGnfqB0fgL0; YNOTE_LOGIN=5||1479361832101; JSESSIONID=aaapIZ7XD8Lktb7u39SHv; YNOTE_CSTK=ff2uX5II')

response=request.urlopen(req) 
html_doc=response.read()
soup =BeautifulSoup(html_doc,'html.parser',from_encoding ='utf-8')

json_str=str(soup)
lst= json.loads(json_str)

user =['Bert Shen','Blithe Shen','Harry Ding','Sunny Xiang','Tymon Tan','Tracy Tan','Vicky Liu']
user_set =set(user)
user_dict={'pollux1314@163.com':'Bert Shen',
        'qqD83C27F3AC417C1ADFA2558418A2A209':'Blithe Shen',
      'qq0A340FFEFF34ADF4A365FA2778D57BBF':'Harry Ding',
      'qqEBAD0546602714E72A6FD1278ACA0245':'Sunny Xiang',
      'qq9A96C7B6ECBA0BD3AFF590FF1D8EDF39':'Tymon Tan',
      'qqC75D0AB53AD2FFA9BFF64D2A810D1CD1':'Tracy Tan',
      'qq765F7FCCB7C66911C8509F3905D66513':'Vicky Liu'
}


#******每次运行需要修改日期
# dt = datetime(2016, 11, 17, 00, 00)  
# dt_end= datetime(2016, 11, 17, 23, 59)

#获取取昨天
#time=datetime.now()#当天
#time=datetime.now()- timedelta(days=3)#上周五
time=datetime.now() - timedelta(days=1)#昨天

day = time.day 
month=time.month
year=time.year

dt = datetime(year, month, day, 00, 00)
dt_end= datetime(year, month, day, 23, 59)



data=set()
for i in lst:
    if (i['type']==4):
        # fileName=i['fileName']
        userId=i['user']['userId']
        name=i['user']['name']
        time=datetime.fromtimestamp(round(i['time']/1000))
        # time=str(datetime.fromtimestamp(round(i['time']/1000)))
        if(time>=dt and time<=dt_end):
            data.add(userId)


re_y=set()#维护的人员
re_n=set()#未维护的人员
for l in data:
    try:
        re_y.add(user_dict[str(l)])
    except:
        pass


re_n= user_set.difference(re_y)

print(re_n)

# 需要文档名称，维护人员和维护的日期
# lst[0]['fileName'] '第4季度_Esquel_SRF_信息总览.xlsx'
# lst[0]['user']['userId']
# lst[0]['user']['name']
# lst[0]['user']['time']
# lst[0]['version']




# curl "http://note.youdao.com/yws/api/group/24762761/message?channel=all&cstk=ff2uX5II&keyfrom=web&length=21&method=list&orgId=0" 
# -H "Accept-Encoding: gzip, deflate, sdch" 
# -H "Accept-Language: zh-CN,zh;q=0.8,en;q=0.6" 
# -H "User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
#  -H "Accept: application/json, text/plain, */*" 
#  -H "Referer: http://note.youdao.com/group/" 
#  -H "Cookie: OUTFOX_SEARCH_USER_ID_NCOO=211754636.31522006; YOUDAO_EAD_UUID=b75d468c-8d80-4693-98a7-9a775da60da0; OUTFOX_SEARCH_USER_ID=-1451180433@61.160.96.234; __yadk_uid=QyqZUxm7NcDwbtQXxsRwBR9Xnfbf0hPl; P_INFO=passions_one@163.com|1479176927|0|other|00&99|jis&1479090077&other#jis&320200#10#0#0|&0||passions_one@163.com; YNOTE_PERS=v2|urstoken||YNOTE||web||-1||1479352338633||61.160.96.234||passions_one@163.com||gBOLPB64g40lEOLU5nfk5RYm0Mpy6Lkf0gFRHOf0MkEROE0LJ4RLkA0UM6MJLOfPyRUGnfTB6M6S06LnMUm6MwK0; _ga=GA1.2.654069098.1465884659; Hm_lvt_4566b2fb63e326de8f2b8ceb1ec367f2=1478756833,1479351855,1479352249,1479352411; Hm_lvt_30b679eb2c90c60ff8679ce4ca562fcc=1478756825,1479351818,1479352238,1479352408; connect.sid=s"%"3AEPOvkAK7nbn8gGAVV6fu2IP7t9nUdxle.ErF"%"2BQDRyWF98sWG"%"2FvYNw59XTyQYYfLOTf1u9QwtQpG4; YNOTE_SESS=v2|Y3EMRfLDjBwFkfzm6LzW0zfh4UfRHpF0wLOfOERLq40JLRHQ4OfTFRYMnH6uPMqB0QL0fUAO4kGRwK0LeF0LYWRYGnfqB0fgL0; YNOTE_LOGIN=5||1479361832101; JSESSIONID=aaapIZ7XD8Lktb7u39SHv; YNOTE_CSTK=ff2uX5II" 
#  -H "Proxy-Connection: keep-alive"
# --compressed


