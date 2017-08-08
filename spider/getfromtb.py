#coding:utf-8
import MySQLdb
data={
#此处放入json
}

#####上面的是data数据
'''
1.主订单号
print  data["mainOrders"][0]["extra"]["id"]     #[0]代表第一条记录
或者
print  data["mainOrders"][0]["id"]
2.订单时间
print  data["mainOrders"][0]["orderInfo"]["createTime"]  #[0]代表第一条记录    (这个地方也有id)
3.付款
print  data["mainOrders"][0]["payInfo"]["actualFee"]
4.卖家
print  data["mainOrders"][0]["seller"]["shopName"]

5.商品
print  data["mainOrders"][0]["id"]
print  data["mainOrders"][0]["subOrders"][0]["itemInfo"]["title"]  #后面的 0 1 2代表的是商品

data["mainOrders"][4]["subOrders"]  这个是一个list
print  len(data["mainOrders"][4]["subOrders"]) 获取商品的长度
'''

itemdetail =data["mainOrders"]

getdata=[]
for main in itemdetail:
    try:
        onedata={}
        onedata['id']=main["id"]
        onedata['createTime']=main["orderInfo"]["createTime"]
        onedata['actualFee']=main["payInfo"]["actualFee"]
        onedata['shopName']=main["seller"]["shopName"]
        onedata['od_num']=len(main["subOrders"])
        textall=[]
        for i in main["subOrders"]:
            try:
                textall.append(i["itemInfo"]["title"])
            except:
                pass

        onedata['orders']="#||#".join(textall)
        getdata.append(onedata)
    except:
        pass



# print getdata[4]['od_num']

#将结果存入mysql

conn= MySQLdb.connect(
                        host='',
                        port = ,
                        user='',
                        passwd='',
                        db ='',
                        charset ='utf8'
                        )


cursor= conn.cursor()


try:
    for data in getdata:
        cursor.execute("insert into shop_in_taobao (id,createTime,actualFee,shopName,od_num,orders) values (%s,%s,%s,%s,%s,%s)",(data['id'],data['createTime'],data['actualFee'],data['shopName'],data['od_num'],data['orders']))
        conn.commit()
except Exception as e:
    print e
    
                               

cursor.close()
conn.close()
