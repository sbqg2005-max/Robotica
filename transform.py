import roboticstoolbox as rtb
import numpy as np
import matplotlib.pyplot as plt

from spatialmath import *
from spatialmath.base import *

#from sympy import Symbol, Matrix

#theta = Symbol('theta')
#R = Matrix(rot2(theta))
#print(R)

#theta_deg = 30
#theta_rad = np.deg2rad(theta_deg)

#R = rot2(theta_rad)
#R = trot2(theta_rad)
#print(R)

#trplot2(R) #Dibujamos en el plot
#plt.axis('equal') #Mantenemos la escala igual en ambos ejes
#plt.grid(True) #Agregamos una cuadrícula
#plt.xlabel('X') #Etiqueta del eje X
#plt.ylabel('Y') #Etiqueta del eje Y
#plt.title(f'rotación 2D') #Título del gráfico
#plt.show() #Mostramos el gráfico

#theta_deg = 30
#theta_rad = np.deg2rad(theta_deg)

#R = rot2(theta_rad)
#print(R)

theta_deg = 0
theta_rad = np.deg2rad(theta_deg)

R2 = rot2(theta_rad)
print(R2)

#T0 = transl2(0, 0)
#trplot2(T0, frame = '0', color='k')

#TA = transl2(1, 2)
#print(TA)
#trplot2(TA, frame = 'A', color='b')

#TA = transl2(1, 2) @ trot2(30, "deg")
#print(TA)
#trplot2(TA, frame = 'A', color='b')

TB = trot2(30, "deg") @ transl2(1, 2)
print(TB)
trplot2(TB, frame = 'B', color='r')

TA = transl2(1, 2) @ trot2(30, "deg")
print(TA)
trplot2(TA, frame = 'A', color='b')

P = np.array([4, 3]) #Punto en coordenadas homogéneas
plot_point(P, 'ko', text = 'p')
print(P)

P1 = homtrans(np.linalg.inv(TA), P) #Transformamos el punto P al sistema de coordenadas A
print(P1)




plt.axis('equal') #Mantenemos la escala igual en ambos ejes
plt.grid(True) #Agregamos una cuadrícula
plt.xlabel('X') #Etiqueta del eje X
plt.ylabel('Y') #Etiqueta del eje Y
plt.title('Transformación 2D') #Título del gráfico
plt.show() #Mostramos el gráfico