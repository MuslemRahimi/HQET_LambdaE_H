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
									if "Pair[LorentzIndex["+n1+", D], Momentum["+i+", D]]" in string and \
									"Pair[LorentzIndex["+n2+", D], Momentum["+j+", D]]" in string:
										result = string1.replace("Pair[LorentzIndex["+n1+", D], Momentum["+i+", D]]","")
										result = result.replace("Pair[LorentzIndex[\[Mu], D], Momentum["+j+", D]]","")
																			
										result = result.replace("Pair[LorentzIndex[x1, D], Momentum[k, D]]","")
										result = result.replace("Pair[LorentzIndex[x1, D], Momentum[el1, D]]","")
										result = result.replace("Pair[LorentzIndex[x1, D], Momentum[el1, D]]","")
										result = result.replace("Pair[LorentzIndex[x2, D], Momentum[k, D]]","")
										result = result.replace("Pair[LorentzIndex[x2, D], Momentum[el1, D]]","")
										result = result.replace("Pair[LorentzIndex[x2, D], Momentum[el2, D]]","")
										result = result.replace("Pair[LorentzIndex[x3, D], Momentum[k, D]]","")
										result = result.replace("Pair[LorentzIndex[x3, D], Momentum[el1, D]]","")
										result = result.replace("Pair[LorentzIndex[x3, D], Momentum[el2, D]]","")

										result = result.replace("Pair[LorentzIndex[\[Mu], D], Momentum[k, D]]","")
										result = result.replace("Pair[LorentzIndex[\[Nu], D], Momentum[k, D]]","")
										result = result.replace("Pair[LorentzIndex[\[Rho], D], Momentum[k, D]]","")
										result = result.replace("Pair[LorentzIndex[\[Sigma], D], Momentum[k, D]]","")
										result = result.replace("Pair[LorentzIndex[\[Mu], D], Momentum[el1, D]]","")
										result = result.replace("Pair[LorentzIndex[\[Nu], D], Momentum[el1, D]]","")
										result = result.replace("Pair[LorentzIndex[\[Rho], D], Momentum[el1, D]]","")
										result = result.replace("Pair[LorentzIndex[\[Sigma], D], Momentum[el1, D]]","")
										result = result.replace("Pair[LorentzIndex[\[Mu], D], Momentum[el2, D]]","")
										result = result.replace("Pair[LorentzIndex[\[Nu], D], Momentum[el2, D]]","")
										result = result.replace("Pair[LorentzIndex[\[Rho], D], Momentum[el2, D]]","")
										result = result.replace("Pair[LorentzIndex[\[Sigma], D], Momentum[el2, D]]","")
																			
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

	return result


