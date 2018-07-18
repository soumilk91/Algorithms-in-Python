"""
Author: Soumil Ramesh Kulkarni
Question: Assume you have a method isSubstring which checks if one word is a substring of another, Given 2 strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring.
Eg: "waterbottle" is a rotation of "erbottlewat" 
"""
import sys 
import unittest

class StringRotation():
	def __init__(self, string1, string2):
		self.string1 = string1
		self.string2 = string2
	
	def is_s2_rotated(self):
		if len(self.string1) != len(self.string2):
			return False
		first_char = self.string1[0]
		no_of_first_chars_in_str_2 = self.string2.count(first_char)
		if no_of_first_chars_in_str_2 < 1:
			return False
		elif no_of_first_chars_in_str_2 == 1:
			string2_index = self.string2.index(first_char)
			first_substr = self.string2[:string2_index]
			second_substr = self.string2[(string2_index) : ]
			#print first_substr
			#print second_substr
			if ((first_substr in self.string1) and (second_substr in self.string1)):
				return True
			else:
				return False
		else:
			index_list = []
			for i in range (len(self.string2)):
				if self.string2[i] == first_char:
					index_list.append(i)
			for i in index_list:
				first_substr = self.string2[ : i]
				second_substr = self.string2[i : ]
				if ((first_substr in self.string1) and (second_substr in self.string1)):
					return True
				else:
					continue
			return False

class TestStringRotation(unittest.TestCase):
	def test_correct_rotation(self):

	def test_wrong_rotation(self):
		
	def test_multiple_same_first_letters(self):

	def test_when_two_completely_different_strings_given(self):


if __name__ == "__main__":
	unittest.main()

#a = StringRotation("wwaterbottlew", "erbottlewwat")
#print a.is_s2_rotated()	
