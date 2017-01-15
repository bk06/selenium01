'''
from __future__ import print_function ##for end function 
for c in range(0,4):
	for r in range(0,c+1):
		print ('* ',end="")    ##"foo"%bar end is used for printing side by side 
	print('')
'''

n = int(raw_input("enter the number: "))
for i in range(0,n):
	print i*"*"


for i in range(0,n):
	print " "*int(n-i-1) + int(i+1) *"*"


for i in range(0,n):
	print " "*int(n-i-1) + int(i+1) *"* "