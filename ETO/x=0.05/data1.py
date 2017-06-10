# This file is used to plot the data from eto SPAWAR 080212a prepared on 04-14-2017.dat(which is renamed R1.dat

import matplotlib.pyplot as plt
from math import*
from numpy import linspace


resistance = []
temp = []
dev = [] 
resistivity =[]
w = 2.8092
t = 1.5723
A = w*t
l = 1.237

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
	resistivity.append(float(list[6])*A/l/10)
	temp.append(list[2])
	


plt.plot(temp,resistance,'r-',temp,resistance,'b.')
plt.axis([0,300,0,1.5])
plt.ylabel('resistance'+r'$( \Omega )$')
plt.xlabel('temperature (K)')
plt.title('resistance X=0.05')
plt.grid(True)
plt.savefig('resistanceX=0.05.png')
plt.close()

plt.plot(temp,resistivity,'r-',temp,resistivity,'b.')
plt.axis([0,300,0,0.5])
plt.ylabel(r'$\rho$'+" "+r'$( \Omega *cm )$')
plt.xlabel('temperature (K)')
plt.title('resistivity X=0.05')
plt.grid(True)
plt.savefig('resistivityX=0.05.png')
plt.show()
 
 


