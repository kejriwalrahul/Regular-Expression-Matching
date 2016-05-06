# Rahul Kejriwal
# CS14B023

"""
NFA definition:

	Q = [] 								list of states(intergers)
	S = []								list of start states(integers)
	F = []								list of final states(integers)
	d = {(state, char): {states} } 	hashmap with key as state and value as a list of nextStates

	'$' stands for epsilon transitions
"""

class nfa:
	maxState = 0

	def __init__(self):
		self.Q = []
		self.S = []
		self.F = []
		self.d = {}

	#O(1) time
	def letternfa(self, ch):
		self.Q = [nfa.maxState+1, nfa.maxState+2]
		nfa.maxState += 2
		self.S = [self.Q[0]]
		self.F = [self.Q[1]]
		self.d = { 
					(self.Q[0], ch) : {self.Q[1]} 
				 }

		return self

	# O(V + SF) time
	def concat(self, nfa1, nfa2):
		self.Q = nfa1.Q + nfa2.Q
		self.S = nfa1.S
		self.F = nfa2.F

		self.d = nfa1.d.copy()
		self.d.update(nfa2.d)

		for f in nfa1.F:
			if (f, '$') not in self.d:
				self.d[(f,'$')] = set()
			for s in nfa2.S:
				# $ stands for epsilon transitions
				self.d[(f,'$')].add(s)

		return self

	# O(V) time
	def union(self, nfa1, nfa2):
		self.Q = nfa1.Q + nfa2.Q
		self.S = nfa1.S + nfa2.S
		self.F = nfa1.F + nfa2.F

		self.d = nfa1.d.copy()
		self.d.update(nfa2.d)

		return self

	# O(V) time
	def asterate(self, nfa1):
		self.Q = nfa1.Q
		newS = nfa.maxState + 1
		self.Q.append(newS)

		self.S = [newS]
		self.F = [newS]

		self.d = nfa1.d.copy()

		self.d[(newS, '$')] = set()
		for s in nfa1.S:
			self.d[(newS, '$')].add(s)

		for f in nfa1.F:
			if (f, '$') not in self.d:
				self.d[(f, '$')] = set()
			self.d[(f, '$')].add(newS)

		nfa.maxState += 1
		return self

	# O(V^3) time
	def closure(self):
		for state in self.Q:
			q = [state]
			visited = {state}
			while len(q):
				curr = q.pop()
				visited.add(curr)

				if (state,'$') not in self.d:
					self.d[(state,'$')] = set()
				
				if curr != state and curr not in self.d[(state,'$')]:
					self.d[(state,'$')].add(curr)
				
				if (curr,'$') in self.d:
					for ns in self.d[(curr,'$')]:
						if ns not in visited:
							q.append(ns)

	# O(len(x)*V^2)
	def check(self, x):
		currentStates = set(self.S)

		for ch in x:
			nextStates = set([])
			
			# Perform epsilon transitions
			for state in currentStates:
				if (state,'$') in self.d:	
					nextStates.update(self.d[(state,'$')])
			currentStates.update(nextStates)
			nextStates = set([])

			# Get next state transitions
			for state in currentStates:
				if (state, ch) in self.d:
					nextStates.update(self.d[(state, ch)])
			currentStates = nextStates

		# Perform epsilon transition
		nextStates = set([])	
		for state in currentStates:
			if (state,'$') in self.d:	
				nextStates.update(self.d[(state,'$')])
		currentStates.update(nextStates)

		if currentStates & set(self.F) != set([]):
			return 1
		else:
			return 0

	def star(self):
		return nfa().asterate(self)

	def plus(self, nfa1):
		return nfa().union(self, nfa1)

	def dot(self, nfa1):
		return nfa().concat(self, nfa1)