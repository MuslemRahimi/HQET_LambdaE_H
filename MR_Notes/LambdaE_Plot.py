import matplotlib.pyplot as plt 
import numpy as np

#=========================================================#
"""

fig, ax = plt.subplots()
plt.xlabel("$E_{\\ell}^{cut}$ in GeV")
plt.ylabel("$<E>$ in GeV")
plt.xticks((0.5, 0.7,0.9, 1.1, 1.3, 1.5, 1.7))
ax.plot(x, E1, '-or', color='black',label='Theory: $<E>$')
ax.plot(x, MC1, 'or', label='MC results')
plt.fill_between(x,E1-dE1 ,E1+dE1 , color='gray',alpha=0.2)
legend = ax.legend(loc='lower right', shadow=True)
plt.grid(True)
#plt.show()
plt.savefig("E1.png")

"""
#=========================================================#

# wth for 0.85 GeV
M_085 = []
lambdaE_085 = []
with open("LambdaE_0.85.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_085.append(float(i.split()[0]))
		lambdaE_085.append(float(i.split()[1]))

M_085 = np.array(M_085)
lambdaE_085 = np.array(lambdaE_085)
#=========================================================#

# wth for 1.0 GeV
M_10 = []
lambdaE_10 = []
with open("LambdaE_1.0.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_10.append(float(i.split()[0]))
		lambdaE_10.append(float(i.split()[1]))

M_10 = np.array(M_10)
lambdaE_10 = np.array(lambdaE_10)

#=========================================================#

# wth for 1.15 GeV

M_115 = []
lambdaE_115 = []
with open("LambdaE_1.15.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_115.append(float(i.split()[0]))
		lambdaE_115.append(float(i.split()[1]))

M_115 = np.array(M_115)
lambdaE_115 = np.array(lambdaE_115)
#=========================================================#




fig, ax = plt.subplots()

plt.ylim(0.025,0.15)
plt.xlim(0.20,1.0)
ax.plot(M_085, lambdaE_085, "--", color='blue',label='$\omega_{th} = 0.85$ GeV')
ax.plot(M_10, lambdaE_10, color='black',label='$\omega_{th} = 1.0$ GeV')
ax.plot(M_115, lambdaE_115,"--",color='red',label='$\omega_{th} = 1.15$ GeV')


legend = ax.legend(loc=(0.65,0.07), shadow=True)
plt.xlabel("$M$ in GeV")
plt.ylabel("$\lambda_{E} ^2$ in GeV$^2$")
plt.grid(True)
#plt.show()
plt.savefig("LambdaE.svg")
