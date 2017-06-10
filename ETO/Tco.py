import matplotlib.pyplot as plt
from math import*
from numpy import linspace
x1 = round(10.6/9.8,2)
x5 = round(8.8/9.8,2)
plt.plot([0,0.01,0.05],[1,1,1],'ro',[0,0.01,0.05],[1,1,1],'b-',)
plt.axis([0,0.06,0,1.2])
plt.annotate('(0,1)', xytext = (0,1.1),xy=(0,1.1))
plt.annotate('(0.1,'+ str(1) +')', xytext = (0.01,1.1),xy=(0.01,1.1))
plt.annotate('(0.5,'+ str(1) +')', xytext = (0.05,1.1),xy=(0.05,1.1))
plt.ylabel(r'$T_o/T_{o_0}$')
plt.xlabel('X in '+r'$Li(Ti_{1-x}V_x)_2O_4$')
plt.title('ratio of onset temperature')
plt.grid(True)
plt.savefig('ratio of onset temperature with new measurement x=0.05.png')
plt.show()
