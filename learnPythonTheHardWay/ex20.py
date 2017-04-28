from sys import argv
script,filename=argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count,f):
	print line_count,f.readline()

cruurent_file=open(filename)

print_all(cruurent_file)
rewind(cruurent_file)
print_a_line(1,cruurent_file)
