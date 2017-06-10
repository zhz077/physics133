import matplotlib.pyplot as plt
from math import*
import numpy as np
from scipy import signal
resistance = []
temp = []
sus = []
mass = 0.002268260714
file = open('R1.dat','r')
lines = file.readlines()
file.close()

# read the data from the file
for line in lines:  	
	list = line.split(",")
	if (list[4] != ''):
		resistance.append(float(list[4])/mass)
		temp.append(list[2])
		sus.append(mass*5000/float(list[4]))
		print mass*5000/float(list[4])
def curie(t,tc,c):
	return (t-tc)/c
init_vals=[70,2]
best_vals, covar = curve_fit(curie,t, sus,  p0=init_vals)
b, a = signal.butter(2, 0.08)

plt.subplot(221)
y = signal.filtfilt(b, a, sus)
plt.plot(temp,sus,'g-',temp,y,'k',temp,sus,'b.')
plt.axis([50,300,80000,102000])
plt.ylabel('susceptibiity^-1')
plt.xlabel('temperature')
plt.title('raw data -sus')
plt.grid(True)

plt.subplot(223)
b, a = signal.butter(2, 0.08)
y = signal.filtfilt(b, a, sus)
plt.plot(temp,y,'k')
plt.axis([50,300,80000,102000])
plt.ylabel('susceptibiity^-1')
plt.xlabel('temperature')
plt.title('filtered -sus')
plt.grid(True)

# k is 
plt.subplot(222)
b, a = signal.butter(2, 0.08)
y = signal.filtfilt(b, a, resistance)
plt.plot(temp,resistance,'r-',temp,y,'k',temp,resistance,'b.')
plt.axis([50,300,0.0001/mass,0.000145/mass])
plt.ylabel('moment')
plt.xlabel('temperature')
plt.title('raw data -moment')
plt.grid(True)

plt.subplot(224)
b, a = signal.butter(2, 0.08)
y = signal.filtfilt(b, a, resistance)
plt.plot(temp,y,'k')
plt.axis([50,300,0.0001/mass,0.000145/mass])
plt.ylabel('moment')
plt.xlabel('temperature')
plt.title('filtered -moment')
plt.grid(True)

plt.savefig('EM_BEST_RUN_NONFILTERED.png')
plt.show()


