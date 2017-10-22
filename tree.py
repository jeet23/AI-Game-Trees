import random
import pdb
INFINITY = 10001
class Node(object):
	def __init__(self, data):
		self.data = data
		self.children = []
		self.reordered_children = []
	def add_child(self, obj):
		self.children.append(obj)
		self.reordered_children.append(obj)


def insertNodes(root, branching, height, approx):
	level = height - 1
	if (height == 0) or (branching == 0):
		return
	# Delta is 0 for leaf nodes and between +approx and -approx for internal nodes
	delta = random.randint(-approx, approx) if height != 1 else 0
	
	addDaughtersAtEachLevel(root, branching, delta, level)

	# Calculating chance of branching factor for all but root node
	branchingFactor = calculateBranchingFactorChance(branching)
	branching = branchingFactor
	recurseForEachChild(root, branching, height, approx)

def recurseForEachChild(root, branching, height, approx):
	for daughters in root.children:
		if daughters.data == INFINITY:
			break
		insertNodes(daughters, branching, height-1, approx)

def addDaughtersAtEachLevel(root, branchingFactor, delta, level):
	randomlyChosenDaughter = random.randint(0, branchingFactor-1)
	for branches in range(0, branchingFactor):
		negatedValue = -(root.data)
		# pdb.set_trace()
		if branches == randomlyChosenDaughter:
			E = negatedValue + delta
			print("Copying parent Negated node ----> Adding child node at level {} : {}".format(level, E))
			root.add_child(Node(E))
		else:
			randomNumberGreaterThanNegatedValue = random.randint(negatedValue+1,INFINITY)
			E = randomNumberGreaterThanNegatedValue + delta
			print("Creating random node ----> Adding child node at level {} : {}".format(level, E))
			root.add_child(Node(E))


def printTree(root, branching, height):
	print("----------------------- T R E E ---------------------")
	for level in range(0, height + 1):
		# if level > 1:
		# 	branchingFactor = calculateBranchingFactorChance(branching)
		# else:
		# 	branchingFactor = branching
		# flagBranchChanged = True if branching != branchingFactor else False
		# TODO :: Printing tree with branching factor b+1 or b-1 is BUGGY right now. (>90% chance cases)

		printGivenLevel(root, level, branching)
		print("\n")

def printGivenLevel(root, level, branchingFactor):
	if root is None:
		return
	elif level == 0:
		print(root.data, end=" ")
	elif level > 0:
		for j in range(0, branchingFactor):				
			printGivenLevel(root.children[j], level-1, branchingFactor)
			print(end = "   ")

def calculateBranchingFactorChance(branching):
	if (90 < branching % 100 < 95):
		branchingFactor = branching + 1
	elif ( branching % 100 > 95):
		branchingFactor = branching - 1
	else:
		branchingFactor = branching
	return branchingFactor

def main():
	# Input branching factor b , Height h and approximation approx

	b = 2 #int(input("Enter Branching factor: "), 10)
	h = 3 #int(input("Enter Height: "), 10)
	approx = 5 #int(input("Enter Approximation: "), 10)

	root = Node(random.randint(-2500,2500))
	print("Adding root node at height {}: {}".format(h, root.data))
	insertNodes(root, b ,h, approx)

	printTree(root, b, h)

main()
