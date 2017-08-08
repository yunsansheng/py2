# -*- coding: utf-8 -*-


class HtmlOutputer(object):
	
	def __init__(self):
		self.datas = [ ]
			
	def collect_data(self,data):
		if data is None:
			return None
		print data['url']
		print data['title'].encode('utf-8')
		print data['summary'].encode('utf-8')
		self.datas.append(data)
		
	def output_html(self):
		fout = open('output.html','w')
		
		fout.write("<html>")
		fout.write("<meta charset='utf-8'>")
		fout.write("<body>")
		fout.write("<table>")
		
		#ascii
		for data in self.datas:
			fout.write("<tr>")
			fout.write("<td>%s</td>" % data['url'])
			fout.write("<td>\t</td>" )
			fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
			fout.write("<td>\t</td>" )
			fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
			fout.write("</tr>")
		
		fout.write("</table>")
		fout.write("</body>")
		fout.write("</html>")
		fout.close()
