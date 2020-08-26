import matplotlib.pyplot as plt 
import numpy as np


#Without RGE improved, F with O1 order is defined 
#in Nishikawa & Tanaka paper, Eq. (71)
# wth for 0.6 GeV
M_06 = []
fBO1_06 = []
with open("fBO1_06.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_06.append(float(i.split()[0]))
		fBO1_06.append(float(i.split()[1]))

M_06 = np.array(M_06)
fBO1_06 = np.array(fBO1_06)
#=========================================================#

# wth for 0.7 GeV
M_07 = []
fBO1_07 = []
with open("fBO1_07.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_07.append(float(i.split()[0]))
		fBO1_07.append(float(i.split()[1]))

M_07 = np.array(M_07)
fBO1_07 = np.array(fBO1_07)

#=========================================================#

# wth for 0.8 GeV
M_08 = []
fBO1_08 = []
with open("fBO1_08.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_08.append(float(i.split()[0]))
		fBO1_08.append(float(i.split()[1]))

M_08 = np.array(M_08)
fBO1_08 = np.array(fBO1_08)
#=========================================================#

# wth for 0.9 GeV
M_09 = []
fBO1_09 = []
with open("fBO1_09.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_09.append(float(i.split()[0]))
		fBO1_09.append(float(i.split()[1]))

M_09 = np.array(M_09)
fBO1_09 = np.array(fBO1_09)
#=========================================================#

# wth for 1.0 GeV
M_10 = []
fBO1_10 = []
with open("fBO1_10.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_10.append(float(i.split()[0]))
		fBO1_10.append(float(i.split()[1]))

M_10 = np.array(M_10)
fBO1_10 = np.array(fBO1_10)
#=========================================================#



fig, ax = plt.subplots()

plt.ylim(0.1,0.3)
plt.xlim(0.20,1.0)
ax.plot(M_06, fBO1_06, color='blue',label='$\omega_{th} = 0.9$ GeV')
ax.plot(M_07, fBO1_07, color='orange',label='$\omega_{th} = 1.0$ GeV')
ax.plot(M_08, fBO1_08,color='purple',label='$\omega_{th} = 1.1$ GeV')
ax.plot(M_09, fBO1_09,color='black',label='$\omega_{th} = 1.2$ GeV')
ax.plot(M_10, fBO1_10,color='red',label='$\omega_{th} = 1.3$ GeV')



#fB lattice QCD result
#=================#
#plt.axvline(0.4,0,1,color="black",linewidth=1.2,linestyle="--")
fB= 0.1920
dfB= 0.0046
ax.hlines(0.1920, 0, 1, colors='black', linestyles='--', label='')
ax.axhspan(fB-dfB, fB+dfB, facecolor="green",alpha=0.5)
#==================#

legend = ax.legend(loc= 'upper left', shadow=True)
plt.xlabel("$M$ in GeV")
plt.ylabel("$f_{B}$ in GeV")
plt.grid(True)
#plt.show()
plt.savefig("fBO1.svg")
