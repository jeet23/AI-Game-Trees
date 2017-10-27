pv = {-1752: 1755, 1755: -1753, -1753: 1756, 1756: None, 7236: None, 6174: -6179, -6179: None, 9455: -9458, -9458: 9453, 9453: None, 9511: None, -7579: 7581, 7581: None, 9809: None}

index=0
output = {}
for i in pv:
	print(index, i, pv[i])

	list_of_keys = list(pv.keys())
	list_of_values = list(pv.values())

	j = index
	output[list_of_keys[index]] = list()
	while(j < len(list_of_keys)-1 and list_of_values[j] == list_of_keys[j+1] and list_of_values[j] is not None):
		output[list_of_keys[index]].append(list_of_values[j])
		j+=1
	index+=1

print(output)