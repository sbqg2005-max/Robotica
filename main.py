import roboticstoolbox as rtb
import numpy as np
import matplotlib.pyplot as plt

from spatialmath import *
from spatialmath.base import *      

from sympy import Symbol, Matrix

#theta = Symbol('theta')
#R = Matrix(rot2(theta))
#print(R)

theta_deg = 30
theta_rad = np.deg2rad(theta_deg)

R = rot2(theta_rad)
print(R)

trplot2(R) #dibujamos en el plot

plt.axis('equal')
plt.grid(True)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Rotación 2D")
plt.show() #Mostrar ventana

# Convertir grados a radianes
theta_deg = 30
theta_rad = np.deg2rad(theta_deg)

R = rot2(theta_rad)
print(R)    

R2 = rot2(-theta_rad)
print(R2)

# Convertir grados a radianes
theta_deg = 0
theta_rad = np.deg2rad(theta_deg)

T0 = transl2(0, 0) #Referencia
trplot2(T0, frame="0", color="k") 

#Traslación de 2,2 seguida de
TA = transl2(1, 2)
print(TA)
trplot2(TA, frame="A", color="b") 

plt.axis('equal')
plt.grid(True)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Transformación 2D")
plt.show() #Mostrar ventana
