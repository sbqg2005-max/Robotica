# ==========================================
# Mitsubishi RV-5AS-D (6R)
# Implementación DH en Robotics Toolbox
# ==========================================

import numpy as np
import roboticstoolbox as rtb
from spatialmath import SE3

# ------------------------------------------
# Definición del robot (estructura 6R clásica tipo industrial)
# Unidades: metros, radianes
# ------------------------------------------

rv5as = rtb.DHRobot(
    [
        # J1
        rtb.RevoluteDH(d=0.330, a=0.050, alpha=np.pi/2, qlim=[-2.9, 2.9]),

        # J2
        rtb.RevoluteDH(d=0.0, a=0.450, alpha=0.0, qlim=[-2.0, 2.0]),

        # J3
        rtb.RevoluteDH(d=0.0, a=0.400, alpha=0.0, qlim=[-2.5, 2.5]),

        # J4
        rtb.RevoluteDH(d=0.420, a=0.0, alpha=np.pi/2, qlim=[-3.14, 3.14]),

        # J5
        rtb.RevoluteDH(d=0.0, a=0.0, alpha=-np.pi/2, qlim=[-2.2, 2.2]),

        # J6
        rtb.RevoluteDH(d=0.080, a=0.0, alpha=0.0, qlim=[-6.28, 6.28]),
    ],
    name="Mitsubishi_RV5AS_D",
    base=SE3(0, 0, 0)
)

print(rv5as)

# ------------------------------------------
# Validación HOME (todos los joints en 0)
# ------------------------------------------

q_home = [0, 0, 0, 0, 0, 0]

T_home = rv5as.fkine(q_home)

print("\nT06 en HOME:")
print(T_home)

print("\nPosición HOME [x y z] (m):")
print(T_home.t)

# ------------------------------------------
# Plot del robot (para reporte)
# ------------------------------------------

rv5as.plot(q_home, backend="pyplot", shadow=True, jointaxes=True)