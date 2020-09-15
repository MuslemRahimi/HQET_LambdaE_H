import re
from raw_txt import *
from Tdec_func import *
def momentum_counts(string):
	# Wir müssen das löschen oder es zählt el1*v als ein Impuls obwohl nur zwei impulse existieren
	string = string.replace("Pair[Momentum[el1], Momentum[v]]","")
	string = string.replace("Pair[Momentum[v], Momentum[el1]]","")
	string = string.replace("Pair[Momentum[el2], Momentum[v]]","")
	string = string.replace("Pair[Momentum[v], Momentum[el2]]","")
	string = string.replace("Pair[Momentum[k], Momentum[v]]","")
	string = string.replace("Pair[Momentum[v], Momentum[k]]","")
	count = string.count("el1")+string.count("el2")+string.count("k")
	return count

def Decomposition(string):
	count = momentum_counts(string)
	if count ==4:
		result = Tdec4(string)
		print("Momentum count: {}".format(count))
	if count ==3:
		result = Tdec3(string)
		print("Momentum count: {}".format(count))
	elif count == 2:
		result = Tdec2(string)
		print("Momentum count: {}".format(count))
	else:
		pass
	#print(result)
	return result



string = stringw1.strip()

if "DiracGamma[Momentum[el1]]" in string:
	string=string.replace("DiracGamma[Momentum[el1]]","GAD[x1].Pair[LorentzIndex[x1], Momentum[el1]]")

if "DiracGamma[Momentum[el2]]" in string:
	string=string.replace("DiracGamma[Momentum[el2]]","GAD[x2].Pair[LorentzIndex[x2], Momentum[el2]]")
if "DiracGamma[Momentum[k]]" in string:
	string=string.replace("DiracGamma[Momentum[k]]","GAD[x3].Pair[LorentzIndex[x3], Momentum[k]]")

string=string.rstrip()
string=string.replace(" + ","+")
string=string.replace(" - ","-")
string=string.replace("-","+-") #Kleiner Trick von mir, nicht loeschen!
string=string.split("+")
string = string[:] #Ignoriere erstes element weil empty

#print(string[1])
result = ""
print("========================")

#result =Decomposition(string[1])
#print(result)


for n,i in enumerate(string):
	result = result+"+"+Decomposition(i)
	result = result.rstrip()
	result = result.replace("+-","-")
	result = result.replace("++","+")
	result = result.rstrip()
print("Number of terms: {}".format(n+1))
print("========================")
print(result)

print("========================")