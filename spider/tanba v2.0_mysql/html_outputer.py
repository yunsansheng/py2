# -*- coding: utf-8 -*-



import chardet
import MySQLdb




class HtmlOutputer(object):
        
        def __init__(self):
                self.datas = [ ]
                        
        def collect_data(self,data):
                if data is None:
                        return None
                
                self.datas=self.datas + data
                
        def output_html(self):
                fout = open('output.html','w')
                
                fout.write("<html>")
                fout.write("<meta charset='utf-8'>")
                fout.write("<body>")
                fout.write("<table>")
                
                #ascii
                for data in self.datas:

                        fout.write("<tr>")
                        fout.write("<td>%s</td>" % data['singer_name'])
                        fout.write("<td>\t</td>" )
                        fout.write("<td>%s</td>" % data['name'])
                        fout.write("<td>\t</td>" )
                        fout.write("<td>%s</td>" % data['author'])
                        fout.write("<td>\t</td>" )
                        fout.write("<td>%s</td>" % data['clicknum'])
                        fout.write("<td>\t</td>" )
                        fout.write("<td>%s</td>" % data['like'])
                        fout.write("<td>\t</td>" )
                        fout.write("<td>%s</td>" % data['url'])
                        fout.write("</tr>")


                fout.write("</table>")
                fout.write("</body>")
                fout.write("</html>")
                fout.close()
        def output_mysql(self):
                conn= MySQLdb.connect(
                        host='',
                        port = ,
                        user='',
                        passwd='',
                        db ='',
                        charset ='utf8'
                        )
                cursor= conn.cursor()

                for data in self.datas:
                        
                        #print chardet.detect(data['singer_name'])
                        #print data['singer_name']
                        #print data['singer_name'].decode('gbk').encode('utf-8')
                
                        cursor.execute("insert into song_detail (singer_name,name,author,clicknum,likenum,url) values (%s,%s,%s,%s,%s,%s)",(data['singer_name'],data['name'],data['author'],data['clicknum'],data['like'],data['url']))
                        conn.commit()

                
                cursor.close()
                conn.close()


