from tree_with_t import *
import PVA_negamax
import negamax
import pvs

def main():
	# Input branching factor b , Height h and approximation approx

	branching = [3,6] #int(input("Enter Branching factor: "), 10)
	height = [4,5] #int(input("Enter Height: "), 10)
	approx_values = [0,50,100] #int(input("Enter Approximation: "), 10)

	for i in range(0, len(branching)):
		for j in range(0, len(height)):
			for k in range(0, len(approx_values)):
				b = branching[i]
				h = height[j]
				approx = approx_values[k]
				for num in range(0,5):
					tValue= random.randint(-2500,2500)
					delta = random.randint(-approx,approx)
					root = Node( tValue + delta)
					insertNodes(root, b, h, delta, approx, tValue)
					print("\nBranching factor is: {} and height is {} and approx is {}".format(b,h,approx))
					print("Tree number : {}".format(num+1))

					negamaxValue = negamax.negamax(root, b, h, negamax.alpha, negamax.beta)
					print("Negamax value is : {} ".format(negamaxValue))
					print("Static Evaluation for Negamax is : {} ".format(negamax.numberOfStaticEvaluation))

					PV, negamaxValue2 = PVA_negamax.negamax(root, b, h, PVA_negamax.alpha, PVA_negamax.beta, True)
					print("Negamax value with re-ordering is : {} ".format(negamaxValue2))
					print("Static Evaluation for Negamax with re-ordering is : {} ".format(PVA_negamax.numberOfStaticEvaluation_with_pva))

					# Since PVA_Negamax already reoredered the children, we restore the tree by inserting again
					root = Node( tValue + delta)
					insertNodes(root, b, h, delta, approx, tValue)
					pvsValue = pvs.pvs(root, b, h, pvs.alpha, pvs.beta, False)
					print("PVS value without re-ordering is : {} ".format(pvsValue))
					print("Static Evaluation for PVS without re-ordering is : {} ".format(pvs.numberOfStaticEvaluation))

					pvsValue1 = pvs.pvs(root, b, h, pvs.alpha, pvs.beta, True)
					print("PVS value with re-ordering is : {} ".format(pvsValue1))
					print("Static Evaluation for PVS with re-ordering is : {} ".format(pvs.numberOfStaticEvaluation_with_pva))

if __name__ == "__main__":
    main()