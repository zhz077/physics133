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
lineC = 1;
for line in lines[20::]:
	if lineC != 0:  	
		list = line.split(",,,")
		resistance.append(list[1].split(",")[0])
		temp.append(list[0].split(",")[2])

	
		if counter > -1:
			if float(temp[counter])-float(temp[counter+1])== 0:
				dev.append(dev[counter-1])
			else:
				dev.append(abs((float(resistance[counter])-float(resistance[counter+1]))/(float(temp[counter])-float(temp[counter+1]))))
				
			if dev[counter] > 0.5 and stage == 1:
				transitT = temp[counter-1]
				transitR = resistance[counter-1] 
				stage = 2
			if dev[counter-1]<0.5 and  dev[counter] < 0.5 and stage == 2:
				onsetT = temp[counter]		
				onsetR = resistance[counter]
				stage = 3
		counter += 1
		lineC = 0 
	else :
		lineC = 1

Tc = round((float(onsetT)+float(transitT))/2,2)
To = round(float(onsetT),2)
Tt = round(float(transitT),2)

plt.plot(temp,resistance,'r-',temp,resistance,'b.')
plt.axis([50,320,0,24])
plt.ylabel('resistance')
plt.xlabel('temperature')
plt.title('resistivity experiment sample C')
plt.grid(True)

plt.annotate('On set',xy = (onsetT,onsetR),xytext = (onsetT,20),arrowprops=dict(arrowstyle = '->',connectionstyle = 'arc3'))
plt.annotate('Transit',xy = (transitT,transitR),xytext = (100,5),arrowprops=dict(arrowstyle = '->',connectionstyle = 'arc3'))

plt.annotate('Tc = '+ str(Tc)+'K', xytext = (250,4),xy=(250,4))
plt.annotate('Tt = '+ str(Tt)+'K', xytext = (250,8),xy=(250,8))
plt.annotate('To = '+ str(To)+'K', xytext = (250,6),xy=(250,6))
plt.savefig('resistivitySampleC.png')
plt.show()


