import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#CONO -> z=rcotan(theta)
#PIANO -> z=(pi/6)*r*cos(phi)+d

def cono(theta, raggio):
    return raggio*(1/(np.tan(theta)))

def norma(x,y,z):
    return np.sqrt(x**2+y**2+z**2)

n=1.5   #inidce di rifrazione della lastra
beta=np.sqrt(1/(n**2-1))+0.05  #velocità normalizzata della particella incidente
alpha=np.pi/6   #angolo di incidenza della particella sulla lastra
theta=np.arccos(1/(n*beta)) #angolo Cherenkov
d=1 #distanza fra origine e piano
crit=np.arcsin(1/n) #angolo critico per la riflessione totale
fired=100   #numero di fotoni emessi
phi=np.random.uniform(0, np.pi*2, fired)    #estrazione casuale della direzione del fotone
print(crit*180/np.pi)

raggio=((-d)/(alpha*np.cos(phi)-(1/np.tan(theta))))
x,y,z=raggio*np.cos(phi), raggio*np.sin(phi), cono(theta, raggio) #calcolo della punto in cui i fotoni incidono sulla superficie

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.set_aspect('equal')

normale=(np.sin(alpha),0,np.cos(alpha)) #normale alla superficie
riflessi, rifratti=0,0

#DISCRIMINAZIONE E PLOTTING 3D
for i in range (0, len(x)):
    norme=(norma(x[i],y[i],z[i]))   #calcolo della norma dei vettori che collegato i punti della superficie colpiti dai fotoni al vertice del cono
    vec=((x[i]/norme,y[i]/norme,z[i]/norme))    #normalizzazione dei vettori
    angolo = (np.arccos((np.dot(vec,normale))))-np.pi/2    #prodotto scalare fra la normale ed i vettori normalizzati per calcolare l'angolo di incidenza
    if(np.abs(angolo) > crit): #discriminazione dei fotoni secondo l'angolo di incidenza rispetto all'angolo critico
            riflessi+=1
            ax.scatter(x[i],y[i],z[i], color="blue")
    else:
            rifratti+=1
            ax.scatter(x[i],y[i],z[i], color="red")

print(str(riflessi/fired*100)+"%")  #calcolo della percentuale di fotoni che vengono riflessi
plt.show()
plt.close()

#DISCRIMINAZIONE E PLOTTING PER ANGOLO DI EMISSIONE
for i in range (0, len(x)):
    norme=(norma(x[i],y[i],z[i]))
    vec=((x[i]/norme,y[i]/norme,z[i]/norme))
    angolo = (np.arccos((np.dot(vec,normale))))-np.pi/2
    if(np.abs(angolo) > crit):
            riflessi+=1
            plt.errorbar(np.cos(phi[i]),np.sin(phi[i]), color="blue", fmt=".")
    else:
            rifratti+=1
            plt.errorbar(np.cos(phi[i]),np.sin(phi[i]), color="red", fmt=".")
plt.show()