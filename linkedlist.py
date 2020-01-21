import sys

class Node:
	def __init__(self , value):
		self.next = None
		self.data = value

class LinkedList:
	def __init__(self):
		self.start = None

	def insertLast(self , value):
		newNode = Node(value)
		if self.start == None:
			self.start = newNode
			print("{} inserted in the beginning".format(value))
		else:
			temp = self.start
			while temp.next is not None:
				temp = temp.next
			temp.next = newNode
			print("{} inserted successfully at the last".format(value))

	def insertFirst(self , value):
		newNode = Node(value)
		if self.start == None:
			self.start = newNode
			print("{} inserted in the beginning".format(value))
		else:
			newNode.next = self.start
			self.start = newNode
			print("{} inserted successfully in the beginning".format(value))
			
	def insertAfter(self , after , value):
		newNode = Node(value)
		if self.start == None:
			print("Linked list is empty , inserting {}".format(value))
			self.start = newNode
		else:
			temp = self.start
			while temp is not None:
				if temp.data == after:
					newNode.next = temp.next
					temp.next = newNode
					break
				else:
					temp = temp.next
			print("{} inserted successfully after {}".format(value , after))
			
	def insertBefore(self , before , value):
		newNode = Node(value)
		if self.start == None:
			print("Linked list is empty , inserting {}".format(value))
			self.start = newNode
		else:
			previous_node = self.start
			next_node = previous_node.next
			if self.start.data == before:
				insertFirst(value)
			else:
				while next_node is not None:
					if next_node.data == before:
						newNode.next = next_node
						previous_node.next = newNode
						print("{} inserted successfully before {}".format(value , before))
						break
					else:
						previous_node = next_node
						next_node = next_node.next

	def removeFirst(self):
		if self.start == None:
			print("Linked list is empty")
		else:
			temp = self.start
			self.start = self.start.next
			print("Start Node: {} successfully deleted".format())
			
	def removeLast(self):
		if self.start == None:
			print("Linked list is empty")
		else:
			second_last = self.start
			last = second_last.next
			while last.next is not None:
				second_last = last
				last = last.next
			second_last.next = None
			print("Last Node successfully deleted")

	def removeValue(self , value):
		if self.start == None:
			print("Linked list is empty")
		else:
			target_node = self.start
			nextNode = target_node.next
			if target_node.data == value:
				self.removeFirst()
			else:
				while nextNode.data != value:
					target_node = nextNode
					nextNode = nextNode.next
				target_node.next = nextNode.next
				print("{} successfully deleted".format(value))
					

	def displayList(self):
		if self.start == None:
			print("Linked list is empty")
		else:
			temp = self.start
			print("\nLinked List:")
			while temp is not None:
				print(temp.data , end = "  ")
				temp = temp.next


#####MAIN########
obj = LinkedList()
while True:
	print("\n--------------------------------")
	print("Main Menu")
	print("1. Insert node (start)")
	print("2. Insert node (end)")
	print("3. Insert after number")
	print("4. Insert before number")
	print("5. Remove node (start)")
	print("6. Remove node (end)")
	print("7. Remove node (by value")
	print("Enter <space> to display linked list")
	print()
	print("Enter any other key to exit")
	print("---------------------------------")
	ch = input("> ")
	
	if ch == " ":
		obj.displayList()
	elif ch == "1":
		values = list(map(int , input("Enter space separated values > ").strip().split(" ")))
		for value in values:
			obj.insertFirst(value)
	elif ch == "2":
		values = list(map(int , input("Enter space separated values > ").strip().split(" ")))
		for value in values:
			obj.insertLast(value)
	elif ch == "3":
		l = input("Enter the data after which the value is to be inserted and the value separated by space > ").strip().split(" ")
		obj.insertAfter(int(l[0]) , int(l[1]))
	elif ch == "4":
		l = input("Enter the data before which the value is to be inserted and the value separated by space > ").strip().split(" ")
		obj.insertBefore(int(l[0]) , int(l[1]))
	elif ch == "5":
		obj.removeFirst()
	elif ch == "6":
		obj.removeLast()
	elif ch == "7":
		l = int(input("Enter the value to be removed > "))
		obj.removeValue(l)
	else:
		sys.exit()
