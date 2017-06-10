# This file is used to plot the data from eto SPAWAR 080212a prepared on 04-14-2017.dat(which is renamed R1.dat

import matplotlib.pyplot as plt
from math import*
from numpy import linspace


resistance = []
temp = []

file = open('sb.dat','r')
lines = file.readlines()
file.close()

# read the data from the file
for line in lines[19::]:  	
	list = line.split(",,,")
	resistance.append(list[1].split(",")[0])
	temp.append(list[0].split(",")[2])
plt.plot(temp,resistance,'r-',temp,resistance,'b.')
plt.axis([50,320,50,70])
plt.ylabel('resistance')
plt.xlabel('temperature')
plt.title('resistivity experiment sample B')
plt.grid(True)

plt.savefig('resistivitySampleA.png')
plt.show()


