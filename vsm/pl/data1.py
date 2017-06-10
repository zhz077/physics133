import matplotlib.pyplot as plt
from math import*
import numpy 
from scipy import signal
import scipy.optimize as optimization

resistance = []
temp = []
sus = []
mass = 0.2581
dev = []
counter=-1
file = open('R1.dat','r')
lines = file.readlines()
file.close()
# read the data from the file
for line in lines:  	
	list = line.split(",")
	if (list[4] != ''):
		resistance.append(float(list[4])/mass)
		temp.append(list[2])
		sus.append(5000*mass/float(list[4]))

		if counter > -1:
			dev.append(abs((sus[counter]-sus[counter+1])/(float(temp[counter])-float(temp[counter+1]))))
			print dev[counter]
		counter += 1
		



plt.subplot(221)

plt.plot(temp,sus,'g-',temp,sus,'b.')
plt.axis([50,300,120000,190000])
plt.ylabel('susceptibiity^-1')
plt.xlabel('temperature')
plt.title('raw data -sus')
plt.grid(True)

plt.subplot(223)
plt.plot(temp,sus,'k')
plt.axis([50,300,120000,190000])
plt.ylabel('susceptibiity^-1')
plt.xlabel('temperature')
plt.title('filtered -sus')
plt.grid(True)

# k is 
plt.subplot(222)
plt.plot(temp,resistance,'r-',temp,resistance,'b.')
plt.axis([50,300,0.025,0.04])
plt.ylabel('moment')
plt.xlabel('temperature')
plt.title('raw data -moment')
plt.grid(True)

plt.subplot(224)
plt.plot(temp,resistance,'k')
plt.axis([50,300,0.025,0.04])
plt.ylabel('moment')
plt.xlabel('temperature')
plt.title('filtered -moment')
plt.grid(True)

plt.savefig('EM_BEST_RUN_NONFILTERED.png')
plt.show()