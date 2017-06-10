# This file is used to plot the data from eto SPAWAR 080212a prepared on 04-14-2017.dat(which is renamed R1.dat

import matplotlib.pyplot as plt
from math import*
from numpy import linspace


resistance = []
temp = []
dev = [] 
file = open('R1.dat','r')
lines = file.readlines()
file.close()
counter=-1
stage = 1;
onsetT = 0;
onsetR = 0;
transitT = 0;
transitR = 0;
l = 0.02337
w = 0.13005
t = 0.04775
A = w*t
resistivity =[]
# read the data from the file
counter =0;
for line in lines:  	
	list = line.split(",")
	if list[26] == "":
		continue;
	resistance.append(list[26])
	print resistance[counter]
	temp.append(float(list[2]))
	resistivity.append(float(list[26])*A/l)
	counter = counter +1
	


plt.plot(temp,resistance,'r-',temp,resistance,'b.')
plt.axis([0,300,0,0.35])
plt.ylabel('resistance'+r'$( \Omega )$')
plt.xlabel('temperature (K)')
plt.title('resistance X=0.01')
plt.grid(True)

plt.savefig('resistanceX=0.01.png')
plt.close()

plt.plot(temp,resistivity,'r-',temp,resistivity,'b.')
plt.axis([0,300,0,0.1])
plt.ylabel(r'$\rho$'+" "+r'$( \Omega *cm )$')
plt.xlabel('temperature (K)')
plt.title('resistivity X=0.01')
plt.grid(True)
plt.savefig('resistivityX=0.01.png')

plt.show()
 
 


