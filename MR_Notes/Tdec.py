import re
from raw_txt import *
import os
from Tdec_func import *
import time
def momentum_counts(string):
	# Wir müssen das löschen oder es zählt el1*v als ein Impuls obwohl nur zwei impulse existieren
	string = string.replace("Pair[Momentum[el1, D], Momentum[v, D]]","")
	string = string.replace("Pair[Momentum[v, D], Momentum[el1, D]]","")
	string = string.replace("Pair[Momentum[el2, D], Momentum[v, D]]","")
	string = string.replace("Pair[Momentum[v, D], Momentum[el2, D]]","")
	string = string.replace("Pair[Momentum[k, D], Momentum[v, D]]","")
	string = string.replace("Pair[Momentum[v, D], Momentum[k, D]]","")
	#==============Scalar product of momentum itself==================#
	string = string.replace("Pair[Momentum[k, D], Momentum[k, D]]","")
	string = string.replace("Pair[Momentum[el1, D], Momentum[el1, D]]","")
	string = string.replace("Pair[Momentum[el2, D], Momentum[el2, D]]","")
	count = string.count("el1")+string.count("el2")+string.count("k")
	return count

def Decomposition(string):
	count = momentum_counts(string)
	if count == 5:
		result = Tdec5(string)
		print("Momentum count: {}".format(count))
	elif count == 4:
		result = Tdec4(string)
		print("Momentum count: {}".format(count))
	elif count == 3:
		result = Tdec3(string)
		print("Momentum count: {}".format(count))
	elif count == 2:
		result = Tdec2(string)
		print("Momentum count: {}".format(count))
	elif count == 1:
		print("Not implemented yet!")
		print("Momentum count: {}".format(count))
	else:
		print("Momentum count: {}".format(0))
	
	#print(result)
	return result




def main(string):
	try: 
		os.remove("Tdec.txt")
	except:
		pass

	result = ""
	#print("========================")
	NumberOfTerms = 0
	for n,i in enumerate(string):
		result = result+"+"+Decomposition(i)
		
		result = result.rstrip()
		result = result.replace("+-","-")
		result = result.replace("++","+")
		result = result.rstrip()
		result = result.replace("**",".")
		result = result.replace(".*",".")
		result = result.replace("*.",".")
		result = result.replace("....",".")
		result = result.replace("...",".")
		result = result.replace("..",".")
		result = result.replace(". . ",".")
		result = result.replace(" . ",".")
	NumberOfTerms = n
	#Das ist um das plus ganz am Anfang wegzubekommen
	if result[0] == "+":
		result = result[1:]
	#print(result)
		
	result = result.split()
	open('Tdec.txt', 'a+').write(' '.join([str(i) for i in result]) + '\n')
	return result, NumberOfTerms

if __name__=='__main__':
	string = stringw0.strip()

	if "DiracGamma[Momentum[el1, D], D]" in string:
		string=string.replace("DiracGamma[Momentum[el1, D], D]","GAD[x1].Pair[LorentzIndex[x1, D], Momentum[el1, D]]")
	if "DiracGamma[Momentum[el2, D], D]" in string:
		string=string.replace("DiracGamma[Momentum[el2, D], D]","GAD[x2].Pair[LorentzIndex[x2, D], Momentum[el2, D]]")
	if "DiracGamma[Momentum[k, D], D]" in string:
		string=string.replace("DiracGamma[Momentum[k, D], D]","GAD[x3].Pair[LorentzIndex[x3, D], Momentum[k, D]]")


	string=string.rstrip()
	string=string.replace(" + ","+")
	string=string.replace(" - ","-")
	string=string.replace("-","+-") #Kleiner Trick von mir, nicht loeschen!
	string=string.split("+")


	try:
		result, NumberOfTerms = main(string[:])
		print("========================")
		print("Number of terms: {}".format(NumberOfTerms+1))
		print("========================")
		result = " ".join([str(i) for i in result])
		print(result.count("False"))
	except:
		print("We try string[1:] but be careful!")
		result,NumberOfTerms = main(string[1:])
		print("========================")
		print("Number of terms: {}".format(NumberOfTerms+1))
		print("========================")
		result = " ".join([str(i) for i in result])
		print(result.count("False"))
		#print(result)