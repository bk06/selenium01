#n=[8, 2, 3, 4, 6]
#print "even numbers: "

#for x in n[0:5]: 
	#if x%2==0:
		#print x

	#else:	
		#print "odd numbers:"
		#print x




n=[8, 2, 3, 4, 6]
i=0
count=len(n)
while i<count:
	 
	if n[i]%2==0:
		print"the number is even: %s"%n[i]
		
	else:
		print"the number is odd: %s"%n[i]
	i+=1
	pass
	

