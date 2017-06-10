# This file is used to plot the data from eto SPAWAR 080212a prepared on 04-14-2017.dat(which is renamed R1.dat
import matplotlib.pyplot as plt
from math import*
from numpy import linspace


resistance = []
temp = []
dev = [] 
filec = open('SC.dat','r')
linesc = filec.readlines()
filec.close()
counter=-1
stage = 1;
onsetT = 0;
onsetR = 0;
transitT = 0;
transitR = 0;
# read the data from the file
lineC = 1;
for line in linesc[20::]:
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

Tcc = round((float(onsetT)+float(transitT))/2,2)
Toc = round(float(onsetT),2)
Ttc = round(float(transitT),2)

plt.plot(temp,resistance,'k-',temp,resistance,'b.')
plt.axis([50,320,0,24])
plt.ylabel('resistance')
plt.xlabel('temperature')
plt.title('resistivity experiment sample A+C')
plt.grid(True)
plt.annotate('On set',xy = (onsetT,onsetR),xytext = (100,20),arrowprops=dict(arrowstyle = '->',connectionstyle = 'arc3'),color='b')
plt.annotate('Transit',xy = (transitT,transitR),xytext = (100,5),arrowprops=dict(arrowstyle = '->',connectionstyle = 'arc3'),color='b')
plt.figtext(0.8,0.35,'Sample C', size = 'small',color='k')
plt.figtext(0.8,0.2,'Tc = '+ str(Tcc)+'K', size = 'small',color='k')
plt.figtext(0.8,0.25,'To = '+ str(Toc)+'K', size = 'small',color='k')
plt.figtext(0.8,0.3,'Tt = '+ str(Ttc)+'K', size = 'small',color='k')

resistance = []
temp = []
dev = [] 
file = open('SA.dat','r')
lines = file.readlines()
file.close()
counter=-1
stage = 1;
onsetT = 0;
onsetR = 0;
transitT = 0;
transitR = 0;
# read the data from the file
for line in lines[18::]:  	
	list = line.split(",,,,,,,,,,,,,,,,,,,,,,")
	resistance.append(list[1].split(",")[1])
	temp.append(list[0].split(",")[2])
	if counter > -1:
		dev.append(abs((float(resistance[counter])-float(resistance[counter+1]))/(float(temp[counter])-float(temp[counter+1]))))
		if dev[counter] > 0.5 and stage == 1:
			transitT = temp[counter-1]
			transitR = resistance[counter-1] 
			stage = 2
		if dev[counter] < 0.5 and dev[counter-1]<0.5 and stage == 2:
			onsetT = temp[counter]		
			onsetR = resistance[counter]
			stage = 3
	counter += 1

Tc = round((float(onsetT)+float(transitT))/2,2)
To = round(float(onsetT),2)
Tt = round(float(transitT),2)

plt.plot(temp,resistance,'r-',temp,resistance,'b.')
plt.annotate('On set',xy = (onsetT,onsetR),xytext = (100,20),arrowprops=dict(arrowstyle = '->',connectionstyle = 'arc3'),color='b')
plt.annotate('Transit',xy = (transitT,transitR),xytext = (100,5),arrowprops=dict(arrowstyle = '->',connectionstyle = 'arc3'),color='b')
plt.figtext(0.65,0.35,'Sample A', size = 'small',color='r')
plt.figtext(0.65,0.2,'Tc = '+ str(Tc)+'K', size = 'small',color='r')
plt.figtext(0.65,0.25,'To = '+ str(To)+'K', size = 'small',color='r')
plt.figtext(0.65,0.3,'Tt = '+ str(Tt)+'K', size = 'small',color='r')

plt.savefig('resistivitySampleA+C.png')
plt.show()


