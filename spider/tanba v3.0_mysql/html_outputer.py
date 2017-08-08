# -*- coding: utf-8 -*-



import chardet
import MySQLdb




class HtmlOutputer(object):
        
        def __init__(self):
                self.datas = [ ]
                        
        def collect_data(self,data):
                if data is None:
                        return None
                print data['name']
                self.datas.append(data)
                #self.datas=self.datas + data
                
        def output_html(self):
                fout = open('output.html','w')
                
                fout.write("<html>")
                fout.write("<meta charset='utf-8'>")
                fout.write("<body>")
                fout.write("<table>")
                print self.datas
                
                #ascii
                for data in self.datas:

                        fout.write("<tr>")
                        fout.write("<td>%s</td>" % data['name'])
                        fout.write("<td>\t</td>" )
                        fout.write("<td>%s</td>" % data['eye'])
                        fout.write("<td>\t</td>" )
                        fout.write("<td>%s</td>" % data['likenum'])
                        fout.write("<td>\t</td>" )
                        fout.write("<td>%s</td>" % data['hardnum'])
                        fout.write("<td>\t</td>" )
                        fout.write("</tr>")


                fout.write("</table>")
                fout.write("</body>")
                fout.write("</html>")
                fout.close()



