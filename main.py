# Rahul Kejriwal
# CS14B023

from buildnfa import build
from cyk import validCYK
# from plot import plot

regex = raw_input()

if not validCYK(regex):
	print "Wrong Expression"
else:
	M = build(regex)
	# plot(M)
	M.closure()

	n = int(raw_input())
	for i in range(n):
		string = raw_input()

		if M.check(string) == 1:
			print "Yes"
		else:
			print "No"