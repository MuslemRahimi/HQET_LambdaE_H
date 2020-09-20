from raw_txt import *
import os
import time
def Denrule(string):
	result = string
	a1 = 0
	a2 = 0
	a3 = 0
	a4 = 0
	a5 = 0
	a6 = 0
	a7 = 0
	a8 = 0
	a9 = 0
	for i in range(990,1011):
		if "Den1[vk]^%s" % (i) in string:
			result = result.replace("Den1[vk]^%s" %(i),"")
			a1 = i - 1000
		if "Den2[el1]^%s" % (i) in string:
			result = result.replace("Den2[el1]^%s" %(i),"")
			a2 = i -1000
		if "Den3[el2]^%s" % (i) in string:
			result = result.replace("Den3[el2]^%s" %(i),"")
			a3 = i -1000
		if "Den4[el1 + k - v*\[Omega]]^%s" % (i) in string:
			result = result.replace("Den4[el1 + k - v*\[Omega]]^%s" %(i),"")
			a4 = i -1000
		if "Den5[el1 + el2 + k - v*\[Omega]]^%s" % (i) in string:
			result = result.replace("Den5[el1 + el2 + k - v*\[Omega]]^%s" %(i),"")
			a5 = i -1000
		if "Den6[el1el2]^%s" % (i) in string:
			result = result.replace("Den6[el1el2]^%s" %(i),"")
			a6 = 1000 - i
		if "Den7[kel1]^%s" % (i) in string:
			result = result.replace("Den7[kel1]^%s" %(i),"")
			a7 = 1000 - i
		if "Den8[kel2]^%s" % (i) in string:
			result = result.replace("Den8[kel2]^%s" %(i),"")
			a8 = 1000 - i
		if "Den9[vel1]^%s" % (i) in string:
			result = result.replace("Den9[vel1]^%s" %(i),"")
			a9 = 1000 - i
	result = result+"*"+"j[MI,%s,%s,%s,%s,%s,%s,%s,%s,%s]" % (a1,a2,a3,a4,a5,a6,a7,a8,a9)
	result = result.replace(" . ",".")
	result = result.replace("*","")
	result = result.replace("\[Omega]","\[Omega] ")
	result = result.replace("DDirac"," D Dirac")
	result = result.replace("j[MI,0,0,0,0,0,0,0,0,0]","")
	return result

if __name__=='__main__':
	stringDen=stringDen.replace("/((1 - D)\[Omega] )","/((1 - D)\[Omega] )$")
	stringDen=stringDen.replace("/(1 - D)","/(1 - D)$")
	stringDen=stringDen.replace("/((1 - D^2)\[Omega] )","/((1 - D^2)\[Omega] )$")
	stringDen=stringDen.replace("/(1 - D^2)","/(1 - D^2)$")
	# Trick um es in N terme zu splitten
	#stringDen = stringDen.replace("D)*\[Omega]","D)*\[Omega])+")
	stringDen = stringDen.split("$")
	result = ""
	for string in stringDen:
		#stringe = string+")"
		result = result+Denrule(string)

	result = result.split()
	try:
		os.remove("Denrule.txt")
	except:
		pass
	open('Denrule.txt', 'a+').write(' '.join([str(i) for i in result]) + '\n')
	