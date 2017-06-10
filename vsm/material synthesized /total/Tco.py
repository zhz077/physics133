import matplotlib.pyplot as plt
from math import*
from numpy import linspace
x1 = round(0.28/0.08,2)
x5 = round(0.48/0.08,2)
plt.plot([0,0.01,0.05],[1,x1,x5],'ro',[0,0.01,0.05],[1,x1,x5],'b-',)
plt.axis([0,0.06,0,6.5])
plt.annotate('(0,1)', xytext = (0,1.1),xy=(0,1.1))
plt.annotate('(0.1,'+ str(1) +')', xytext = (0.01,4),xy=(0.01,4))
plt.annotate('(0.5,'+ str(1) +')', xytext = (0.04,6),xy=(0.04,6))
plt.ylabel(r'$\mu_{eff}/\mu_{eff_0}$')
plt.xlabel('X in '+r'$Li(Ti_{1-x}V_x)_2O_4$')
plt.title('ratio of effective magnetic moment')
plt.grid(True)
plt.savefig('ratio of effective magnetic moment.png')
plt.show()