#=====================================================================================================================================#

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
															
														if "Pair[LorentzIndex["+n1+", D], Momentum["+i+", D]]" in string and \
															"Pair[LorentzIndex["+n2+", D], Momentum["+j+", D]]" in string and \
															"Pair[LorentzIndex["+n3+", D], Momentum["+k+", D]]" in string:
															result = string1.replace("Pair[LorentzIndex["+n1+", D], Momentum["+i+", D]]","")
															result = result.replace("Pair[LorentzIndex["+n2+", D], Momentum["+j+", D]]","")
															result = result.replace("Pair[LorentzIndex["+n3+", D], Momentum["+k+", D]]","")
																
															result = result.replace("Pair[LorentzIndex[x1, D], Momentum[k, D]]","")
															result = result.replace("Pair[LorentzIndex[x1, D], Momentum[el1, D]]","")
															result = result.replace("Pair[LorentzIndex[x1, D], Momentum[el1, D]]","")
															result = result.replace("Pair[LorentzIndex[x2, D], Momentum[k, D]]","")
															result = result.replace("Pair[LorentzIndex[x2, D], Momentum[el1, D]]","")
															result = result.replace("Pair[LorentzIndex[x2, D], Momentum[el2, D]]","")
															result = result.replace("Pair[LorentzIndex[x3, D], Momentum[k, D]]","")
															result = result.replace("Pair[LorentzIndex[x3, D], Momentum[el1, D]]","")
															result = result.replace("Pair[LorentzIndex[x3, D], Momentum[el2, D]]","")

															result = result.replace("Pair[LorentzIndex[x1, D], Momentum[el1, D]]","")

															result = result.replace("Pair[LorentzIndex[\[Mu], D], Momentum[k, D]]","")
															result = result.replace("Pair[LorentzIndex[\[Nu], D], Momentum[k, D]]","")
															result = result.replace("Pair[LorentzIndex[\[Rho], D], Momentum[k, D]]","")
															result = result.replace("Pair[LorentzIndex[\[Sigma], D], Momentum[k, D]]","")
															result = result.replace("Pair[LorentzIndex[\[Mu], D], Momentum[el1, D]]","")
															result = result.replace("Pair[LorentzIndex[\[Nu], D], Momentum[el1, D]]","")
															result = result.replace("Pair[LorentzIndex[\[Rho], D], Momentum[el1, D]]","")
															result = result.replace("Pair[LorentzIndex[\[Sigma], D], Momentum[el1, D]]","")
															result = result.replace("Pair[LorentzIndex[\[Mu], D], Momentum[el2, D]]","")
															result = result.replace("Pair[LorentzIndex[\[Nu], D], Momentum[el2, D]]","")
															result = result.replace("Pair[LorentzIndex[\[Rho], D], Momentum[el2, D]]","")
															result = result.replace("Pair[LorentzIndex[\[Sigma], D], Momentum[el2, D]]","")


															result = result+"*"+"Tdec[{{%s},{%s},{%s}},{v},List->False]" % (comp1,comp2,comp3)
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
																			
																		if "Pair[LorentzIndex["+n1+", D], Momentum["+i+", D]]" in string and \
																			"Pair[LorentzIndex["+n2+", D], Momentum["+j+", D]]" in string and \
																			"Pair[LorentzIndex["+n3+", D], Momentum["+k+", D]]" in string and \
																			"Pair[LorentzIndex["+n4+", D], Momentum["+w+", D]]" in string:
																			result = string1.replace("Pair[LorentzIndex["+n1+", D], Momentum["+i+", D]]","")
																			result = result.replace("Pair[LorentzIndex["+n2+", D], Momentum["+j+", D]]","")
																			result = result.replace("Pair[LorentzIndex["+n3+", D], Momentum["+k+", D]]","")
																			result = result.replace("Pair[LorentzIndex["+n4+", D], Momentum["+w+", D]]","")
																				
																			result = result.replace("Pair[LorentzIndex[x1, D], Momentum[k, D]]","")
																			result = result.replace("Pair[LorentzIndex[x1, D], Momentum[el1, D]]","")
																			result = result.replace("Pair[LorentzIndex[x1, D], Momentum[el2, D]]","")
																			result = result.replace("Pair[LorentzIndex[x2, D], Momentum[k, D]]","")
																			result = result.replace("Pair[LorentzIndex[x2, D], Momentum[el1, D]]","")
																			result = result.replace("Pair[LorentzIndex[x2, D], Momentum[el2, D]]","")
																			result = result.replace("Pair[LorentzIndex[x3, D], Momentum[k, D]]","")
																			result = result.replace("Pair[LorentzIndex[x3, D], Momentum[el1, D]]","")
																			result = result.replace("Pair[LorentzIndex[x3, D], Momentum[el2, D]]","")
																			


																			result = result.replace("Pair[LorentzIndex[\[Mu], D], Momentum[k, D]]","")
																			result = result.replace("Pair[LorentzIndex[\[Nu], D], Momentum[k, D]]","")
																			result = result.replace("Pair[LorentzIndex[\[Rho], D], Momentum[k, D]]","")
																			result = result.replace("Pair[LorentzIndex[\[Sigma], D], Momentum[k, D]]","")
																			result = result.replace("Pair[LorentzIndex[\[Mu], D], Momentum[el1, D]]","")
																			result = result.replace("Pair[LorentzIndex[\[Nu], D], Momentum[el1, D]]","")
																			result = result.replace("Pair[LorentzIndex[\[Rho], D], Momentum[el1, D]]","")
																			result = result.replace("Pair[LorentzIndex[\[Sigma], D], Momentum[el1, D]]","")
																			result = result.replace("Pair[LorentzIndex[\[Mu], D], Momentum[el2, D]]","")
																			result = result.replace("Pair[LorentzIndex[\[Nu], D], Momentum[el2, D]]","")
																			result = result.replace("Pair[LorentzIndex[\[Rho], D], Momentum[el2, D]]","")
																			result = result.replace("Pair[LorentzIndex[\[Sigma], D], Momentum[el2, D]]","")



																			result = result+"*"+"Tdec[{{%s},{%s},{%s},{%s}},{v},List->False]" % (comp1,comp2,comp3,comp4)
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


