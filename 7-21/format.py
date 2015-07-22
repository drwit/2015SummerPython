format = "%s %s %s %s"

print format % (1,2,3,4)
print format % ('a', 'bat', 'red capes', 'cheese')
print format % ("snake", "jake", "4", 'armstrong')

fruit = format % ('cake', 'pinch', 'apple', 'elppa')

print fruit + " which is true fruit?"

print '''
	cat
	dog
	human
'''

print """
cat
dog
human
"""