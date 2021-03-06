# Author @ Zheng H. Zhang
# Date @ 5/22/2017
# Description: This file is used to plot and fit the vsm data from Li(Ti_(1-x)V_(x))_2O_4 
#			   || x =0.05 for phys 133
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

sus2 = []
moment2 =[]
counter = 0
offset = 0
fitT = []
fitSus=[]
fitM=[]
Mm = 167.27475
mass = mass/Mm

file = open('r.dat','r')
lines = file.readlines()
file.close()

# read the data from the file
for line in lines:  	
	list = line.split(",")
	if (list[4] != ''):
		resistance1.append(float(list[4])/mass/10000)
		temp1.append(float(list[2]))
		sus1.append(1/(float(list[4])/mass/10000))

sus2 = sus1
moment2 = resistance1
plt.plot(temp1,resistance1,'r-',temp1,resistance1,'b.')
plt.axis([50,300,0,0.001])
plt.ylabel(r'$\chi = M/H$'+" " +r'$($'+ " " +r'$emu$'+" " +r'$mol^{-1}$'+')')
plt.xlabel('temperature')
plt.title('raw data -sus')
plt.grid(True)
plt.savefig('rawDataPlots.png')

####################################################################################
#Starts the analysis

#plot raw data // no need to filter the signal
plt.subplot(221)
plt.plot(temp1,sus1,'k-',temp1,sus1,'b.')
plt.axis([50,300,1000,2500])
plt.ylabel(r'$\chi^-$')
plt.xlabel('temperature(K)')
plt.title('raw data -susInv')
plt.grid(True)

plt.subplot(222)
plt.plot(temp1,resistance1,'k-',temp1,resistance1,'b.')
plt.axis([50,300,0,0.001])
plt.ylabel(r'$\chi = M/H$')
plt.xlabel('temperature(K)')
plt.title('raw data -sus')
plt.grid(True)

# define the fitting function for moment plot
def funcM(t1,c1,tc1,xo):
	return c1/(t1-tc1)+xo
paramsM = curve_fit(funcM,temp1,moment2)
[mc,mtc,xo] = paramsM[0]
print mc,mtc,xo

# define the fitting function for sus^-1 plot
def funcX(t,xo,c,tc):
	return 1/(c/(t-tc)+xo)

def funcXo (t,c,tc):
	return 1/(c/(t-tc))
	

# find the linear region to apply the method


# apply the fitting function and offset to the data
plt.subplot(223)
plt.plot(temp1,sus2,'b.')
plt.plot(temp1,sus2,'k-',label = 'rawData')
plt.plot(temp1, funcX(temp1,xo,mc,mtc), 'r-', label='fit')
plt.axis([50,300,1000,2500])
plt.ylabel(r'$\chi^-$')
plt.xlabel('temperature(K)')
plt.legend()
plt.title('adjusted -susInv')
plt.grid(True)

plt.subplot(224)
plt.plot(temp1,moment2,'b.')
plt.plot(temp1,moment2,'k-',label = 'rawData')
plt.plot(temp1, funcM(temp1, mc,mtc,xo), 'r-', label='fit')
plt.axis([50,300,0,0.001])
plt.ylabel(r'$\chi = M/H$')
plt.xlabel('temperature(K)')
plt.legend()
plt.title('adjusted -sus')
plt.grid(True)

susL = []
susL2 = []
for i in range(len(moment2)):
	susL.append((moment2[i]-xo)**(-1))
	#print susL[i]
	susL2.append((moment2[i])**(-1))
##################Calculate effective moment = 2.82787 * (T*X)^0.5#################
ME= []
for i in range(len(sus2)):
	sus2[i] = 1/sus2[i];
 	ME.append((moment2[i]*temp1[i])**0.5*2.82787);

 	
 	#print ME[i]

#print sum(ME)/len(ME)
plt.savefig('processed.png')
plt.close()


 
	
fig, ax1 = plt.subplots()
ax1.plot(temp1,moment2,'b.')
plt.plot(temp1, funcM(temp1, mc,mtc,xo), 'r-')
ax1.set_xlabel('temperature(K)')
ax1.set_ylabel(r'$\chi = M/H$', color='r')
ax1.tick_params('y', colors='r')


ax2 = ax1.twinx()
ax2.plot(temp1,susL,'k.')
#ax2.plot(temp1,sus2,'r.')
meff = str(round(2.872787*(mc)**0.5,2))
ax2.plot(temp1, funcXo(temp1, mc,mtc), 'g-',label = '$\mu_{eff} =$' +meff +'emu')
ax2.set_ylabel(r'$(\chi-\chi_o)^-$', color='g')
ax2.tick_params('y', colors='g')
ax2.axis([50,300,2000,15000])
plt.title('x = 0.00')
ax2.legend()
plt.savefig('sus-susInv.png')

plt.close()

plt.plot(temp1,ME,'r-',temp1,ME,'b.')
plt.ylabel('$\mu_eff (emu)$')
plt.xlabel('$temperature(K)$')
plt.title('x=0.0')
plt.savefig('effective moment plots.png')
plt.show()