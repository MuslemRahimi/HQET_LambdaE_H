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







fig, ax = plt.subplots()

plt.ylim(0,0.2)
plt.xlim(0.20,2.0)
ax.plot(M_0, lambdaH_0, "--", color='blue',label='dim. 0')
ax.plot(M_3, lambdaH_3, "--",color='green',label='up to dim. 3')
ax.plot(M_4, lambdaH_4,"--",color='red',label='up to dim. 4')
ax.plot(M_5, lambdaH_5,color='black',label='up to dim. 5')


plt.rc('legend',fontsize=12) 
ax.legend(loc='best', shadow=True)
plt.xlabel("$M$ in GeV")
plt.ylabel("$\lambda_{H}^4 \cdot 10^{-1}$ in GeV$^4$")
plt.grid(True)
#plt.show()
plt.savefig("LambdaH_uptodim.svg")
