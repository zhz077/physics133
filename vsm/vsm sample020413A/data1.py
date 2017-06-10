import matplotlib.pyplot as plt
from math import*
import numpy as np
from scipy import signal
resistance1 = []
temp1 = []
sus1= []
mass = 0.007736426875
file = open('run1.dat','r')
lines = file.readlines()
file.close()

# read the data from the file
for line in lines:  	
	list = line.split(",")
	if (list[4] != ''):
		resistance1.append(float(list[4])/mass)
		temp1.append(list[2])
		sus1.append(5000*mass/float(list[4]))
		print 5000*mass/float(list[4])

moment2 = []
temp2 = []
sus2= []
file = open('run2.dat','r')
lines = file.readlines()
file.close()

for line in lines:  	
	list = line.split(",")
	if (list[4] != ''):
		moment2.append(float(list[4])/mass)
		temp2.append(list[2])
		sus2.append(5000*mass/float(list[4]))

plt.plot(temp1,resistance1,'r-',temp1,resistance1,'b.',temp2,moment2,'g-',temp2,moment2,'b.')
plt.axis([50,300,0.000045/mass,0.000075/mass])
plt.ylabel('moment')
plt.xlabel('temperature')
plt.title('raw data -moment')
plt.grid(True)
plt.figtext(0.65,0.35,'first run', size = 'small',color='r')
plt.figtext(0.65,0.2,'second run', size = 'small',color='g')
plt.savefig('two run raw.png')



b, a = signal.butter(2, 0.08)
plt.subplot(221)
y1 = signal.filtfilt(b, a, sus1)
y2 = signal.filtfilt(b, a, sus2)
plt.plot(temp1,sus1,'r-',temp1,sus1,'b.',temp2,sus2,'g-',temp2,sus2,'b.')
plt.axis([50,300,500000,850000])
plt.ylabel('susceptibiity^-1')
plt.xlabel('temperature')
plt.title('raw data -sus')
plt.figtext(0.65,0.35,'first run', size = 'small',color='r')
plt.figtext(0.65,0.2,'second run', size = 'small',color='g')
plt.grid(True)

plt.subplot(223)
plt.plot(temp1,y1,'r',temp2,y2,'g')
plt.axis([50,300,500000,850000])
plt.ylabel('susceptibiity^-1')
plt.xlabel('temperature')
plt.title('filtered -sus')
plt.grid(True)

# k is 
plt.subplot(222)
y1 = signal.filtfilt(b, a, resistance1)
y2 = signal.filtfilt(b, a, moment2)
plt.plot(temp1,resistance1,'r-',temp1,resistance1,'b.',temp2,moment2,'g-',temp2,moment2,'b.')
plt.axis([50,300,0.000045/mass,0.000075/mass])
plt.ylabel('moment')
plt.xlabel('temperature')
plt.title('raw data -moment')
plt.grid(True)

plt.subplot(224)
plt.plot(temp1,y1,'r',temp2,y2,'g')
plt.axis([50,300,0.000045/mass,0.000075/mass])
plt.ylabel('moment')
plt.xlabel('temperature')
plt.title('filtered -moment')
plt.grid(True)


plt.savefig('processed.png')
plt.show()



