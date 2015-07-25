from sys import argv

script, filename = argv

def show_all(f):
	print f.read()
	
def rewind(f):
	f.seek(0)
	
def show_line(f, current_line):
	print current_line, f.readline(),
	
f = open(filename)
print 'all:'
show_all(f)

print 'rewinding...'
rewind(f)

current_line = 1
show_line(f, current_line)
current_line += 1
show_line(f, current_line)
current_line += 1
show_line(f, current_line)