#=====================================================================================================================================#


def Tdec5(string):
	comp1 = ""
	comp2 = ""
	comp3 = ""
	comp4 = ""
	comp5 = ""
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
									for y in variable:
										if condition == False:
											for n1 in lorentzindex:
												if condition == False:
													for n2 in lorentzindex:
														if condition == False:
															for n3 in lorentzindex:
																if condition == False:
																	for n4 in lorentzindex:
																		if condition == False:
																			for n5 in lorentzindex:
																				if condition == False:
																					if n1 == n2 or n1 == n3 or n1==n4 or n1 ==n5 \
																					or n2==n3 or n2==n4 or n2==n5 or n3==n4 \
																					or n3==n5 or n4==n5:
																						pass
																					else:
																						comp1 = i+","+n1
																						comp2 = j+","+n2
																						comp3 = k+","+n3
																						comp4 = w+","+n4
																						comp5 = y+","+n5
																							
																						if "Pair[LorentzIndex["+n1+", D], Momentum["+i+", D]]" in string and \
																							"Pair[LorentzIndex["+n2+", D], Momentum["+j+", D]]" in string and \
																							"Pair[LorentzIndex["+n3+", D], Momentum["+k+", D]]" in string and \
																							"Pair[LorentzIndex["+n4+", D], Momentum["+w+", D]]" in string and \
																							"Pair[LorentzIndex["+n5+", D], Momentum["+y+", D]]" in string:
																							result = string1.replace("Pair[LorentzIndex["+n1+", D], Momentum["+i+", D]]","")
																							result = result.replace("Pair[LorentzIndex["+n2+", D], Momentum["+j+", D]]","")
																							result = result.replace("Pair[LorentzIndex["+n3+", D], Momentum["+k+", D]]","")
																							result = result.replace("Pair[LorentzIndex["+n4+", D], Momentum["+w+", D]]","")
																							result = result.replace("Pair[LorentzIndex["+n5+", D], Momentum["+y+", D]]","")
																								
																							result = result.replace("Pair[LorentzIndex[x1, D], Momentum[k, D]]","")
																							result = result.replace("Pair[LorentzIndex[x1, D], Momentum[el1, D]]","")
																							result = result.replace("Pair[LorentzIndex[x1, D], Momentum[el2, D]]","")
																							result = result.replace("Pair[LorentzIndex[x2, D], Momentum[k, D]]","")
																							result = result.replace("Pair[LorentzIndex[x2, D], Momentum[el1, D]]","")
																							result = result.replace("Pair[LorentzIndex[x2, D], Momentum[el2, D]]","")
																							result = result.replace("Pair[LorentzIndex[x3, D], Momentum[k, D]]","")
																							result = result.replace("Pair[LorentzIndex[x3, D], Momentum[el1, D]]","")
																							result = result.replace("Pair[LorentzIndex[x3, D], Momentum[el2, D]]","")
																							


																							result = result.replace("Pair[LorentzIndex[\[Mu], D], Momentum[k, D]]","")
																							result = result.replace("Pair[LorentzIndex[\[Nu], D], Momentum[k, D]]","")
																							result = result.replace("Pair[LorentzIndex[\[Rho], D], Momentum[k, D]]","")
																							result = result.replace("Pair[LorentzIndex[\[Sigma], D], Momentum[k, D]]","")
																							result = result.replace("Pair[LorentzIndex[\[Mu], D], Momentum[el1, D]]","")
																							result = result.replace("Pair[LorentzIndex[\[Nu], D], Momentum[el1, D]]","")
																							result = result.replace("Pair[LorentzIndex[\[Rho], D], Momentum[el1, D]]","")
																							result = result.replace("Pair[LorentzIndex[\[Sigma], D], Momentum[el1, D]]","")
																							result = result.replace("Pair[LorentzIndex[\[Mu], D], Momentum[el2, D]]","")
																							result = result.replace("Pair[LorentzIndex[\[Nu], D], Momentum[el2, D]]","")
																							result = result.replace("Pair[LorentzIndex[\[Rho], D], Momentum[el2, D]]","")
																							result = result.replace("Pair[LorentzIndex[\[Sigma], D], Momentum[el2, D]]","")



																							result = result+"*"+"Tdec[{{%s},{%s},{%s},{%s},{%s}},{v},List->False]" % (comp1,comp2,comp3,comp4,comp5)
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
				else:
					pass
		else:
			pass
									
	return result