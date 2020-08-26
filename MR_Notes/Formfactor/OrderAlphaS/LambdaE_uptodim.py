import matplotlib.pyplot as plt 
import numpy as np


#=========================================================#

# upto dim 0
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







fig, ax = plt.subplots()

plt.ylim(-0.15,0.15)
plt.xlim(0.20,2.0)
ax.plot(M_0, lambdaE_0, "--", color='blue',label='dim. 0')
ax.plot(M_3, lambdaE_3, "--",color='green',label='up to dim. 3')
ax.plot(M_4, lambdaE_4,"--",color='red',label='up to dim. 4')
ax.plot(M_5, lambdaE_5,color='black',label='up to dim. 5')


plt.rc('legend',fontsize=12) 
ax.legend(loc='best', shadow=True)
plt.xlabel("$M$ in GeV")
plt.ylabel("$\lambda_{E}^{4} \cdot 10^{-1}$ in GeV$^4$")
plt.grid(True)
#plt.show()
plt.savefig("LambdaE_uptodim.svg")
