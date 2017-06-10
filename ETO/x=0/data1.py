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
# read the data from the file
for line in lines:  	
	list = line.split(",")
	if list[6] == "":
		continue;
	resistance.append(list[6])
	print list[6]
	temp.append(list[2])
	


plt.plot(temp,resistance,'r-',temp,resistance,'b.')
plt.axis([0,300,0,10])
plt.ylabel('resistance')
plt.xlabel('temperature')
plt.title('resistance X=0.00')
plt.grid(True)

plt.savefig('resistanceX=0.00 first run channel1.png')
plt.show()
 
 


