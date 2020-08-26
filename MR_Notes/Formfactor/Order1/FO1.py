import matplotlib.pyplot as plt 
import numpy as np


#Without RGE improved, F with order 1 is defined 
#in Nishikawa & Tanaka paper
# wth for 0.6 GeV
M_06 = []
FO1_06 = []
with open("FO1_06.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_06.append(float(i.split()[0]))
		FO1_06.append(float(i.split()[1]))

M_06 = np.array(M_06)
FO1_06 = np.array(FO1_06)
#=========================================================#

# wth for 0.7 GeV
M_07 = []
FO1_07 = []
with open("FO1_07.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_07.append(float(i.split()[0]))
		FO1_07.append(float(i.split()[1]))

M_07 = np.array(M_07)
FO1_07 = np.array(FO1_07)

#=========================================================#

# wth for 0.8 GeV
M_08 = []
FO1_08 = []
with open("FO1_08.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_08.append(float(i.split()[0]))
		FO1_08.append(float(i.split()[1]))

M_08 = np.array(M_08)
FO1_08 = np.array(FO1_08)
#=========================================================#

# wth for 0.9 GeV
M_09 = []
FO1_09 = []
with open("FO1_09.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_09.append(float(i.split()[0]))
		FO1_09.append(float(i.split()[1]))

M_09 = np.array(M_09)
FO1_09 = np.array(FO1_09)
#=========================================================#

# wth for 1.0 GeV
M_10 = []
FO1_10 = []
with open("FO1_10.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_10.append(float(i.split()[0]))
		FO1_10.append(float(i.split()[1]))

M_10 = np.array(M_10)
FO1_10 = np.array(FO1_10)
#=========================================================#



fig, ax = plt.subplots()

plt.ylim(0.2,0.5)
plt.xlim(0.20,1.0)
ax.plot(M_06, FO1_06, color='blue',label='$\omega_{th} = 0.9$ GeV')
ax.plot(M_07, FO1_07, color='orange',label='$\omega_{th} = 1.0$ GeV')
ax.plot(M_08, FO1_08,color='purple',label='$\omega_{th} = 1.1$ GeV')
ax.plot(M_09, FO1_09,color='black',label='$\omega_{th} = 1.2$ GeV')
ax.plot(M_10, FO1_10,color='red',label='$\omega_{th} = 1.3$ GeV')



#stability window
#=================#
#plt.axvline(0.4,0,1,color="black",linewidth=1.2,linestyle="--")
#plt.axvline(0.6,0,1,color="black",linewidth=1.2,linestyle="--")
#==================#

legend = ax.legend(loc= 'best', shadow=True)
plt.xlabel("$M$ in GeV")
plt.ylabel("$F$ in GeV$^{3/2}$")
plt.grid(True)
#plt.show()
plt.savefig("FO1.svg")
