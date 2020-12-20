import matplotlib.pyplot as plt 
import numpy as np


#=========================================================#

# upto dim 0
M_0 = []
lambdaH_0 = []
with open("LambdaH_dim0.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_0.append(float(i.split()[0]))
		lambdaH_0.append(float(i.split()[1]))

M_0 = np.array(M_0)
lambdaH_0 = np.array(lambdaH_0)
#=========================================================#

# upto dim 3
M_3 = []
lambdaH_3 = []
with open("LambdaH_dim3.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_3.append(float(i.split()[0]))
		lambdaH_3.append(float(i.split()[1]))

M_3 = np.array(M_3)
lambdaH_3 = np.array(lambdaH_3)
#=========================================================#

# upto dim 4
M_4 = []
lambdaH_4 = []
with open("LambdaH_dim4.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_4.append(float(i.split()[0]))
		lambdaH_4.append(float(i.split()[1]))

M_4 = np.array(M_4)
lambdaH_4 = np.array(lambdaH_4)
#=========================================================#

# upto dim 5
M_5 = []
lambdaH_5 = []
with open("LambdaH_dim5.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_5.append(float(i.split()[0]))
		lambdaH_5.append(float(i.split()[1]))

M_5 = np.array(M_5)
lambdaH_5 = np.array(lambdaH_5)
#=========================================================#

# upto dim 6
M_6 = []
lambdaH_6 = []
with open("LambdaH_dim6.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_6.append(float(i.split()[0]))
		lambdaH_6.append(float(i.split()[1]))

M_6 = np.array(M_6)
lambdaH_6 = np.array(lambdaH_6)
#=========================================================#
# upto dim 7
M_7 = []
lambdaH_7 = []
with open("LambdaH_dim7.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_7.append(float(i.split()[0]))
		lambdaH_7.append(float(i.split()[1]))

M_7 = np.array(M_7)
lambdaH_7 = np.array(lambdaH_7)

#=========================================================#

M_7 = []
lambdaH_uptodim7_08 = []
with open("LambdaH_uptodim7_08.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_7.append(float(i.split()[0]))
		lambdaH_uptodim7_08.append(float(i.split()[1]))

M_7 = np.array(M_7)
lambdaH_uptodim7_08 = np.array(lambdaH_uptodim7_08)
#=========================================================#

M_7 = []
lambdaH_uptodim7_09 = []
with open("LambdaH_uptodim7_09.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_7.append(float(i.split()[0]))
		lambdaH_uptodim7_09.append(float(i.split()[1]))

M_7 = np.array(M_7)
lambdaH_uptodim7_09 = np.array(lambdaH_uptodim7_09)
#=========================================================#

M_7 = []
lambdaH_uptodim7_10 = []
with open("LambdaH_uptodim7_10.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_7.append(float(i.split()[0]))
		lambdaH_uptodim7_10.append(float(i.split()[1]))

M_7 = np.array(M_7)
lambdaH_uptodim7_10 = np.array(lambdaH_uptodim7_10)

#=========================================================#
#=========================================================#
#=========================================================#
#=========================================================#


M_0 = []
lambdaH_E_0 = []
with open("LambdaH_E_dim0.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_0.append(float(i.split()[0]))
		lambdaH_E_0.append(float(i.split()[1]))

M_0 = np.array(M_0)
lambdaH_E_0 = np.array(lambdaH_E_0)
#=========================================================#

# upto dim 5
M_5 = []
lambdaH_E_5 = []
with open("LambdaH_E_dim5.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_5.append(float(i.split()[0]))
		lambdaH_E_5.append(float(i.split()[1]))

M_5 = np.array(M_5)
lambdaH_E_5 = np.array(lambdaH_E_5)
#=========================================================#
# upto dim 7
M_7 = []
lambdaH_E_7 = []
with open("LambdaH_E_dim7.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_7.append(float(i.split()[0]))
		lambdaH_E_7.append(float(i.split()[1]))

M_7 = np.array(M_7)
lambdaH_E_7 = np.array(lambdaH_E_7)
#=========================================================#

M_7 = []
lambdaH_E_uptodim7_08 = []
with open("LambdaH_E_uptodim7_08.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_7.append(float(i.split()[0]))
		lambdaH_E_uptodim7_08.append(float(i.split()[1]))

M_7 = np.array(M_7)
lambdaH_E_uptodim7_08 = np.array(lambdaH_E_uptodim7_08)
#=========================================================#

M_7 = []
lambdaH_E_uptodim7_09 = []
with open("LambdaH_E_uptodim7_09.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_7.append(float(i.split()[0]))
		lambdaH_E_uptodim7_09.append(float(i.split()[1]))

M_7 = np.array(M_7)
lambdaH_E_uptodim7_09 = np.array(lambdaH_E_uptodim7_09)
#=========================================================#

M_7 = []
lambdaH_E_uptodim7_10 = []
with open("LambdaH_E_uptodim7_10.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_7.append(float(i.split()[0]))
		lambdaH_E_uptodim7_10.append(float(i.split()[1]))

M_7 = np.array(M_7)
lambdaH_E_uptodim7_10 = np.array(lambdaH_E_uptodim7_10)

#=========================================================#
#=========================================================#
#=========================================================#
#=========================================================#

#Lambda_E projection

M_0 = []
lambdaE_0 = []
with open("LambdaE_dim0.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_0.append(float(i.split()[0]))
		lambdaE_0.append(float(i.split()[1]))

M_0 = np.array(M_0)
lambdaE_0 = np.array(lambdaE_0)
#=========================================================#

# upto dim 3
M_3 = []
lambdaE_3 = []
with open("LambdaE_dim3.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_3.append(float(i.split()[0]))
		lambdaE_3.append(float(i.split()[1]))

M_3 = np.array(M_3)
lambdaE_3 = np.array(lambdaE_3)
#=========================================================#

# upto dim 4
M_4 = []
lambdaE_4 = []
with open("LambdaE_dim4.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_4.append(float(i.split()[0]))
		lambdaE_4.append(float(i.split()[1]))

M_4 = np.array(M_4)
lambdaE_4 = np.array(lambdaE_4)
#=========================================================#

# upto dim 5
M_5 = []
lambdaE_5 = []
with open("LambdaE_dim5.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_5.append(float(i.split()[0]))
		lambdaE_5.append(float(i.split()[1]))

M_5 = np.array(M_5)
lambdaE_5 = np.array(lambdaE_5)
#=========================================================#
# upto dim 6
M_6 = []
lambdaE_6 = []
with open("LambdaE_dim6.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_6.append(float(i.split()[0]))
		lambdaE_6.append(float(i.split()[1]))

M_6 = np.array(M_6)
lambdaE_6 = np.array(lambdaE_6)
#=========================================================#
# upto dim 7
M_7 = []
lambdaE_7 = []
with open("LambdaE_dim7.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_7.append(float(i.split()[0]))
		lambdaE_7.append(float(i.split()[1]))

M_7 = np.array(M_7)
lambdaE_7 = np.array(lambdaE_7)

M_7 = []
lambdaE_uptodim7_08 = []
with open("LambdaE_uptodim7_08.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_7.append(float(i.split()[0]))
		lambdaE_uptodim7_08.append(float(i.split()[1]))

M_7 = np.array(M_7)
lambdaE_uptodim7_08 = np.array(lambdaE_uptodim7_08)
#=========================================================#

M_7 = []
lambdaE_uptodim7_09 = []
with open("LambdaE_uptodim7_09.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_7.append(float(i.split()[0]))
		lambdaE_uptodim7_09.append(float(i.split()[1]))

M_7 = np.array(M_7)
lambdaE_uptodim7_09 = np.array(lambdaE_uptodim7_09)
#=========================================================#

M_7 = []
lambdaE_uptodim7_10 = []
with open("LambdaE_uptodim7_10.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_7.append(float(i.split()[0]))
		lambdaE_uptodim7_10.append(float(i.split()[1]))

M_7 = np.array(M_7)
lambdaE_uptodim7_10 = np.array(lambdaE_uptodim7_10)
#=========================================================#
#=========================================================#
#=========================================================#
#=========================================================#



#=========================================================#
plt.subplot(2,1,1)

plt.xlim(0.20,1.0)
plt.plot(M_7, lambdaH_E_uptodim7_08,"--",color='red',linewidth=2,label='OPE for $\omega_{th} = 0.8$ GeV')
plt.plot(M_7, lambdaH_E_uptodim7_09, color='black',linewidth=2,label='OPE for $\omega_{th} = 0.9$ GeV')
plt.plot(M_7, lambdaH_E_uptodim7_10,"--",color='blue',linewidth=2,label='OPE for $\omega_{th} = 1.0$ GeV')
plt.grid(True)
plt.ylabel("$(\lambda_{H}^{2}+\lambda_{E}^{2})^{2}$ in GeV$^4$",fontsize=12)
plt.rc('legend',fontsize=12) 
plt.yticks(np.arange(0,0.050,step=0.01))
plt.legend(loc='best', shadow=True)
plt.xlabel("$M$ in GeV",fontsize=12)
#plt.subplots_adjust(hspace=0.3)
plt.tight_layout()
fig = plt.gcf()
fig.set_size_inches(7.5, 7.5)

plt.subplot(2, 1, 2)
plt.xlim(0.20,1.0)
plt.yticks(np.arange(0,0.040,step=0.005))
plt.plot(M_0, lambdaH_E_0, "--", color='blue',linewidth=2,label='perturbative')
plt.plot(M_5, lambdaH_E_5,"--",color='purple',linewidth=2,label='dimension 5')
plt.plot(M_7, lambdaH_E_7,"--",color='black',linewidth=2,label='dimension 7')
plt.rc('legend',fontsize=12) 
plt.legend(loc='best', shadow=True)
plt.xlabel("$M$ in GeV",fontsize=12)
plt.tight_layout()
fig = plt.gcf()
#plt.yaxis.set_label_coords(-0.12, 0.6) 
plt.ylabel("$(\lambda_{H}^{2}+\lambda_{E}^{2})^{2}$ in GeV$^4$",fontsize=12)
plt.grid(True)
#plt.show()
plt.savefig("LambdaH_E_uptodim.svg")
"""
#=========================================================#

plt.subplot(2,1,1)

plt.xlim(0.20,1.0)
plt.plot(M_7, lambdaE_uptodim7_08,"--",color='red',linewidth=2,label='OPE for $\omega_{th} = 0.55$ GeV')
plt.plot(M_7, lambdaE_uptodim7_09, color='black',linewidth=2,label='OPE for $\omega_{th} = 0.60$ GeV')
plt.plot(M_7, lambdaE_uptodim7_10,"--",color='blue', linewidth=2,label='OPE for $\omega_{th} = 0.65$ GeV')
plt.grid(True)
plt.ylabel("$\lambda_{E}^{4}$ in GeV$^4$",fontsize = 12)
plt.rc('legend',fontsize=12) 
plt.legend(loc='best', shadow=True)
plt.xlabel("$M$ in GeV",fontsize=12)
plt.yticks(np.arange(0,0.020,step=0.005))
plt.tight_layout()
fig = plt.gcf()
fig.set_size_inches(7.5, 7.5)

plt.subplot(2, 1, 2)
plt.xlim(0.20,1.0)
plt.yticks(np.arange(0,0.020,step=0.005))
plt.plot(M_0, lambdaE_0, "--", color='blue',linewidth=2,label='perturbative')
plt.plot(M_3, lambdaE_3, "--",color='green',linewidth=2,label='dimension 3')
plt.plot(M_4, lambdaE_4,"--",color='red',linewidth=2,label='dimension 4')
plt.plot(M_5, lambdaE_5,"--",color='purple',linewidth=2,label='dimension 5')
plt.plot(M_6, lambdaE_6,"--",color='orange',linewidth=2,label='dimension 6')
plt.plot(M_7, lambdaE_7,"--",color='black',linewidth=2,label='dimension 7')
plt.rc('legend',fontsize=12) 
plt.legend(loc='best', shadow=True)
plt.xlabel("$M$ in GeV",fontsize=12)
plt.tight_layout()
fig = plt.gcf()
#plt.yaxis.set_label_coords(-0.12, 0.6) 
plt.ylabel("$\lambda_{E}^{4}$ in GeV$^4$",fontsize=12)
plt.grid(True)
#plt.show()
plt.savefig("LambdaE_uptodim.svg")


#=========================================================#

plt.subplot(2,1,1)

plt.xlim(0.20,1.0)
plt.plot(M_7, lambdaH_uptodim7_08,"--",linewidth=2,color='red',label='OPE for $\omega_{th} = 0.8$ GeV')
plt.plot(M_7, lambdaH_uptodim7_09, color='black',linewidth=2,label='OPE for $\omega_{th} = 0.9$ GeV')
plt.plot(M_7, lambdaH_uptodim7_10,"--",color='blue',linewidth=2,label='OPE for $\omega_{th} = 1.0$ GeV')

plt.grid(True)
plt.ylabel("$\lambda_{H}^{4}$ in GeV$^4$",fontsize=12)
plt.rc('legend',fontsize=12) 
plt.legend(loc='best', shadow=True)
plt.xlabel("$M$ in GeV",fontsize = 12)
plt.yticks(np.arange(0.01,0.030,step=0.005))
plt.tight_layout()
fig = plt.gcf()
fig.set_size_inches(7.5, 7.5)

plt.subplot(2, 1, 2)
plt.xlim(0.20,1.0)
plt.yticks(np.arange(0,0.020,step=0.005))
plt.plot(M_0, lambdaH_0, "--", color='blue',linewidth=2,label='perturbative')
plt.plot(M_3, lambdaH_3, "--",color='green',linewidth=2,label='dimension 3')
plt.plot(M_4, lambdaH_4,"--",color='red',linewidth=2,label='dimension 4')
plt.plot(M_5, lambdaH_5,"--",color='purple',linewidth=2,label='dimension 5')
plt.plot(M_6, lambdaH_6,"--",color='orange',linewidth=2,label='dimension 6')
plt.plot(M_7, lambdaH_7,"--",color='black',linewidth=2,label='dimension 7')
plt.rc('legend',fontsize=12) 
plt.legend(loc='best', shadow=True)
plt.xlabel("$M$ in GeV",fontsize = 12)
plt.tight_layout()
fig = plt.gcf()
plt.ylabel("$\lambda_{H}^{4}$ in GeV$^4$",fontsize = 12)
plt.grid(True)
#plt.show()
plt.savefig("LambdaH_uptodim.svg")
"""