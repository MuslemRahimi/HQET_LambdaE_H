import matplotlib.pyplot as plt 
import numpy as np


#Without RGE improved, F with alphaS order is defined 
#in Nishikawa & Tanaka paper, Eq. (71)
# wth for 0.6 GeV
M_06 = []
FalphaS_06 = []
with open("FalphaS_06.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_06.append(float(i.split()[0]))
		FalphaS_06.append(float(i.split()[1]))

M_06 = np.array(M_06)
FalphaS_06 = np.array(FalphaS_06)
#=========================================================#

# wth for 0.7 GeV
M_07 = []
FalphaS_07 = []
with open("FalphaS_07.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_07.append(float(i.split()[0]))
		FalphaS_07.append(float(i.split()[1]))

M_07 = np.array(M_07)
FalphaS_07 = np.array(FalphaS_07)

#=========================================================#

# wth for 0.8 GeV
M_08 = []
FalphaS_08 = []
with open("FalphaS_08.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_08.append(float(i.split()[0]))
		FalphaS_08.append(float(i.split()[1]))

M_08 = np.array(M_08)
FalphaS_08 = np.array(FalphaS_08)
#=========================================================#

# wth for 0.9 GeV
M_09 = []
FalphaS_09 = []
with open("FalphaS_09.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_09.append(float(i.split()[0]))
		FalphaS_09.append(float(i.split()[1]))

M_09 = np.array(M_09)
FalphaS_09 = np.array(FalphaS_09)
#=========================================================#

# wth for 1.0 GeV
M_10 = []
FalphaS_10 = []
with open("FalphaS_10.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_10.append(float(i.split()[0]))
		FalphaS_10.append(float(i.split()[1]))

M_10 = np.array(M_10)
FalphaS_10 = np.array(FalphaS_10)
#=========================================================#



fig, ax = plt.subplots()

plt.ylim(0.2,0.6)
plt.xlim(0.20,1.0)
ax.plot(M_06, FalphaS_06, color='blue',linewidth=2,label='$\omega_{th} = 0.6$ GeV')
ax.plot(M_07, FalphaS_07, color='orange',linewidth=2,label='$\omega_{th} = 0.7$ GeV')
ax.plot(M_08, FalphaS_08,color='purple',linewidth=2,label='$\omega_{th} = 0.8$ GeV')
ax.plot(M_09, FalphaS_09,color='black',linewidth=2,label='$\omega_{th} = 0.9$ GeV')
ax.plot(M_10, FalphaS_10,color='red',linewidth=2,label='$\omega_{th} = 1.0$ GeV')



#stability window
#=================#
#plt.axvline(0.4,0,1,color="black",linewidth=1.2,linestyle="--")
#plt.axvline(0.6,0,1,color="black",linewidth=1.2,linestyle="--")
#==================#

legend = ax.legend(loc= (0.015,0.03), shadow=True)
plt.xlabel("$M$ in GeV",fontsize =12)
plt.ylabel("$F(\mu)$ in GeV$^{3/2}$", fontsize =12)
plt.grid(True)
#plt.show()
plt.savefig("FalphaS.svg")
