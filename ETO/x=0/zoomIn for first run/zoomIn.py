# This file is used to plot the data from eto SPAWAR 080212a prepared on 04-14-2017.dat(which is renamed R1.dat

import matplotlib.pyplot as plt
from math import*
from numpy import linspace


resistance = []
temp = []
dev = [] 
file = open('zoomIn.dat','r')
lines = file.readlines()
file.close()
counter=-1
stage = 1;
onsetT = 0;
onsetR = 0;
transitT = 0;
transitR = 0;
l = 0.041275
w = 0.209677
t = 0.046863
A = w*t
resistivity =[]
# read the data from the file
for line in lines:  	
	list = line.split(",")
	if list[6] == "" :
		continue;
	resistance.append(list[6])
	resistivity.append(float(list[6])*A/l)
	temp.append(list[2])
	if counter > -1:
		if float(temp[counter]) == float(temp[counter+1]):
			dev.append(dev[counter-1])
		else:
			dev.append((float(resistivity[counter])-float(resistivity[counter+1]))/(float(temp[counter])-float(temp[counter+1])))		

		if float(temp[counter]) > 9.5:
			if dev[counter] > 0 and stage == 1:
				transitT = temp[counter-1]
				transitR = resistivity[counter-1] 
				stage = 2
			if float(temp[counter]) > 11.5:
				if dev[counter] < 0.5 and stage == 2:
					onsetT = temp[counter]		
					onsetR = resistivity[counter]
					stage = 3
	counter += 1

Tc = round((float(onsetT)+float(transitT))/2,2)
To = round(float(onsetT),2)
Tt = round(float(transitT),2)
print onsetT
print transitT

plt.plot(temp,resistivity,'r-',temp,resistivity,'b.')
plt.axis([0,16,0,2])
plt.ylabel(r'$\rho$'+" "+r'$( \Omega *cm )$')
plt.xlabel('temperature (K)')
plt.title('zoomIn part of x=0.00 for Tc')
plt.grid(True)

plt.annotate('On set',xy = (onsetT,onsetR),xytext = (onsetT,1.95),arrowprops=dict(arrowstyle = '->',connectionstyle = 'arc3'))
plt.annotate('Transit',xy = (transitT,transitR),xytext = (transitT,1.95),arrowprops=dict(arrowstyle = '->',connectionstyle = 'arc3'))

plt.annotate('Tc = '+ str(Tc)+'K', xytext = (13,0.4),xy=(13,0.4))
plt.annotate('Tt = '+ str(Tt)+'K', xytext = (13,0.3),xy=(13,0.3))
plt.annotate('To = '+ str(To)+'K', xytext = (13,0.2),xy=(13,0.2))
plt.savefig('zoomIn.png')
plt.show()

