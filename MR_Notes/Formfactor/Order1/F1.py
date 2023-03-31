import matplotlib.pyplot as plt 
import numpy as np

plt.rc('text', usetex=True)

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42


#Without RGE improved, F with alphaS order is defined 
#in Nishikawa & Tanaka paper, Eq. (71)
M_11 = []
F1_11 = []
with open("F1_11.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_11.append(float(i.split()[0]))
		F1_11.append(float(i.split()[1]))

M_11 = np.array(M_11)
F1_11 = np.array(F1_11)
#=========================================================#

M_12 = []
F1_12 = []
with open("F1_12.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_12.append(float(i.split()[0]))
		F1_12.append(float(i.split()[1]))

M_12 = np.array(M_12)
F1_12 = np.array(F1_12)

#=========================================================#

M_13 = []
F1_13 = []
with open("F1_13.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_13.append(float(i.split()[0]))
		F1_13.append(float(i.split()[1]))

M_13 = np.array(M_13)
F1_13 = np.array(F1_13)
#=========================================================#

M_14 = []
F1_14 = []
with open("F1_14.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_14.append(float(i.split()[0]))
		F1_14.append(float(i.split()[1]))

M_14 = np.array(M_14)
F1_14 = np.array(F1_14)
#=========================================================#

M_15 = []
F1_15 = []
with open("F1_15.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_15.append(float(i.split()[0]))
		F1_15.append(float(i.split()[1]))

M_15 = np.array(M_15)
F1_15 = np.array(F1_15)
#=========================================================#



fig, ax = plt.subplots()

plt.ylim(0.1,0.5)
plt.xlim(0.20,2.0)
ax.plot(M_11, F1_11, color='blue',linewidth=2,label='$\\omega_{th} = 0.8$ GeV')
ax.plot(M_12, F1_12, color='orange',linewidth=2,label='$\\omega_{th} = 0.9$ GeV')
ax.plot(M_13, F1_13,color='purple',linewidth=2,label='$\\omega_{th} = 1.0$ GeV')
ax.plot(M_14, F1_14,color='black',linewidth=2,label='$\\omega_{th} = 1.1$ GeV')
ax.plot(M_15, F1_15,color='red',linewidth=2,label='$\\omega_{th} = 1.2$ GeV')

plt.rc('legend',fontsize=12.5) 

#stability window
#=================#
#plt.axvline(0.4,0,1,color="black",linewidth=1.2,linestyle="--")
#plt.axvline(0.6,0,1,color="black",linewidth=1.2,linestyle="--")
#==================#

legend = ax.legend(loc= "lower right", shadow=True)
plt.xlabel("$M$ in GeV",fontsize =14)
plt.ylabel("$F(\mu)$ in GeV$^{3/2}$", fontsize =14)
plt.grid(True)
#plt.show()
plt.savefig("plots/F1.pdf")
