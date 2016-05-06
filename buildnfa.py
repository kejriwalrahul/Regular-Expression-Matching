# Rahul Kejriwal
# CS14B023

from nfa import nfa

def build(regex):
	stack = []

	for char in regex:
		if char == '(':
			stack.append('(')
		elif ord(char) >= 97 and ord(char) <= 122:
			stack.append(char)
		elif char == '+' or char == '.' or char == '*':
			stack.append(char)
		elif char == ')':
			temp = stack.pop()

			if temp == '*':
				temp = stack.pop()
				if type(temp) == str:
					temp = nfa().letternfa(temp)
				
				stack.pop()
				stack.append(temp.star())
			else:
				right = temp
				op = stack.pop()
				left = stack.pop()
				
				if type(right) == str:
					right = nfa().letternfa(right)
				if type(left) == str:
					left = nfa().letternfa(left)

				stack.pop()
				if op == '+':
					stack.append(left.plus(right))
				elif op == '.':
					stack.append(left.dot(right))
		else:
			print "Error"
			return

	return stack[0]