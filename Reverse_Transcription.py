while True:                                           #loop to infinitly ask prompt until program is exited

	bases = input("Enter bases:")                 #ask for and input with the prompt "Enter bases:", if a string of base characters is entered make that string the variable "bases"
 
	transtable = bases.maketrans("GCAT", "CGTA")  #make a translation table and apply it to the string entered above, have this be the variable "transtable"

	print(bases.translate(transtable))            #print the translated string
