import re

def header(fw, title):						# Make HTML Header
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
	data = fr.readline()					# to remove title
	data = fr.readline()					# to remove blank
	regex_h2_1 = re.compile('^(ARGUMENT).')			# for tagname h2
	regex_h2_2 = re.compile('^(I{0,3}V?I{0,2})\.')	# for tagname h2
	regex_pp = re.compile('^[A-Z].+.$')			# for tagname p
	# Handle Exception
	regex_Tw = re.compile('Twas..ight')			# Exception 1 => there is no <br/>
	regex_sp = re.compile('He r.+.$')			# Exception 2 => end with </p>
	regex_pb = re.compile('It i.+,$')			# Exception 3 => start with <p>
	while data:
		data = data[:-1]				# slicing the data
		l = len(data)					# calculate the length of data
		if regex_h2_1.search(data) != None:		# search for 'argument' in data
			fw.write("<h2>%s</h2>\n\n" %data[:-1])	# formatting with h2 tag
			data = fr.readline()			# flush the next line
		elif regex_h2_2.search(data) != None:		# search for 'roman number' in data
			fw.write("<h2>%s</h2>\n" %data[:-1])	# formatting with h2 tag
		elif regex_Tw.search(data) != None:		# search for 'Twas right' or 'Twas night' in data
			fw.write(data + "\n")			# write on file
		elif regex_pp.search(data) != None:		# search for long string in data
			fw.write("<p>%s.</p>\n\n" %data[:-1])	# formatting with p tag
			data = fr.readline()			# flush the next line
		elif regex_sp.search(data) != None:		# handle exception
			fw.write("%s.</p>\n" %data[:-1])	# add </p> at the end of string
		elif l == 0:					# If there is no contents,
			fw.write("<br/>\n")			# Just replace it with <br/>
		elif regex_pb.search(data) != None:		# handle exception
			fw.write("  <p>%s<br/>\n" %data.lstrip())# add <p> at the start of string and <br/> at the end of string
		else:
			regex = re.compile('$')			# If there is no matching,
			fw.write(regex.sub("<br/>", data) + "\n")# add <br/> at the end of string
		data = fr.readline()				# read next line

def footer(file):						# Make HTML Footer
	file.write(" </body>\n")
	file.write("</html>\n\n")

if __name__ == '__main__':
	file_read = 'rime.txt'					# input file
	file_write = 'rime.html'				# output file
	with open('convert/' + file_read, 'r') as fr:		# open input file
		with open('convert/' + file_write, 'w') as fw:	# oen output file
			header(fw, fr.readline()[:-1])		# maek header and make title
			body(fr, fw)				# make body
			footer(fw)				# make footer
