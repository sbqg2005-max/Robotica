import sympy as sp
from spatialmath import *
from spatialmath.base import *
import matplotlib.pyplot as plt
import numpy as np
import roboticstoolbox as rtb

# 1. Creación del robot de 6 grados de libertad (todas son articulaciones de revolución)
robot_abb = rtb.DHRobot([
    rtb.RevoluteDH(d=0.660, a=0.300, alpha=np.deg2rad(90), qlim=np.deg2rad([-0.150, 0.150])),
    rtb.RevoluteDH(d=0, a=1.200,    alpha=0, offset=np.deg2rad(90), qlim=np.deg2rad([-0.065, 150])),
    rtb.RevoluteDH(d=0, a=0.213, alpha=np.deg2rad(90), qlim=np.deg2rad([-0.070, 0.070])),
    rtb.RevoluteDH(d=1.620, a=0, alpha=0, qlim=np.deg2rad([-0.720, 0.720])),
    rtb.RevoluteDH(d=0, a=0, alpha=0, qlim=np.deg2rad([-0.720, 0.720])),
    # rtb.RevoluteDH(d=0, a=0, alpha=0, qlim=np.deg2rad([-0.720, 0.720])),
], name='ABB CRB 1500', base=SE3(0, 0, 0))

print(robot_abb)


joint1 = np.deg2rad(0)
joint2 = np.deg2rad(0)
joint3 = np.deg2rad(0) 
joint4 = np.deg2rad(0)
joint5 = np.deg2rad(0)

q_pos = [joint1, joint2, joint3, joint4, joint5]

# Cinemática directa hasta el efector final
T06DH = robot_abb.fkine(q_pos) 
print("\nTransformación Total (Base a Efector Final):")
print(T06DH)

# Transformaciones de todos los eslabones
T06DH_all = robot_abb.fkine_all(q_pos)
print("\nTransformaciones intermedias:")
for i in range(1, 6):
    print(f"Eslabón {i}: \n", T06DH_all[i])

# 3. Definir variables articulares para la trayectoria (Debe tener 6 columnas)
# q = np.array([  
#     [0, 0, 0, 0, 0, 0],
#     [joint1, 0, 0, 0, 0, 0],
#     [joint1, joint2, 0, 0, 0, 0],
#     [joint1, joint2, joint3, 0, 0, 0],
#     [joint1, joint2, joint3, joint4, 0, 0],
#     [joint1, joint2, joint3, joint4, joint5, 0],
#     [joint1, joint2, joint3, joint4, joint5, joint6],
#     [joint1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0]
# ])

# # Para graficar (descomenta la que necesites usar)
# # robot_abb.plot(q=q, backend='pyplot', dt=3, shadow=True, jointaxes=True)
# # robot_abb.plot(q=q, backend='pyplot', dt=3, shadow=True, jointaxes=True, movie='robot.gif')

# # 4. Graficar con el controlador manual (teach)
# q_teach = np.array([0, 0, 0, 0, 0, 0])
# robot_abb.teach(q_teach)