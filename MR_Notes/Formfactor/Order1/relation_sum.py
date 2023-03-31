import matplotlib.pyplot as plt 
import numpy as np

plt.rc('text', usetex=True)

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42


#=========================================================#

# wth for 0.85 GeV
M_085 = []
Relation1_085 = []
with open("Relation1_0.85.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_085.append(float(i.split()[0]))
		Relation1_085.append(float(i.split()[1]))

M_085 = np.array(M_085)
Relation1_085 = np.array(Relation1_085)
#=========================================================#

# wth for 1.0 GeV
M_10 = []
Relation1_10 = []
with open("Relation1_1.0.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_10.append(float(i.split()[0]))
		Relation1_10.append(float(i.split()[1]))

M_10 = np.array(M_10)
Relation1_10 = np.array(Relation1_10)

#=========================================================#

# wth for 1.15 GeV

M_115 = []
Relation1_115 = []
with open("Relation1_1.15.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_115.append(float(i.split()[0]))
		Relation1_115.append(float(i.split()[1]))

M_115 = np.array(M_115)
Relation1_115 = np.array(Relation1_115)
#=========================================================#
#=========================================================#
#=========================================================#
#=========================================================#

# wth for 0.85 GeV
M_085 = []
Relation2_085 = []
with open("Relation2_0.85.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_085.append(float(i.split()[0]))
		Relation2_085.append(float(i.split()[1]))

M_085 = np.array(M_085)
Relation2_085 = np.array(Relation2_085)
#=========================================================#

# wth for 1.0 GeV
M_10 = []
Relation2_10 = []
with open("Relation2_1.0.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_10.append(float(i.split()[0]))
		Relation2_10.append(float(i.split()[1]))

M_10 = np.array(M_10)
Relation2_10 = np.array(Relation2_10)

#=========================================================#

# wth for 1.15 GeV

M_115 = []
Relation2_115 = []
with open("Relation2_1.15.txt", "r") as data:
	data = data.readlines()
	for i in data:
		M_115.append(float(i.split()[0]))
		Relation2_115.append(float(i.split()[1]))

M_115 = np.array(M_115)
Relation2_115 = np.array(Relation2_115)
#=========================================================#
#=========================================================#
#=========================================================#



#=========================================================#
fig, ax = plt.subplots()

plt.ylim(1,1.5)
ax.plot(M_085, Relation1_085, "--", color='blue',label='$\\omega_{th} = 0.8$ GeV')
ax.plot(M_10, Relation1_10, color='black',label='$\\omega_{th} = 0.9$ GeV')
ax.plot(M_115, Relation1_115,"--",color='red',label='$\\omega_{th} = 1.0$ GeV')
plt.rc('legend',fontsize=12)
ax.axvspan(0.5, 0.8, alpha=0.4, color='green')
legend = ax.legend(loc=1,bbox_to_anchor=(1,1), shadow=True)
#plt.tight_layout()
#fig.set_size_inches(8, 5.5)
plt.xlabel("$M$ in GeV",fontsize=14)
plt.ylabel("$(1+\\mathcal{R})^{2}$",fontsize=14)
plt.grid(True)
#plt.show()
plt.tight_layout()
plt.savefig("plots/Relation1.pdf")
#=========================================================#
fig, ax = plt.subplots()


plt.ylim(1,1.05)
plt.yticks(np.arange(1, 1.05, step=0.01))
ax.plot(M_085, Relation2_085, "--", color='blue',label='$\\omega_{th} = 0.8$ GeV')
ax.plot(M_10, Relation2_10, color='black',label='$\\omega_{th} = 0.9$ GeV')
ax.plot(M_115, Relation2_115,"--",color='red',label='$\\omega_{th} = 1.0$ GeV')

plt.rc('legend',fontsize=12)

ax.yaxis.set_label_coords(-0.09, 0.6)
plt.xlabel("$M$ in GeV",fontsize = 14)
plt.ylabel("$\\frac{(F(\\mu)^{2} e^{-\\bar{\\Lambda}/M} + F(\\mu)^{2} e^{-\\bar{\\Lambda}/M} \\lambda_{H}^{4})}{(F(\\mu)^{2} e^{-\\bar{\\Lambda}/M} - F(\\mu)^{2} e^{-\\bar{\\Lambda}/M} \\lambda_{E}^{4})}$",fontsize=16)
plt.grid(True)
plt.tight_layout()
ax.axvspan(0.5, 0.8, alpha=0.4, color='green')
legend = ax.legend(loc=1,bbox_to_anchor=(1,1), shadow=True)

#plt.show()
plt.savefig("plots/Relation2.pdf")