# -*- coding: utf-8 -*-


class HtmlOutputer(object):
	
	def __init__(self):
		self.datas = [ ]
			
	def collect_data(self,data):
		if data is None:
			return None
		
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
			fout.write("<td>%s</td>" % data['date'])
			fout.write("<td>\t</td>" )
			fout.write("<td>%s</td>" % data['name'])
			fout.write("<td>\t</td>" )
			fout.write("<td>%s</td>" % data['href'])
			fout.write("<td>\t</td>" )
			fout.write("<td>%s</td>" % data['singer'])
			fout.write("<td>\t</td>" )
			fout.write("<td>%s</td>" % data['click'])
			fout.write("</tr>")


		fout.write("</table>")
		fout.write("</body>")
		fout.write("</html>")
		fout.close()
