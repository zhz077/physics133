# This file is used to plot the data from eto SPAWAR 080212a prepared on 04-14-2017.dat(which is renamed R1.dat

import matplotlib.pyplot as plt
from math import*
from numpy import linspace


resistance = []
temp = []
dev = [] 
dev2 = []
resistivity =[]
l = 0.041275
w = 0.209677
t = 0.046863
A = w*t
file = open('zoomIn.dat','r')
lines = file.readlines()
file.close()
counter=-1
stage = 1;
onsetT = 0;
onsetR = 0;
transitT = 0;
transitR = 0;
sharpDe = 0;
sharpDeb =0;
counter2 = -1;
# read the data from the file
for line in lines:  	
	list = line.split(",")
	resistance.append(list[6])
	resistivity.append(float(list[6])*A/l)
	temp.append(list[2])
	if counter > -1:
		if float(temp[counter]) == float(temp[counter+1]):
			dev.append(dev[counter-1])
		else:
			dev.append((float(resistivity[counter])-float(resistivity[counter+1]))/(float(temp[counter])-float(temp[counter+1])))		
		if counter > 1:
			if float(temp[counter]) == float(temp[counter-1]):
				dev2.append(0)
				counter2 += 1;
			else:
				dev2.append((dev[counter]-dev[counter-1]))
				counter2 += 1;
		if float(temp[counter])>8:
			if abs(dev2[counter2])>0.1 and abs(dev[counter]) <0.05 and stage == 1:
				transitT = temp[counter]
				transitR = resistivity[counter] 
				stage = 2
			if float(temp[counter]) > 11:
				print dev[counter]
		
				if dev[counter-1] >0.0703497763942 and dev[counter-1] <0.0703497763944 and stage == 2:
					onsetT = temp[counter]		
					onsetR = resistivity[counter]
					sharpDe = dev[counter]
					sharpDeb = dev[counter-1]
					stage = 3
	counter += 1
	


Tc = round((float(onsetT)+float(transitT))/2,2)
To = round(float(onsetT),2)
Tt = round(float(transitT),2)
plt.plot(temp,resistivity,'k-',temp,resistivity,'b.')
plt.axis([0,15,0,2])
plt.plot((float(transitT)-2, float(transitT)+2), (transitR, transitR), 'r--')
plt.plot((transitT,transitT),(transitR,0),'r--')
plt.plot((float(onsetT)-1,float(onsetT)),(onsetR+sharpDe,onsetR),'r--')
plt.plot((float(onsetT),float(onsetT)+1),(onsetR,onsetR+sharpDeb),'r--')
plt.plot((onsetT,onsetT),(onsetR,0),'r--')

plt.ylabel(r'$\rho$'+" "+r'$( \Omega *cm )$')
plt.xlabel('temperature (K)')
plt.title('zoomIn part of x=0.00 for Tc')
plt.grid(True)

plt.annotate('On set',xy = (onsetT,onsetR),xytext = (10.5,1.75),arrowprops=dict(arrowstyle = '->',connectionstyle = 'arc3'))
plt.annotate('Transit',xy = (transitT,transitR),xytext = (transitT,1),arrowprops=dict(arrowstyle = '->',connectionstyle = 'arc3'))

plt.annotate('Tc = '+ str(Tc)+'K', xytext = (12,0.7),xy=(12,0.7))
plt.annotate('Tt = '+ str(Tt)+'K', xytext = (12,0.5),xy=(12,0.5))
plt.annotate('To = '+ str(To)+'K', xytext = (12,0.3),xy=(12,0.3))
plt.savefig('zoomIn.png')
plt.show()

