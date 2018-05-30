import sys 

class Stack:
	def __init__(self):
		self.arraylist = []

	def is_empty(self):
		if len(self.arraylist) == 0:
			print "The Stack is Empty"
		else:
			print "The Stack is not Empty.... The contents of the Stack are: "
			print self.arraylist

	def push(self, value):
		self.arraylist.append(value)
		print "The current contents of the stack are: "
		print self.arraylist

	def pop(self):
		if len(self.arraylist) == 0:
			self.is_empty()
			return
		self.arraylist.pop()
		print "The contents of the stack after the pop operation are:"
		print self.arraylist

	def size_of_the_stack(self):
		print "The Size of the Stack is : %s" %(str(len(self.arraylist)))
	
