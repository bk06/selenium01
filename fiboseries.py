first_value=0
second_value=1
print (first_value),    ##, for printing in next line.
print (second_value),
for i in range(0,10):
	next_value=first_value+second_value
	first_value=second_value
	second_value=next_value
	print (next_value),
