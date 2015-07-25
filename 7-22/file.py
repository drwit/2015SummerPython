from sys import argv

script, file_name = argv

txt = open(file_name)
print txt.read()

close(txt)