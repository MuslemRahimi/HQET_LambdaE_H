import matplotlib.pyplot as plt 
import numpy as np


#Without RGE improved, F with alphaS order is defined 
#in Nishikawa & Tanaka paper, Eq. (71)
# wth for 0.6 GeV
M_06 = []
fBalphaS_06 = []
with open("fBalphaS_06.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_06.append(float(i.split()[0]))
		fBalphaS_06.append(float(i.split()[1]))

M_06 = np.array(M_06)
fBalphaS_06 = np.array(fBalphaS_06)
#=========================================================#

# wth for 0.7 GeV
M_07 = []
fBalphaS_07 = []
with open("fBalphaS_07.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_07.append(float(i.split()[0]))
		fBalphaS_07.append(float(i.split()[1]))

M_07 = np.array(M_07)
fBalphaS_07 = np.array(fBalphaS_07)

#=========================================================#

# wth for 0.8 GeV
M_08 = []
fBalphaS_08 = []
with open("fBalphaS_08.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_08.append(float(i.split()[0]))
		fBalphaS_08.append(float(i.split()[1]))

M_08 = np.array(M_08)
fBalphaS_08 = np.array(fBalphaS_08)
#=========================================================#

# wth for 0.9 GeV
M_09 = []
fBalphaS_09 = []
with open("fBalphaS_09.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_09.append(float(i.split()[0]))
		fBalphaS_09.append(float(i.split()[1]))

M_09 = np.array(M_09)
fBalphaS_09 = np.array(fBalphaS_09)
#=========================================================#

# wth for 1.0 GeV
M_10 = []
fBalphaS_10 = []
with open("fBalphaS_10.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_10.append(float(i.split()[0]))
		fBalphaS_10.append(float(i.split()[1]))

M_10 = np.array(M_10)
fBalphaS_10 = np.array(fBalphaS_10)
#=========================================================#



fig, ax = plt.subplots()

plt.ylim(0.1,0.3)
plt.xlim(0.20,1.0)
ax.plot(M_06, fBalphaS_06, color='blue',linewidth = 2,label='$\omega_{th} = 0.6$ GeV')
ax.plot(M_07, fBalphaS_07, color='orange',linewidth = 2,label='$\omega_{th} = 0.7$ GeV')
ax.plot(M_08, fBalphaS_08,color='purple',linewidth = 2,label='$\omega_{th} = 0.8$ GeV')
ax.plot(M_09, fBalphaS_09,color='black',linewidth = 2,label='$\omega_{th} = 0.9$ GeV')
ax.plot(M_10, fBalphaS_10,color='red',linewidth = 2,label='$\omega_{th} = 1.0$ GeV')



#fB lattice QCD result
#=================#
#plt.axvline(0.4,0,1,color="black",linewidth=1.2,linestyle="--")
fB= 0.1920
dfB= 0.0046
ax.hlines(0.1920, 0, 1, colors='black', linewidth = 2,linestyles='--', label='')
ax.axhspan(fB-dfB, fB+dfB, facecolor="green",alpha=0.5)
#==================#

legend = ax.legend(loc= (0.015,0.03), shadow=True)
plt.xlabel("$M$ in GeV",fontsize = 12)
plt.ylabel("$f_{B}$ in GeV",fontsize = 12)
plt.grid(True)
#plt.show()
plt.savefig("fBalphaS.pdf")
