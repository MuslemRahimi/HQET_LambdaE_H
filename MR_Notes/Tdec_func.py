import re
def Tdec2(string):
	comp1 = ""
	comp2 = ""
	comp3 = ""
	comp4 = ""	
	
	string1 = string
	result = ""
	variable = ["el1","el2","k"]
	lorentzindex = ["\[Mu]","\[Nu]","\[Sigma]","\[Rho]","x1","x2","x3"]

	condition = False
	for i in variable:
		if condition == False:
			for j in variable:
				if condition == False:
					for n1 in lorentzindex:
						if condition==False:
							for n2 in lorentzindex:
								if n1 == n2:
									pass
								else:
									comp1 = i+","+n1
									comp2 = j+","+n2
									if "Pair[LorentzIndex["+n1+"], Momentum["+i+"]]" in string and \
									"Pair[LorentzIndex["+n2+"], Momentum["+j+"]]" in string:
										result = string1.replace("*Pair[LorentzIndex["+n1+"], Momentum["+i+"]]","")
										result = result.replace("*Pair[LorentzIndex[\[Mu]], Momentum["+j+"]]","")
																			
										result = result.replace("*Pair[LorentzIndex[x1], Momentum[k]]","")
										result = result.replace("*Pair[LorentzIndex[x1], Momentum[el1]]","")
										result = result.replace("*Pair[LorentzIndex[x1], Momentum[el1]]","")
										result = result.replace("*Pair[LorentzIndex[x2], Momentum[k]]","")
										result = result.replace("*Pair[LorentzIndex[x2], Momentum[el1]]","")
										result = result.replace("*Pair[LorentzIndex[x2], Momentum[el2]]","")
										result = result.replace("*Pair[LorentzIndex[x3], Momentum[k]]","")
										result = result.replace("*Pair[LorentzIndex[x3], Momentum[el1]]","")
										result = result.replace("*Pair[LorentzIndex[x3], Momentum[el2]]","")

										result = result.replace("*Pair[LorentzIndex[\[Mu]], Momentum[k]]","")
										result = result.replace("*Pair[LorentzIndex[\[Nu]], Momentum[k]]","")
										result = result.replace("*Pair[LorentzIndex[\[Rho]], Momentum[k]]","")
										result = result.replace("*Pair[LorentzIndex[\[Sigma]], Momentum[k]]","")
										result = result.replace("*Pair[LorentzIndex[\[Mu]], Momentum[el1]]","")
										result = result.replace("*Pair[LorentzIndex[\[Nu]], Momentum[el1]]","")
										result = result.replace("*Pair[LorentzIndex[\[Rho]], Momentum[el1]]","")
										result = result.replace("*Pair[LorentzIndex[\[Sigma]], Momentum[el1]]","")
										result = result.replace("*Pair[LorentzIndex[\[Mu]], Momentum[el2]]","")
										result = result.replace("*Pair[LorentzIndex[\[Nu]], Momentum[el2]]","")
										result = result.replace("*Pair[LorentzIndex[\[Rho]], Momentum[el2]]","")
										result = result.replace("*Pair[LorentzIndex[\[Sigma]], Momentum[el2]]","")
																			
										result = result+"*"+"Tdec[{{%s},{%s}},{v},List->False]" % (comp1,comp2)
										condition= True
									
									else:
										pass
							else:
								pass
								
						else:
							pass
				else:
					pass
		else:
			pass
	#print(comp1,comp2)
	return result

