"""
Author: Soumil Ramesh Kulkarni
Question: Implement an Algorithm to determine if the string has all unique characters. What if you cannot use additional data structure?
"""
import sys 
import unittest


class IsUnique():
	def __init__(self, string):
		self.string = string

	# Running Time O(n), Extra Space O(n)
	def compute_using_dict(self):
		temp_dict = {}
		for i in self.string:
			if i in temp_dict:
				return False
			else:
				temp_dict[i] = 1
		return True
	
	def compute_using_nested_for_loop(self):
		for i in range (len(self.string)- 1):
			temp = self.string[i]
			for j in range ((i + 1), len(self.string)):
				if self.string[j] == temp:
					return False
				else:
					continue
		return True
		

class Test_IsUnique_methods(unittest.TestCase):
	
	def test_function_with_dict_unique_string(self):
		a = IsUnique('soumil')
		self.assertTrue(a.compute_using_dict())

	def test_function_with_dict_not_a_unique_string(self):
		a = IsUnique('soumils')
		self.assertFalse(a.compute_using_dict())

	def test_function_with_nested_for_loops_unique_string(self):
		a = IsUnique('%soumil*')
		self.assertTrue(a.compute_using_nested_for_loop())

	def test_function_with_nested_for_loops_not_a_unique_string(self):
		a = IsUnique('%%soumils')
		self.assertFalse(a.compute_using_nested_for_loop())


if __name__ == '__main__':
	unittest.main()

		


#a= IsUnique('soumils')
#a.compute_using_dict()
#a.compute_using_nested_for_loop()
