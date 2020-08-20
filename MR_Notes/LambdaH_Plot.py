import matplotlib.pyplot as plt 
import numpy as np


#=========================================================#

# wth for 0.85 GeV
M_085 = []
lambdaH_085 = []
with open("LambdaH_0.85.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_085.append(float(i.split()[0]))
		lambdaH_085.append(float(i.split()[1]))

M_085 = np.array(M_085)
lambdaH_085 = np.array(lambdaH_085)
#=========================================================#

# wth for 1.0 GeV
M_10 = []
lambdaH_10 = []
with open("LambdaH_1.0.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_10.append(float(i.split()[0]))
		lambdaH_10.append(float(i.split()[1]))

M_10 = np.array(M_10)
lambdaH_10 = np.array(lambdaH_10)

#=========================================================#

# wth for 1.15 GeV

M_115 = []
lambdaH_115 = []
with open("LambdaH_1.15.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_115.append(float(i.split()[0]))
		lambdaH_115.append(float(i.split()[1]))

M_115 = np.array(M_115)
lambdaH_115 = np.array(lambdaH_115)
#=========================================================#




fig, ax = plt.subplots()

plt.ylim(0.025,0.15)
plt.xlim(0.20,1.0)
ax.plot(M_085, lambdaH_085, "--", color='blue',label='$\omega_{th} = 1.0$ GeV')
ax.plot(M_10, lambdaH_10, color='black',label='$\omega_{th} = 1.1$ GeV')
ax.plot(M_115, lambdaH_115,"--",color='red',label='$\omega_{th} = 1.2$ GeV')

#stability window
#=================#
plt.axvline(0.4,0,1,color="black",linewidth=1.2,linestyle="--")
plt.axvline(0.6,0,1,color="black",linewidth=1.2,linestyle="--")
#==================#

legend = ax.legend(loc=(0.65,0.07), shadow=True)
plt.xlabel("$M$ in GeV")
plt.ylabel("$\lambda_{H} ^2$ in GeV$^2$")
plt.grid(True)
#plt.show()
plt.savefig("LambdaH.svg")