def Tdec3(string):
	comp1 = ""
	comp2 = ""
	comp3 = ""
	comp4 = ""
	result = ""
	string1 = string
	variable = ["el1","el2","k"]
	lorentzindex = ["\[Mu]","\[Nu]","\[Sigma]","\[Rho]","x1","x2","x3"]
	condition = False
	for i in variable:
		if condition == False:
			for j in variable:
				if condition == False:
					for k in variable:
						if condition == False:
							for n1 in lorentzindex:
								if condition == False:
									for n2 in lorentzindex:
										if condition == False:
											for n3 in lorentzindex:
												if condition == False:
													if n1 == n2 or n1 == n3 or n2==n3:
														pass
													else:
														comp1 = i+","+n1
														comp2 = j+","+n2
														comp3 = k+","+n3
															
														if "Pair[LorentzIndex["+n1+"], Momentum["+i+"]]" in string and \
															"Pair[LorentzIndex["+n2+"], Momentum["+j+"]]" in string and \
															"Pair[LorentzIndex["+n3+"], Momentum["+k+"]]" in string:
															result = string1.replace("*Pair[LorentzIndex["+n1+"], Momentum["+i+"]]","")
															result = result.replace("*Pair[LorentzIndex["+n2+"], Momentum["+j+"]]","")
															result = result.replace("*Pair[LorentzIndex["+n3+"], Momentum["+k+"]]","")
																
															result = result.replace("Pair[LorentzIndex[x1], Momentum[k]]","")
															result = result.replace("Pair[LorentzIndex[x1], Momentum[el1]]","")
															result = result.replace("Pair[LorentzIndex[x1], Momentum[el2]]","")
															result = result.replace("Pair[LorentzIndex[x2], Momentum[k]]","")
															result = result.replace("Pair[LorentzIndex[x2], Momentum[el1]]","")
															result = result.replace("Pair[LorentzIndex[x2], Momentum[el2]]","")
															result = result.replace("Pair[LorentzIndex[x3], Momentum[k]]","")
															esult = result.replace("Pair[LorentzIndex[x3], Momentum[el1]]","")
															esult = result.replace("Pair[LorentzIndex[x3], Momentum[el2]]","")
															


															result = result.replace("Pair[LorentzIndex[\[Mu]], Momentum[k]]","")
															result = result.replace("Pair[LorentzIndex[\[Nu]], Momentum[k]]","")
															result = result.replace("Pair[LorentzIndex[\[Rho]], Momentum[k]]","")
															result = result.replace("Pair[LorentzIndex[\[Sigma]], Momentum[k]]","")
															result = result.replace("Pair[LorentzIndex[\[Mu]], Momentum[el1]]","")
															result = result.replace("Pair[LorentzIndex[\[Nu]], Momentum[el1]]","")
															result = result.replace("Pair[LorentzIndex[\[Rho]], Momentum[el1]]","")
															result = result.replace("Pair[LorentzIndex[\[Sigma]], Momentum[el1]]","")
															result = result.replace("Pair[LorentzIndex[\[Mu]], Momentum[el2]]","")
															result = result.replace("Pair[LorentzIndex[\[Nu]], Momentum[el2]]","")
															result = result.replace("Pair[LorentzIndex[\[Rho]], Momentum[el2]]","")
															result = result.replace("Pair[LorentzIndex[\[Sigma]], Momentum[el2]]","")


															result = result.replace(".",".Tdec[{{%s},{%s},{%s}},{v},List->False]" % (comp1,comp2,comp3))
															condition = True
														else:
															pass
												else:
													pass
										else:
											pass
								else:
									pass
						else:
							pass
				else:
					pass
		else:
			pass
									
	return result


#=========================================================================#

