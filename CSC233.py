import random
#special_characters = set(∨, ∧, ¬, →, ↔, ⊕)

# def parse_character(expression):
# 	for i in special_characters:
# 		if i not in expression:
# 			return

# 	num_var, varss = 0, set()

class treeNode:
	def __init__(self, data):
		self.data = data
		self.left = None 
		self.right = None

	def addToNode(self, x):
		if(x < self.data):
			if(self.left == None):
				p = treeNode(x)
				self.left = p
			else:
				self.left.addToNode(x)

		elif(x > self.data):
			if(self.right == None):
				p = treeNode(x)
				self.right = p
			else:
				self.right.addToNode(x)

		else:
			return

	def postOrderPrintNode(self):
		if self.left != None:
			self.left.postOrderPrintNode()

		if self.right != None:
			self.right.postOrderPrintNode()

		print(self.data)

	def display_node(self):
		lines, *_ = self._display_aux()
		for line in lines:
			print(line)

	def _display_aux(self):
		"""Returns list of strings, width, height, and horizontal coordinate of the root."""
		# No child.
		if self.right is None and self.left is None:
			line = '%s' % self.data
			width = len(line)
			height = 1
			middle = width // 2
			return [line], width, height, middle

		# Only left child.
		if self.right is None:
			lines, n, p, x = self.left._display_aux()
			s = '%s' % self.data
			u = len(s)
			first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
			second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
			shifted_lines = [line + u * ' ' for line in lines]
			return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

		# Only right child.
		if self.left is None:
			lines, n, p, x = self.right._display_aux()
			s = '%s' % self.data
			u = len(s)
			first_line = s + x * '_' + (n - x) * ' '
			second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
			shifted_lines = [u * ' ' + line for line in lines]
			return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

		# Two children.
		left, n, p, x = self.left._display_aux()
		right, m, q, y = self.right._display_aux()
		s = '%s' % self.data
		u = len(s)
		first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
		second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
		if p < q:
			left += [n * ' '] * (q - p)
		elif q < p:
			right += [m * ' '] * (p - q)
		zipped_lines = zip(left, right)
		lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
		return lines, n + m + u, max(p, q) + 2, n + u // 2


class BST:
	def __init__(self):
		self.root = None 

	def addToBST(self, x):
		if self.root == None:
			p = treeNode(x)
			self.root = p 
		else:
			self.root.addToNode(x)

	def parseFromArray(self, array):
		for i in array:
			self.addToBST(i)

	def postOrderPrintTree(self):
		self.root.postOrderPrintNode()

	def display_tree(self):
		self.root.display_node()




# function to print the headline containing all the logical values in alphabetic characters 
def print_headlines(n):
	for i in range(n):
		print(chr(i + 97), end = ' ')
	print('', end = '')
	print("|", end = ' ')
	print(chr(n + 97))
	for _ in range(n * 3 - 1):
		print("-", end = '')
	print()

# function to get the logical result from the proposition
def proposition(a, b, c, d):
	# the expression changes here 
	result = not (a and b and not c) and (b and d)
	return result

# generate the values of the logical variables in the form of the truth table
def generate_truth_table(n, arr, i, expression):
	if i == n:
		if proposition(arr[0], arr[1], arr[2], arr[3]):
			expression.append([arr[0], arr[1], arr[2], arr[3], proposition(arr[0], arr[1], arr[2], arr[3])])
		print_table(array, proposition(array[0], array[1], array[2], array[3]))
		return 

	arr[i] = 0
	generate_truth_table(n, arr, i + 1, expression)

	arr[i] = 1
	generate_truth_table(n, arr, i + 1, expression)	

# function to print the truth table using the values from 2 previous functions
def print_table(array, result):
	for i in range(len(array)):
		if array[i] == 1:
			print("T", end = ' ')
		else:
			print("F", end = ' ')

	print("|", end = ' ')
	if result == 1:
		print("T")
	else:
		print("F")
	print()

# make the disjunctive normal form and print it 
def DNF(array):
	final_expression = ""
	for i in range(len(array)):
		for j in range(len(array[i])):
			if j == 0:
				final_expression += "("
			if not array[i][j]:
				final_expression += "¬"
			if j < len(array[i]) - 1:
				final_expression += chr(97 + j)
			if j < len(array[i]) - 2:
				final_expression += " ∧ "
			if j == len(array[i]) - 1:
				final_expression += ")"
		if i < len(array) - 1:
			final_expression += " ∨ "
	print(final_expression)



# expression = [] #array that stores logical expressions that result in a "True" result
# n = 4 #number of logical variables
# array = [None] * n
# print_headlines(n)
# generate_truth_table(n, array, 0, expression)
# DNF(expression)


# nodes = [4, 3, 2, 7, 5, 12, 34, 23, 1, 9, 8, 10, 20, 24, 21, 45, 16, 18, 90, 32, 30, 27, 29, 44, 31, 33, 36, 0, -1, -23, -3, -7]
nodes = []
for _ in range(50):
	nodes.append(random.randint(0, 100))

BST = BST()
BST.parseFromArray(nodes)
BST.display_tree()

