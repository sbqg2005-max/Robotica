import sympy as sp
from sympy.matrices import rot_axis3
# Para el ejemplo donde generamos la matriz DH
from spatialmath import *
from spatialmath.base import *
# Para poder graficar
import matplotlib.pyplot as plt
plt.ion()
import numpy as np
# Para usar el DH
import roboticstoolbox as rtb

scara = rtb.DHRobot(
[
    rtb.RevoluteDH(d=0.544, a=0, alpha=np.deg2rad(90),     qlim=[-0.180, 0.180]),
    rtb.RevoluteDH(d=0, a=0.425,    alpha=0, offset=np.deg2rad(90), qlim=[-0.100, 0.130]),
    rtb.RevoluteDH(d=0,     a=0.040, alpha=np.deg2rad(90),     qlim=[-0.210, 0.065]),
    rtb.RevoluteDH(d=0.565,     a=0,     alpha=np.deg2rad(-90),     qlim=[-0.230, 0.230]),
    rtb.RevoluteDH(d=0,     a=0,     alpha=np.deg2rad(90),     qlim=[-0.130, 0.130]),
], name="IRB1300-11", base=SE3(0, 0, 0))
print(scara)

joint1 = np.deg2rad(0)
joint2 = np.deg2rad(0)
joint3 = np.deg2rad(0)  
joint4 = np.deg2rad(0)
joint5 = np.deg2rad(0)
T04DH = scara.fkine([joint1, joint2, joint3, joint4, joint5])  # Lo definimos asi por el offset
print(T04DH)

# #T04DH_all = scara.fkine_all([joint1, joint2, joint3, joint4])

# #print(T04DH_all[1])
# #print(T04DH_all[2])
# #print(T04DH_all[3])
# #print(T04DH_all[4])

# # Definir variables articulares
# q = np.array([[0, 0, 0, 0],
#               [joint1, 0, 0, 0], 
#               [joint1, joint2, 0, 0],
#               [joint1, joint2, joint3, 0],
#               [joint1, joint2, joint3, joint4],
#               [joint1, joint2, joint3, 0],
#               [joint1, joint2, 0, 0],
#               [joint1, 0, 0, 0],
#               [0, 0, 0, 0]])

# # Graficar con posiciones q, una cada 3 segundos
# scara.plot(q=q, backend='pyplot', block=True, dt=3, limits=[-0.8, 0.8, -0.8,0.8,0,0.6])
# plt.show(block=True)

# q1 = np.array([[0, 0, 0, 0,]])
# scara.teach(q1)