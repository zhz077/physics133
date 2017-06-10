# Author @ Zheng H. Zhang
# Date @ 5/22/2017
# Description: This file is used to plot and fit the vsm data from Li(Ti_(1-x)V_(x))_2O_4 
#			   || x =0.00, x=0.01 and x=0.05 for phys 133
# Notice: This file is only usable when there is a data file named 'r1.dat' in the same
#		  Directory.

# import packages
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import csv
from scipy.optimize import curve_fit
# Declare variables 
resistance1 = []
temp1 = []
sus1= []
mass = 0.0221
error=[]
sus2 = []
moment2 =[]
counter = 0
offset = 0
fitT = []
fitSus=[]
fitM=[]
Mm = 167.27475
mass = mass/Mm

file = open('0.5.dat','r')
lines = file.readlines()
file.close()

# read the data from the file
for line in lines:  	
	list = line.split(",")
	if (list[4] != ''):
		resistance1.append(float(list[4])/mass/10)
		error.append(float(list[5])/mass/10)
		temp1.append(float(list[2]))
		sus1.append(10000*mass/float(list[4]))
		sus2.append(10000*mass/(float(list[4]) + offset*mass))
		counter += 1;
def funcM(t1,c1,tc1,xo):
	return 1000*(c1/(t1-tc1)+xo)
paramsM = curve_fit(funcM,temp1,resistance1)
[mc,mtc,xo] = paramsM[0]

# plot the original data and found there is a offset
plt.plot(temp1,resistance1,'gv',label=r'$ x = 0.05,T_c = -10.17K, C = 0.028, \chi_o = 0.3679*10^{-3}emu$')
# plt.plot(temp1,resistance1,'gv')
c = str (round(mc,3))
tc = str (round(mtc,2))
print c 
print tc
plt.plot(temp1, funcM(temp1, mc,mtc,xo), 'g--')

plt.axis([50,300,0,1])
plt.ylabel(r'$\chi = M/H/$'+" " +r'$(10^{-3}$'+ " " +r'$emu$'+" " +r'$mol^{-1}$'+')')
plt.xlabel('Temperature (K)')
plt.title('raw data -moment')
plt.grid(True)

resistance1 = []
temp1 = []
sus1= []
mass = 0.0213

sus2 = []
moment2 =[]
counter = 0
offset = 0
fitT = []
fitSus=[]
fitM=[]
Mm = 166.79175
mass = mass/Mm

file = open('0.1.dat','r')
lines = file.readlines()
file.close()

# read the data from the file
for line in lines:  	
	list = line.split(",")
	if (list[4] != ''):
		resistance1.append(float(list[4])/mass/10)
		temp1.append(float(list[2]))
		sus1.append(10000*mass/float(list[4]))
		moment2.append(	(float(list[4])) /mass+offset)
		sus2.append(10000*mass/(float(list[4]) + offset*mass))
		counter += 1;


# plot the original data and found there is a offset
paramsM = curve_fit(funcM,temp1,resistance1)
[mc,mtc,xo] = paramsM[0]
plt.plot(temp1,resistance1,'kD',label=r'$ x = 0.01,T_c = -0.50K, C = 0.010, \chi_o = 0.18958*10^{-3}emu$')
c = str (round(mc,4))
tc = str (round(mtc,2))

plt.plot(temp1, funcM(temp1, mc,mtc,xo), 'k:')

resistance1 = []
temp1 = []
sus1= []
mass = 0.00983

sus2 = []
moment2 =[]
counter = 0
offset = 0
fitT = []
fitSus=[]
fitM=[]
Mm =166.671
mass = mass/Mm

file = open('0.dat','r')
lines = file.readlines()
file.close()

# read the data from the file
for line in lines:  	
	list = line.split(",")
	if (list[4] != ''):
		resistance1.append(float(list[4])/mass/10)
		temp1.append(float(list[2]))
		sus1.append(10000*mass/float(list[4]))
		if (resistance1[counter-1]>0.00014/mass/10 and resistance1[counter]<0.00014/mass/10 ):
			offset = resistance1[counter-1]-resistance1[counter]
		moment2.append(	(float(list[4]))/mass/10+offset)
		sus2.append(10000*mass/(float(list[4]) + offset*mass))
		if (temp1[counter]>110 and temp1[counter]<260):
			fitT.append(temp1[counter])
			fitSus.append(sus2[counter])
			fitM.append(moment2[counter])
		counter += 1;

paramsM = curve_fit(funcM,temp1,moment2)
[mc,mtc,xo] = paramsM[0]
print xo
plt.plot(temp1,moment2,'ro',label=r'$ x = 0.00,T_c = 45.97K, C = 0.001, \chi_o = 0.23125*10^{-3}emu$')
c = str (round(mc,3))
tc = str (round(mtc,3))
plt.plot(temp1, funcM(temp1, mc,mtc,xo), 'r-')
plt.legend()


plt.savefig('processed.png')
plt.show()



