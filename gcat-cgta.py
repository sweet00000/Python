while True:

	bases = input("Enter bases:") #string of base characters
 
	transtable = bases.maketrans("GCAT", "CGTA") #defining each character swap

	print(bases.translate(transtable))
