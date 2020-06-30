import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

lambdaH_Dim4 = pd.read_csv("lambdaH_Dim4.txt", sep = '\s+',header=None)
lambdaH_Dim4= pd.DataFrame(lambdaH_Dim4)

lambdaH_Dim5 = pd.read_csv("lambdaH_Dim5.txt", sep = '\s+',header=None)
lambdaH_Dim5= pd.DataFrame(lambdaH_Dim5)

M_values = pd.read_csv("M_values.txt", sep = '\s+',header=None)
M_values = pd.DataFrame(M_values)

print(M_values)
print(lambdaH_Dim4)

plt.yticks((0.07,0.08,0.09,0.10,0.11,0.12,0.13,0.14,0.15))
plt.plot(M_values,lambdaH_Dim5)
plt.show()

"""
with open("lambdaH_Dim4.txt") as f:
	lines= f.readlines()
	lambdaH_Dim4 = [line.split()[0] for line in lines]

with open("lambdaH_Dim5.txt") as f:
	lines= f.readlines()
	lambdaH_Dim5 = [line.split()[0] for line in lines]
with open("M_values.txt") as f:
	lines= f.readlines()
	M_values = [line.split()[0] for line in lines]




fig, ax = plt.subplots()
plt.xlabel("$M$ in GeV")
plt.ylabel("$\lambda_{H}^{2}$ in GeV^2")

ax.plot(M_values, lambdaH_Dim4, '-or', color='black',label='Theory: $<E>$')
ax.plot(M_values, lambdaH_Dim5, 'or', label='MC results')

legend = ax.legend(loc='lower right', shadow=True)
plt.grid(True)
"""


#plt.savefig("E1.png")