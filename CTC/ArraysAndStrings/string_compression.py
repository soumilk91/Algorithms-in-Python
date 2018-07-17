"""
Author: Soumil Ramesh Kulkarni
Question: Implement a methos to perform basic string compression using the counts of repeated characters. If the "compressed" string is would not become smaller than the original string, your method should return the original string. You can assume that the string can contain only uppercase and lowercase letters
  eg: aabcccaaa -> a2b1c3a3
      abcdef -> a1b1c1d1e1f1 -> in this case it should return -> abcdef
"""

import sys 
import unittest

class StringCompression():
	def __init__(self, string):
		self.string = string

	def str_compress(self):
		ret_string = ""
		counter = 0
		current_letter = ""
		for i in self.string:
			if i != current_letter:
				ret_string = ret_string + str(counter)
				counter = 0
				current_letter = i
				ret_string = ret_string + current_letter
				counter += 1
			else:
				counter += 1

		ret_string = ret_string + str(counter)
		result_string = ret_string[1:]
		if len(self.string) <= len(result_string):
			return self.string
		else:
			return result_string

class TestStringCompression(unittest.TestCase):
	def test_correct_compress(self):
		a = StringCompression("aabcccaaa")
		self.assertEqual(a.str_compress(), "a2b1c3a3")

	def test_same_string_return(self):
		a = StringCompression("abcdef")
		self.assertEqual(a.str_compress(), "abcdef")

if __name__ == "__main__":
	unittest.main()
