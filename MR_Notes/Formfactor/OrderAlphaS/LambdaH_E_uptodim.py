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


#=========================================================#
fig, ax = plt.subplots()

plt.xlim(0.20,1.0)
ax.plot(M_0, lambdaH_0, "--", color='blue',label='perturbative')
ax.plot(M_3, lambdaH_3, "--",color='green',label='dimension 3')
ax.plot(M_4, lambdaH_4,"--",color='red',label='dimension 4')
ax.plot(M_5, lambdaH_5,"--",color='purple',label='dimension 5')
ax.plot(M_6, lambdaH_6,"--",color='orange',label='dimension 6')
ax.plot(M_7, lambdaH_7,color='black',label='dimension 7')


plt.rc('legend',fontsize=12) 
ax.legend(loc='best', shadow=True)
plt.xlabel("$M$ in GeV")
plt.ylabel("$\lambda_{H}^4$ in GeV$^4$")
plt.grid(True)
#plt.show()
plt.savefig("LambdaH_uptodim.svg")

#=========================================================#
fig, ax = plt.subplots()

plt.xlim(0.20,1.0)
ax.plot(M_0, lambdaH_E_0, "--", color='blue',label='perturbative')
#ax.plot(M_3, lambdaH_E_3, "--",color='green',label='up to dim. 3')
#ax.plot(M_4, lambdaH_E_4,"--",color='red',label='up to dim. 4')
ax.plot(M_5, lambdaH_E_5,"--",color='purple',label='dimension 3')
#ax.plot(M_6, lambdaH_E_6,"--",color='orange',label='up to dim. 6')
ax.plot(M_7, lambdaH_E_7,color='black',label='dimension 7')


plt.rc('legend',fontsize=12) 
ax.legend(loc='best', shadow=True)
plt.xlabel("$M$ in GeV")
plt.ylabel("$(\lambda_{H}^{2}+\lambda_{E}^{2})^{2}$ in GeV$^4$")
plt.grid(True)
#plt.show()
plt.savefig("LambdaH_E_uptodim.svg")


#=========================================================#
fig, ax = plt.subplots()

plt.xlim(0.20,1.0)
ax.plot(M_0, lambdaE_0, "--", color='blue',label='perturbative')
ax.plot(M_3, lambdaE_3, "--",color='green',label='dimension 3')
ax.plot(M_4, lambdaE_4,"--",color='red',label='dimension 4')
ax.plot(M_5, lambdaE_5,"--",color='purple',label='dimension 5')
ax.plot(M_6, lambdaE_6,"--",color='orange',label='dimension 6')
ax.plot(M_7, lambdaE_7,color='black',label='dimension 7')


plt.rc('legend',fontsize=12) 
ax.legend(loc='best', shadow=True)
plt.xlabel("$M$ in GeV")
ax.yaxis.set_label_coords(-0.12, 0.6) 
plt.ylabel("$\lambda_{E}^{4}$ in GeV$^4$")
plt.grid(True)
#plt.show()
plt.savefig("LambdaE_uptodim.svg")
