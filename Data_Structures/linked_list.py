"""
Author: Soumil Ramesh Kulkarni
Description: Basic Operations on a Singly Linked List
Operations Coverd: 
1) Add a node at the beginning of a Linked List
2) Add a node at the end of a Linked List
3) Add a node at the nth position of a Linked List
4) Delete a node at the beginning of a Linked List
5) Delete a node at the end of a Linked List
6) Delete a node at the nth position of a Linked List
7) Reverse a Singly Linked List (Iterative Solution)

"""
import sys 

class Node(object):
	def __init__(self, data):
		self.data = data
		self.next_node = None

class LinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None

	def add_at_begining(self, data):
		new_node = Node(data)
		if ( (self.head == None) and (self.tail == None)):
			self.head = new_node
			self.tail = new_node
		else:
			new_node.next_node = self.head
			self.head = new_node
	
	def add_at_the_end(self,data):
		new_node = Node(data)
		if ((self.tail == None) and (self.head == None)):
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next_node = new_node
			self.tail = new_node

	def add_node_at_k_th_position(self, data, position):
		new_node = Node(data)
		if position < 1:
			print "Position given is less than 1 so it is invalid"
			return
		elif position == 1:
			new_node.next_node = self.head
			self.head = new_node
			return
		else:
			current_node = self.head
			if current_node == None:
				print "List Empty and the position given is wrong"
				return
			for i in range(position - 2):
				current_node = current_node.next_node
				if current_node == None:
					print "Not enough space in the Linked List. Position entered is not correct"
					return
			new_node.next_node = current_node.next_node
			current_node.next_node  = new_node
				
				
	def delete_node_at_the_beginning(self):
		if self.head == None:
			print "The List is already empty"
			return
		else:
			self.head = self.head.next_node

	def delete_node_at_the_end(self):
		if self.head == None:
                        print "The List is already empty"
                        return
		else:
			previous_node = None
			current_node = self.head
			if self.head.next_node == None:
				self.head = None
				return
			while (current_node.next_node != None):
				previous_node = current_node
				current_node = current_node.next_node
			previous_node.next_node = None	 

	
	def delete_node_at_n_th_position(self, position):
		if self.head == None:
			print "The Linked List is already empty"
			return
		else:
			previous_node = None
			current_node = self.head
			if position == 1:
				self.head = self.head.next_node
				return
			else:
				for i in range (position - 1):
					previous_node = current_node
					current_node = current_node.next_node
					if current_node == None:
						print "Position entered is Wrong. No elements in the linkedlist to delete"
						return
				previous_node.next_node = current_node.next_node
				current_node.next_node = None			 	

	def reverse_a_linked_list_iterative(self):
		previous = None
		current = self.head
		while current != None:
			next = current.next_node
			current.next_node = previous
			previous = current
			current = next	
		self.head = previous


	def print_the_entire_linkedlist(self):
		ret_list = []
		if self.head == None:
			print "Linked List is empty"
		else:
			current_node = self.head
			while current_node:
				ret_list.append(current_node.data)
				current_node = current_node.next_node	
			print ret_list
