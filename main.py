import numpy as np
from matplotlib import pylab as plt
from scipy.optimize import curve_fit
import random

n=1.5

b=np.linspace(0.0001,1,10000)
def cherenkov (b,n):
    return np.arccos(1/(b*n))

crit=[np.arcsin(1/n)]*len(b)
blim=[np.sqrt(1/(n**2-1))]*len(b)

plt.plot(b, cherenkov(b,n), color="black")
plt.xlim(0,1)
plt.grid(color="grey", alpha=0.5)
plt.plot(b, crit, alpha=0.75)
plt.plot(blim, b, color="red",alpha=0.75)
plt.ylim(0,1)
plt.ylabel("Angolo Cherenkov [radianti]")
plt.xlabel("Velocità della carica normalizzata")
plt.text(0.05,0.9,"n="+str(n))
#plt.show()
plt.close()

shots=100
phi=[]
for i in range (0, shots):
    phi.append(random.randint(0,360))

for i in range (0, len(phi)):
    phi[i]=phi[i]*((np.pi)/(180))
print(len(phi), phi)

b=np.sqrt(1/(n**2-1))+0.05
crit=np.arcsin(1/n)


incidenza=np.pi/6

for a in phi:
    angolo=(incidenza)+np.cos(a)*cherenkov(b,n)
    x=np.cos(a)
    y=np.sin(a)
    if(angolo > crit):
        plt.errorbar(x,y, fmt=".", color="blue")
    else:
        plt.errorbar(x,y, fmt=".", color="red")
plt.show()