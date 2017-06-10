# This file is used to plot the data from eto SPAWAR 080212a prepared on 04-14-2017.dat(which is renamed R1.dat

import matplotlib.pyplot as plt
from math import*
from numpy import linspace


resistance = []
temp = []
dev = [] 
resistivity =[]
l = 0.041275
w = 0.209677
t = 0.046863
A = w*t


file = open('R1.dat','r')
lines = file.readlines()
file.close()
counter=-1
stage = 1;
onsetT = 0;
onsetR = 0;
transitT = 0;
transitR = 0;
# read the data from the file
for line in lines:  	
	list = line.split(",")
	resistance.append(list[6])
	resistivity.append(float(list[6])*A/l)
	temp.append(list[2])
	


plt.plot(temp,resistance,'r-',temp,resistance,'b.')
plt.axis([0,300,0,10])
plt.ylabel('resistance'+r'$( \Omega )$')
plt.xlabel('temperature (K)')
plt.title('resistance X=0.00')
plt.grid(True)
plt.savefig('resistanceX=0.00.png')
plt.close()

plt.plot(temp,resistivity,'r-',temp,resistivity,'b.')
plt.axis([0,300,0,2])
plt.ylabel(r'$\rho$'+" "+r'$( \Omega *cm )$')
plt.xlabel('temperature (K)')
plt.title('resistivity X=0.00')
plt.grid(True)
plt.savefig('resistivityX=0.00.png')
plt.show()
 
 


