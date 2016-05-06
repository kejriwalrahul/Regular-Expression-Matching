# Rahul Kejriwal
# CS14B023

def validCYK(regex):
	length = len(regex)

	# Adding basic productions
	unitProd = [('L','('),
				('R',')'),
				('P','+'),
				('A','*'),
				('D','.')]

	prod = [('S','LM'),
			('M','SN'),
			('N','PO'),
			('O','SR'),
			('S','LF'),
			('F','SG'),
			('G','AR'),
			('S','LH'),
			('H','SI'),
			('I','DO')]

	# Adding all letters
	# Productions of form S -> a | b | c | ... | z
	ch = "a"
	for i in range(0,26):
		unitProd.append(('S',ch))
		ch = chr(ord(ch) + 1)

	arr = [[[] for j in range(length)] for i in range(length)]

	for i in range(length):
		for production in unitProd:
			if regex[i] == production[1]:
				arr[i][i].append(production[0])
				break

	for k in range(1,length):
		for i in range(k,length):
			# at index (i,i-k)
			for j in range(i-k+1,i+1):
				for l,r in prod:
					if r[0] in arr[j-1][i-k] and r[1] in arr[i][j]:
						arr[i][i-k].append(l)

	if 'S' in arr[length-1][0]:
		return 1
	return 0