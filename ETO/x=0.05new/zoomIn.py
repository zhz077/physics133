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
max = 0;
maxI=0
# read the data from the file
for line in lines:  	
	list = line.split(",")
	if list[26] =="":
		continue;
	resistance.append(list[26])
	resistivity.append(float(list[26])*A/l/10)
	print float(list[26])*A/l/10
	temp.append(list[2])
	if counter > -1:
		if float(temp[counter]) == float(temp[counter+1]):
			dev.append(dev[counter-1])
		else:
			dev.append((float(resistivity[counter])-float(resistivity[counter+1]))/(float(temp[counter])-float(temp[counter+1])))		
		print dev[counter]
		if float(temp[counter])>6:
			if dev[counter] == 0 and dev[counter-1]>0 and stage == 1:
				transitT = temp[counter-1]
				transitR = resistivity[counter-1] 
				stage = 2
			if float(temp[counter]) > 11.05:
				if resistivity[counter]>max:
					max = resistivity[counter]
					maxI= counter
				##if dev[counter] < 0.4168926465 and dev[counter] >0.4168926464 and stage == 2:
				##	onsetT = temp[counter]		
				##	onsetR = resistivity[counter]
				##	sharpDe = dev[counter]
				##	sharpDeb = dev[counter-3]
				##	stage = 3
	counter += 1

onsetT = temp[maxI]		
onsetR = resistivity[maxI]
sharpDe = dev[maxI]
sharpDeb = dev[maxI-2]	

Tc = round((float(onsetT)+float(transitT))/2,2)
To = round(float(onsetT),2)
Tt = round(float(transitT),2)
plt.plot(temp,resistivity,'k-',temp,resistivity,'b.')
plt.axis([0,15,0,0.6])
plt.plot((float(transitT)-2, float(transitT)+2), (transitR, transitR), 'r--')
plt.plot((transitT,transitT),(transitR,0),'r--')
plt.plot((float(onsetT)-1,float(onsetT)),(onsetR+sharpDe,onsetR),'r--')
plt.plot((float(onsetT),float(onsetT)+0.5),(onsetR,onsetR+sharpDeb/2),'r--')
plt.plot((onsetT,onsetT),(onsetR,0),'r--')
print sharpDeb
plt.ylabel(r'$\rho$'+" "+r'$( \Omega *cm )$')
plt.xlabel('temperature (K)')
plt.title('zoomIn part of x=0.05 RERUN for Tc')
plt.grid(True)

plt.annotate('On set',xy = (onsetT,onsetR),xytext = (10.5,0.55),arrowprops=dict(arrowstyle = '->',connectionstyle = 'arc3'))
plt.annotate('Transit',xy = (transitT,transitR),xytext = (transitT,0.3),arrowprops=dict(arrowstyle = '->',connectionstyle = 'arc3'))

plt.annotate('Tc = '+ str(Tc)+'K', xytext = (12,0.3),xy=(12,0.3))
plt.annotate('Tt = '+ str(Tt)+'K', xytext = (12,0.25),xy=(12,0.25))
plt.annotate('To = '+ str(To)+'K', xytext = (12,0.2),xy=(12,0.2))
plt.savefig('zoomInReRun.png')
plt.show()

