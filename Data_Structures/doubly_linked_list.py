"""
Author: Soumil Ramesh Kulkarni
Description: Basic Operations on a Doubly Linked List
Operations Coverd: 
1) Add a node at the beginning of a Linked List
2) Add a node at the end of a Linked List
3) Add a node at the nth position of a Linked List
4) Delete a node at the beginning of a Linked List
5) Delete a node at the end of a Linked List
6) Delete a node at the nth position of a Linked List

"""
import sys 

class Node():
	def __init__(self, data):
		self.data = data
		self.previous_node = None
		self.next_node = None

class  DoublyLinkedList():
	def __init__(self):
		self.head = None
		self.tail = None

	def add_node_at_beginning(self, data):
		new_node = Node(data)
		if self.head == None:
			self.head = new_node
			self.tail = new_node
		else:
			new_node.next_node = self.head
			self.head.previous_node = new_node
			self.head = new_node

	def add_node_at_the_end(self, data):
		new_node = Node(data)
		if self.head == None:
			self.head = new_node
			self.tail = new_node
		else:
			current_node = self.head
			while(current_node.next_node != None):
				current_node = current_node.next_node
			new_node.previous_node = current_node
			current_node.next_node = new_node
			self.tail = new_node

	def add_node_at_k_th_location(self, data, position):
		new_node = Node(data)
		if position < 1:
			print "Location entered is wrong !!! Location cannot be less than 1"
			return
		elif position == 1:
			if self.head == None:
				self.head = new_node
				self.tail = new_node
				return
			else:
				new_node.next_node = self.head
				self.head.previous_node = new_node
				self.head = new_node
		else:
			prev = None
			curr = self.head
			for i in range(position - 1):
				prev = curr
				curr = curr.next_node
				if curr == None:
					if i == position - 2:
						break
					else:
						print "Not enough space in the linked list. The location entered is wrong"
						return
			new_node.next_node = curr
			new_node.previous_node = prev
			prev.next_node = new_node
			if curr == None:
				self.tail = new_node
			else:
				curr.previous_node = new_node
						
	def delete_node_at_the_beginning(self):
		if self.head == None:
			print "The Linked List is already empty"
			return
		else:
			self.head = self.head.next_node

	def delete_node_at_the_end(self):
		if self.head == None:
			print "The Linked List is already empty"
			return
		else:
			current_node = self.head
			if current_node.next_node == None:
				self.head = None
				self.tail = None
				return
			while (current_node.next_node != None):
				current_node = current_node.next_node
			self.tail = current_node.previous_node
			self.tail.next_node = None

	def delete_node_at_k_th_location(self, position):
		if self.head == None:
			print "The Linked List is already empty"
			return
		prev = None
		curr = self.head
		if position == 1:
			if self.head.next_node ==  None:
				if position > 1:
					print "Not enough elements in the Linked List. The position entered is wrong"
					return
				else:
					self.head = None
					self.tail = None
					return
			else:
				current_node = self.head 
				current_node = current_node.next_node
				self.head.next_node = None
				self.head = current_node
				return
		for i in range(position - 1):
			prev = curr
			curr = curr.next_node
			if curr == None:
				"Not enough elements in the Linked List. The position entered is wrong"
				return
		prev.next_node = curr.next_node
		curr = curr.next_node
		if curr == None:
			self.tail = prev
		else:
			curr.previous_node = prev
			

	def pring_doubly_linked_list(self):
		if self.head == None:
			print "Linked List is empty"
			return
		ret_list = []
		current_node = self.head
		while current_node != None:
			ret_list.append(current_node.data)
			current_node = current_node.next_node
		print ret_list	
