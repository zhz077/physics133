import matplotlib.pyplot as plt
from math import*
import numpy as np
from scipy import signal
resistance = []
temp = []
sus = []
file = open('R1.dat','r')
lines = file.readlines()
file.close()
mass =0.003688356786

# read the data from the file
for line in lines:  	
	list = line.split(",")
	if (list[4] != ''):
		resistance.append(float(list[4])/mass)
		temp.append(list[2])
		sus.append(mass*5000/float(list[4]))
		print mass*5000/float(list[4]) 

plt.subplot(221)

plt.plot(temp,sus,'g-',temp,sus,'b.')
plt.axis([50,300,-350,2200])
plt.ylabel('susceptibiity^-1')
plt.xlabel('temperature')
plt.title('raw data -sus')
plt.grid(True)

plt.subplot(223)
plt.plot(temp,sus,'k')
plt.axis([50,300,-350,2200])
plt.ylabel('susceptibiity^-1')
plt.xlabel('temperature')
plt.title('filtered -sus')
plt.grid(True)

# k is 
plt.subplot(222)
plt.plot(temp,resistance,'r-',temp,resistance,'b.')
plt.axis([50,300,-0.00005,0.0003])
plt.ylabel('moment')
plt.xlabel('temperature')
plt.title('raw data -moment')
plt.grid(True)

plt.subplot(224)
plt.plot(temp,resistance,'k')
plt.axis([50,300,-0.00005,0.0003])
plt.ylabel('moment')
plt.xlabel('temperature')
plt.title('filtered -moment')
plt.grid(True)

plt.savefig('EM_BEST_RUN_NONFILTERED.png')
plt.clf()



# recalibrating the data
momentR = []
tempR = []
susR = []
for line in lines:  	
	list = line.split(",")
	if (list[4] != ''):
		momentR.append(float(list[4]) + 0.00001)
		tempR.append(list[2])
		susR.append(1.0/(float(list[4])+0.00001)/5000)
		print 1.0/(float(list[4])+0.00001)/5000

plt.subplot(221)
plt.plot(tempR,susR,'g-',tempR,susR,'b.')
plt.axis([50,300,0,550])
plt.ylabel('susceptibiity^-1')
plt.xlabel('temperature')
plt.title('raw data -sus')
plt.grid(True)

plt.subplot(223)
plt.plot(tempR,susR,'k')
plt.axis([50,300,0,550])
plt.ylabel('susceptibiity^-1')
plt.xlabel('temperature')
plt.title('filtered -sus')
plt.grid(True)

# k is 
plt.subplot(222)
plt.plot(tempR,momentR,'r-',tempR,momentR,'b.')
plt.axis([50,300,0,0.0003])
plt.ylabel('moment')
plt.xlabel('temperature')
plt.title('raw data -moment')
plt.grid(True)

plt.subplot(224)
plt.plot(tempR,momentR,'k')
plt.axis([50,300,0,0.0003])
plt.ylabel('moment')
plt.xlabel('temperature')
plt.title('filtered -moment')
plt.grid(True)

plt.savefig('Recalibrated_EM_BEST_RUN_NONFILTERED.png')
plt.show()
