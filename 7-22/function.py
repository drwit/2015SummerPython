def add(a, b):
	y = a + b
	print '%d + %d = %d' % (a, b, y)
	
def none():
	print 'There is no arg in the function'
	
def get_shit():
	"""You may get some shit"""
	str = 'shit'
	return str
	
print 'Plz input two numbers:'
a = int(raw_input('first one>'))
b = int(raw_input('second one>'))
add(a, b)

none()

print 'We are getting shit!>>>', get_shit()