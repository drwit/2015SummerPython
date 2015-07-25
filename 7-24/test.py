import hashmap
	
x = hashmap.new()
print x

#print hashmap.hash_key(x, 'shit')
#print hashmap.hash_key(x, 'shit')
#print hashmap.hash_key(x, 'apple')
#print hashmap.hash_key(x, 4)
#print hashmap.hash_key(x, 88)
#print hashmap.hash_key(x, 4)
#print hashmap.hash_key(x, 250)
#print hashmap.hash_key(x, 258)
#print hashmap.hash_key(x, 2)

y = [1,2,3,4,5]

for i, j in enumerate(y):
	print i, j
	
yy = [[0,1], [1,2], [2,3], [3,4]]	
for i, kv in enumerate(yy):
	print kv
	k, v = kv
	print k,v