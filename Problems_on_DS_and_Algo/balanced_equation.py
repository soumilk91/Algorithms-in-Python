"""
Author: Soumil Ramesh Kulkarni
Question: Find if the given expression is balanced.
          eg: {(3+5)*[5-3]} == Balanced because every opening bracket has a corresponding closing bracket and their position is correct
	  eg: {(3+5)[}] == Not Balanced because the position of opening and closing brackets is not correct. 
	  eg: {(3+6)*{7-2} = Not Balanced because not every opening bracket has a corresponding closing bracket
Solution : Can be implemented using a Stack Data Structure
"""
import sys 
import unittest

class Stack():
	def __init__(self):
		self.arraylist = []

	def push(self, val):
		self.arraylist.append(val)
	
	def pop(self):
		if len(self.arraylist) == 0:
			print "The Stack is already Empty... Cannot pop an element"
			return
		self.arraylist.pop()

	def top(self):
		if len(self.arraylist) == 0:
                        print "The Stack is already Empty... hence the element at the top of the stack cannot be returned"
                        return
		ret_element = self.arraylist[(len(self.arraylist) - 1)]
		return ret_element

	def is_empty(self):
		if len(self.arraylist) == 0:
			return True
		else:
			return False

	def print_the_stack(self):
		if len(self.arraylist) == 0:
			print "The Stack is emnpty.... Nothing to print ..."
			return
		return self.arraylist


class check_balance():
	def __init__(self, expression):
		self.stack = Stack()
		#self.exp = raw_input("Please Enter Your Expression: ")
		self.exp = expression

	def print_exp(self):
		print self.exp

	def check_balance(self):
		inp_braces = ["(", "[", "{"]
		closing_braces = [")", "}", "]"]
		paring = {"}":"{", ")":"(", "]":"["}
		for i in self.exp:
			if i in inp_braces:
				self.stack.push(i)
			if i in closing_braces:
				top_element = self.stack.top()
				if top_element != paring[i]:
					#print "The Expression is not balanced"
					return False
				self.stack.pop()
		#ret = self.stack.print_the_stack()
		#print ret
		if self.stack.is_empty() == True:
			return True
		else:
			return False

#inp = check_balance("{(5+3) * [4-2]")
#inp.check_balance()

class TestBalancedEquation(unittest.TestCase):

	def test_correct_brackets(self):
		expression = "{(5+1)*[4-2]}"
		inp = check_balance(expression)
		self.assertTrue(inp.check_balance())
	
	def test_wrong_brackets_sequence(self):
		expression = "{(5+3) * [4-2}]"	
		inp = check_balance(expression)
		self.assertFalse(inp.check_balance())

	def test_wrong_brackets_numbering(self):
		expression = "{(5+3) * [4-2]"
		inp = check_balance(expression)
                self.assertFalse(inp.check_balance())

if __name__ == '__main__':
	unittest.main()
