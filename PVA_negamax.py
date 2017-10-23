import random
from tree_with_t import *
import pdb

alpha = -10000
beta = 10000

numberOfStaticEvaluation = 0
numberOfStaticEvaluation_with_pva = 0
iterativeDeepening = 5 #User has to input
heightChecked = 0

def negamax(root, branching, height, alpha, beta, Modified):
	global heightChecked, iterativeDeepening
	# Check if leaf node or Iterative deepening reached limit
	if len(root.children) == 0 or heightChecked == iterativeDeepening:
		global numberOfStaticEvaluation, numberOfStaticEvaluation_with_pva
		numberOfStaticEvaluation += 1
		# if Modified is True:
		# 	numberOfStaticEvaluation_with_pva += 1
		# else:
		# 	numberOfStaticEvaluation += 1
		PV = {}
		return [PV, root.data]
	else:
		# Implement OrderMoves(root.children) here if parameter Modified == True
		if Modified is True:
			root = orderMoves(root)
		PV = {}
		for move in range(0, branching):
			newNode = root.children[move]
			temp = -(negamax(newNode, branching, height - 1, -beta, -alpha, Modified))[1]
			# Do nothing ---> destroy newNode
			if temp > beta:
				return [PV,temp]
			alpha = max(temp, alpha)
		heightChecked += 1 # Next level being checked now
	return [PV,alpha]


def orderMoves(root):
	minChild = root.children[0].data
	for daughters in range(0, len(root.children)):
		# Find the best node
		minChild = min(minChild, root.children[daughters].data)

	# Finds the index of min element
	array = [daughters.data for daughters in root.children]
	minIndex = array.index(minChild)
	
	for daughters in range(0, len(root.children)):
 		# Copy nodes to reordered nodes
		root.reordered_children[daughters].data = root.children[daughters].data
	
	print("Original order : {} ".format([item.data for item in root.reordered_children]))
	
	# Swapping min element with first element
	root.children[0].data, root.children[minIndex].data = root.children[minIndex].data, root.children[0].data

	print("Original order : {} ".format([item.data for item in root.reordered_children]))
	print("Changed order : {} ".format([item.data for item in root.children]))
	return root

def main():
	# Input branching factor b , Height h and approximation approx

	b = 2 #int(input("Enter Branching factor: "), 10)
	h = 3 #int(input("Enter Height: "), 10)
	approx = 5 #int(input("Enter Approximation: "), 10)


	tValue= random.randint(-2500,2500)
	delta = random.randint(-approx,approx)
	root = Node( tValue + delta)
	print("Adding root node at height {}: T Value: {}".format(h, tValue))
	insertNodes(root, b, h, delta, approx, tValue)
	printTree(root, b, h)
	PV, negamaxValue = negamax(root, b, h, alpha, beta, True)
	print("PV is {}: ".format(PV))
	print("Negamax value is : {} ".format(negamaxValue))
	print("numberOfStaticEvaluation is : {} ".format(numberOfStaticEvaluation))


	# root = orderMoves(root)
	# print("After Principal Variation Re-ordering")
	# printTree(root, b, h)
	# PV1, negamaxValue1 = negamax(root, b, h, alpha, beta, True)
	# print("PV is {}: ".format(PV1))
	# print("Negamax value is : {} ".format(negamaxValue1))
	# print("numberOfStaticEvaluation_with_pva is : {} ".format(numberOfStaticEvaluation_with_pva))

main()

