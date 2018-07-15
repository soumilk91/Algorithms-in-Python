"""
Author: Soumil Ramesh Kulkarni
Question: Given 2 strings find if one is permutation of the other. 
"""
import sys
import unittest
class StringPermutation():
	def __init__(self, string1, string2):
		self.string1 = string1
		self.string2 = string2

	def is_one_string_permutation_of_other(self):
		# Check if the length of both the given strings is equal
		if len(self.string1) != len(self.string2):
			return False
		string1_dict = {}
		string2_dict = {}
		for i in range (len(self.string1)):
			if self.string1[i] not in string1_dict:
				string1_dict[self.string1[i]] = 1
			else:
				string1_dict[self.string1[i]] += 1
			if self.string2[i] not in string2_dict:
                                string2_dict[self.string2[i]] = 1
                        else:
                                string2_dict[self.string2[i]] += 1
		if string1_dict == string2_dict:
			return True
		else:
			return False


class TestStringPermutation(unittest.TestCase):
	def test_perm_strings(self):
		a = StringPermutation("god", "dog")
		self.assertTrue(a.is_one_string_permutation_of_other())

	def test_not_perm_strings(self):
		a = StringPermutation("god", "dogg")
		self.assertFalse(a.is_one_string_permutation_of_other())

if __name__ == "__main__":
	unittest.main()
