import re

def header(fw, title):			# Make HTML Header
	fw.write("<!DOCTYPE html>\n")
	fw.write("<html xmlns=\"http://www.w3.org/1999/xhtml\">\n")
	fw.write(" <head>\n")
	fw.write("  <title>%s</title>\n" %title)
	fw.write("  <meta charset=\"utf-8\"/>\n")
	fw.write(" </head>\n")
	fw.write("<body>\n")
	fw.write("<h1>%s</h1>\n" %title)
	fw.write(title + "\n\n")

def body(fr, fw):
	data = fr.readline()		# to remove title
	data = fr.readline()		# to remove title
	regex_h2_1 = re.compile('^(ARGUMENT).')			#
	regex_h2_2 = re.compile('^(I{0,3}V?I{0,2})\.')
	regex_pp = re.compile('^[A-Z].+.$')
	# Exception
	regex_Tw = re.compile('Twas..ight')
	regex_sp = re.compile('He r.+.$')
	regex_pb = re.compile('It is an anc.+,$')
	while data:
		data = data[:-1]
		l = len(data)
		if regex_h2_1.search(data) != None:
			fw.write("<h2>%s</h2>\n\n" %data[:-1])
			data = fr.readline()
		elif regex_h2_2.search(data) != None:
			fw.write("<h2>%s</h2>\n" %data[:-1])
		elif regex_Tw.search(data) != None:
			fw.write(data + "\n")
		elif regex_pp.search(data) != None:
			fw.write("<p>%s.</p>\n\n" %data[:-1])
			data = fr.readline()
		elif regex_sp.search(data) != None:
			fw.write("%s.</p>\n" %data[:-1])
		elif l == 0:
			fw.write("<br/>\n")
		elif regex_pb.search(data) != None:
			fw.write("  <p>%s<br/>\n" %data.lstrip())
		else:
			regex = re.compile('$')
			fw.write(regex.sub("<br/>", data) + "\n")
		data = fr.readline()

def footer(file):
	file.write(" </body>\n")
	file.write("</html>\n\n")

if __name__ == '__main__':
	file_read = 'rime.txt'
	file_write = 'rime.html'
	with open('convert/' + file_read, 'r') as fr:
		with open('convert/' + file_write, 'w') as fw:
			header(fw, fr.readline()[:-1])
			body(fr, fw)
			footer(fw)