import random
from tree import *

alpha=-10000
beta=10000

def evaluation(alpha, beta):
	return (alpha * beta) / 1000;

def makemove(root):
	return 1

def unmakemove(root):
	return 0

def pvs(root, branching, height, alpha, beta):
	if len(root.children) == 0:
		return evaluation(alpha, beta)
	else:
		makemove(root.children[0])
		score = - pvs(root.children[0], branching, height - 1 , - beta, -alpha)
		unmakemove(root.children[0])
		if score < beta:
			for m in range(1, branching):
				LB = max(alpha, score)
				UB = LB + 1
				makemove(root.children[m])
				temp = - pvs (root.children[m], branching, height - 1, -UB, -LB)
				if(temp > UB) and (temp < beta):
					temp = - pvs(root.children[m], branching, height - 1, -beta, -temp)
				unmakemove(root.children[m])
				score = max(score,temp)
				if (temp > beta):
					break
			return score

def main():
	# Input branching factor b , Height h and approximation approx

	b = 2 #int(input("Enter Branching factor: "), 10)
	h = 3 #int(input("Enter Height: "), 10)
	approx = 5 #int(input("Enter Approximation: "), 10)

	root = Node(random.randint(-2500,2500))
	print("Adding root node at height {}: {}".format(h, root.data))
	insertNodes(root, b ,h, approx)

	printTree(root, b, h)

	pvsValue = pvs(root, b, h, alpha, beta)
	print("Negamax value is : {} ".format(negamaxValue))
	print("numberOfStaticEvaluation is : {} ".format(numberOfStaticEvaluation))

main()
