while True:


	bases = input("Enter bases:") #String of Base Characters
 
	transtable = bases.maketrans("GCAT", "CGTA") #Defining each swap

	print(bases.translate(transtable))






























	#new_bases=bases.replace("g", "c").replace("t", "a")


	#print(new_bases)


#new_bases=bases.replace("c", "g")
#new_bases=bases.replace("a", "t")
#new_bases=bases.replace("t", "a")

#, ("c", "g"), ("a", "t"), ("t", "a")


#if bases == ("A" or "a"):
#	print("T" or "t")

#elif bases == ("T" or "t"):
#	print("A")

#elif (bases == ("G" or "g")):
#	print("C")

#elif (bases == ("C" or "c")):
#	print("G")




# get the sequence from the user:

	#dna_seq = input("Please enter your sequence here: ")

# make a for loop to read the seq one nucleotide at a time and add each one in a new variable

	#compliment = ""

	#for n in dna_seq:

	  #  if n == "A":
	       # compliment = compliment + "T"
	  #  elif n == "T":
	        #compliment = compliment + "A"
	  #  elif n == "G":
	        #compliment = compliment + "C"
	  #  elif n == "C":
#	        compliment = compliment + "G"

	#print(compliment)