def Tdec4(string):
	comp1 = ""
	comp2 = ""
	comp3 = ""
	comp4 = ""
	result = ""
	string1 = string
	variable = ["el1","el2","k"]
	lorentzindex = ["\[Mu]","\[Nu]","\[Sigma]","\[Rho]","x1","x2","x3"]
	condition = False
	for i in variable:
		if condition == False:
			for j in variable:
				if condition == False:
					for k in variable:
						if condition == False:
							for w in variable:
								if condition == False:
									for n1 in lorentzindex:
										if condition == False:
											for n2 in lorentzindex:
												if condition == False:
													for n3 in lorentzindex:
														if condition == False:
															for n4 in lorentzindex:
																if condition == False:
																	if n1 == n2 or n1 == n3 or n1==n4 \
																	or n2==n3 or n2==n4 or n3 == n4:
																		pass
																	else:
																		comp1 = i+","+n1
																		comp2 = j+","+n2
																		comp3 = k+","+n3
																		comp4 = w+","+n4
																			
																		if "Pair[LorentzIndex["+n1+"], Momentum["+i+"]]" in string and \
																			"Pair[LorentzIndex["+n2+"], Momentum["+j+"]]" in string and \
																			"Pair[LorentzIndex["+n3+"], Momentum["+k+"]]" in string and \
																			"Pair[LorentzIndex["+n4+"], Momentum["+w+"]]" in string:
																			result = string1.replace("*Pair[LorentzIndex["+n1+"], Momentum["+i+"]]","")
																			result = result.replace("*Pair[LorentzIndex["+n2+"], Momentum["+j+"]]","")
																			result = result.replace("*Pair[LorentzIndex["+n3+"], Momentum["+k+"]]","")
																			result = result.replace("*Pair[LorentzIndex["+n4+"], Momentum["+w+"]]","")
																				
																			result = result.replace("Pair[LorentzIndex[x1], Momentum[k]]","")
																			result = result.replace("Pair[LorentzIndex[x1], Momentum[el1]]","")
																			result = result.replace("Pair[LorentzIndex[x1], Momentum[el2]]","")
																			result = result.replace("Pair[LorentzIndex[x2], Momentum[k]]","")
																			result = result.replace("Pair[LorentzIndex[x2], Momentum[el1]]","")
																			result = result.replace("Pair[LorentzIndex[x2], Momentum[el2]]","")
																			result = result.replace("Pair[LorentzIndex[x3], Momentum[k]]","")
																			esult = result.replace("Pair[LorentzIndex[x3], Momentum[el1]]","")
																			esult = result.replace("Pair[LorentzIndex[x3], Momentum[el2]]","")
																			


																			result = result.replace("Pair[LorentzIndex[\[Mu]], Momentum[k]]","")
																			result = result.replace("Pair[LorentzIndex[\[Nu]], Momentum[k]]","")
																			result = result.replace("Pair[LorentzIndex[\[Rho]], Momentum[k]]","")
																			result = result.replace("Pair[LorentzIndex[\[Sigma]], Momentum[k]]","")
																			result = result.replace("Pair[LorentzIndex[\[Mu]], Momentum[el1]]","")
																			result = result.replace("Pair[LorentzIndex[\[Nu]], Momentum[el1]]","")
																			result = result.replace("Pair[LorentzIndex[\[Rho]], Momentum[el1]]","")
																			result = result.replace("Pair[LorentzIndex[\[Sigma]], Momentum[el1]]","")
																			result = result.replace("Pair[LorentzIndex[\[Mu]], Momentum[el2]]","")
																			result = result.replace("Pair[LorentzIndex[\[Nu]], Momentum[el2]]","")
																			result = result.replace("Pair[LorentzIndex[\[Rho]], Momentum[el2]]","")
																			result = result.replace("Pair[LorentzIndex[\[Sigma]], Momentum[el2]]","")

																			result = result.strip()
																			result = result.rstrip()
																			#result = result.replace(". ",".")
																			#result = result.replace(" .",".")
																			#result = result.replace("..",".")

																			#result = result.replace("..Pair",".Pair")
																			result = result.replace("*Pair",".Pair")
																			result = result.replace("*Pair[Momentum[k], Momentum[v]]",".Pair[Momentum[k], Momentum[v]]")

																			result = result+"."+"Tdec[{{%s},{%s},{%s},{%s}},{v},List->False]" % (comp1,comp2,comp3,comp4)
																			condition = True
																			
																		else:
																			pass
																else:
																	pass
														else:
															pass
												else:
													pass
										else:
											pass
								else:
									pass
						else:
							pass
				else:
					pass
		else:
			pass
									
	return result