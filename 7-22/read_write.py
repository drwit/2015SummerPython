from sys import argv

script, filename = argv
print 'We are going to erase %r.' % filename
print 'Hit Ctrl + C to cancel or enterany key to continue.'

raw_input('?')

print 'Openning the file...'
txt = open(filename,'w')

print 'Truncating the file'
txt.truncate()

print 'Input 3 lines:'
line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

txt.write(line1)
txt.write('\n')
txt.write(line2)
txt.write('\n')
txt.write(line3)
txt.write('\n')

print 'Closing file...'
txt.close()