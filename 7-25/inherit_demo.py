class Parent(object):

	def fun1(self):
		print "PARENT FUN1()"

	def fun2(self):
		print "PARENT FUN2()"

	def fun3(self):
		print "PARENT FUN3()"

class Child(Parent):

	def fun2(self):
		print "CHILD REWRITE FUN2()"

	def fun3(self):
		print "Before altered"
		super(Child, self).fun3()
		print "After altered"


dad = Parent()
son = Child()

dad.fun1()
son.fun1()

dad.fun2()
son.fun2()

dad.fun3()
son.fun3()
son.fun3()