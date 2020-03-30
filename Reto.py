import numpy as np
import matplotlib.pyplot as plt

plt.style.use("default")

N = 12
gmin= -2
gmax= 2

x=np.linspace(gmin,gmax,N)
y=np.linspace(gmin,gmax,N)
X,Y=np.meshgrid(x,y)

k= 9e9
q=20e-6
r2=(X**2)+(Y**2)
E=(k*q)/(r2)

if (q<0):
    c1="black"
if (q>0):
    c1="red"

comp = X + (Y * 1j)
angle=np.angle(comp)
Ex=E*(np.cos(angle))
Ey=E*(np.sin(angle))

fig, ax= plt.subplots(figsize=(7,7))

ax.quiver(X,Y,Ex,Ey)
ax.scatter(0,0,c=c1,s=1000)
ax.axis([-2,2,-2,2])
ax.set_aspect("equal","box")

mags=np.sqrt((Ex**2)+(Ey**2))

Ex_u= Ex/mags
Ey_u= Ey/mags

fig, ax = plt.subplots(figsize=(7,7))

ax.quiver(X,Y,Ex_u,Ey_u)
ax.scatter(0,0,c='red',s=1000)
ax.axis([-2,2,-2,2])
ax.set_aspect('equal','box')
plt.show()

#Paso 2

N=21
gmin=-5
gmax=5

x=np.linspace(gmin,gmax,N)
y=np.linspace(gmin,gmax,N)
X,Y= np.meshgrid(x,y)

qloc=[-2,0]
if (q<0):
    c1="black"
if (q>0):
    c1="red"

X_new= X+2
Y_new= Y

comp = X_new + (Y_new * 1j)
angle=np.angle(comp)

r2=(X_new**2)+(Y_new**2)
En=(k*q)/(r2)
Ex=En*(np.cos(angle))
Ey=En*(np.sin(angle))

mags=np.sqrt((Ex**2)+(Ey**2))

Ex_u= Ex/mags
Ey_u= Ey/mags

fig, ax = plt.subplots(figsize = (7,7))

ax.quiver(X,Y,Ex_u,Ey_u)
ax.scatter(qloc[0],qloc[1],c=c1,s=1000)
ax.axis([gmin,gmax,gmin,gmax])
ax.set_aspect('equal','box')

#Paso 3

N=21
gmin=-5
gmax=5

x=np.linspace(gmin,gmax,N)
y=np.linspace(gmin,gmax,N)
X,Y= np.meshgrid(x,y)

k=9e9
q=20e-6
qloc=[-2,-1]

if (q<0):
    c1="black"
if (q>0):
    c1="red"

X_new= X-qloc[0]
Y_new= Y-qloc[1]

comp = X_new + (Y_new * 1j)
angle=np.angle(comp)

r2=(X_new**2)+(Y_new**2)
En=(k*q)/(r2)
Ex=En*(np.cos(angle))
Ey=En*(np.sin(angle))

k = 9e9
q2 = -20e-6
qloc2 = [2, 1]

if (q2 < 0):
    c2 = "black"
if (q2 > 0):
    c2 = "red"

X_new2 = X - qloc2[0]
Y_new2 = Y - qloc2[1]

comp2 = X_new2 + (Y_new2 * 1j)
angle2 = np.angle(comp2)

r22 = (X_new2 ** 2) + (Y_new2 ** 2)
En2 = (k * q2) / (r22)
Ex2 = En2 * (np.cos(angle2))
Ey2 = En2 * (np.sin(angle2))

Ext= Ex+Ex2
Eyt= Ey+Ey2

mags=np.sqrt((Ext**2)+(Eyt**2))

Ex_ut= Ext/mags
Ey_ut= Eyt/mags

fig, ax = plt.subplots(figsize = (7,7))

ax.quiver(X,Y,Ex_ut,Ey_ut)
ax.scatter(qloc[0],qloc[1],c=c1,s=1000)
ax.scatter(qloc2[0],qloc2[1],c=c2,s=1000)

ax.axis([gmin,gmax,gmin,gmax])
ax.set_aspect('equal','box')
plt.show()