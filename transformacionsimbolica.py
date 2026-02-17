import roboticstoolbox as rtb
import numpy as np
import matplotlib.pyplot as plt

from spatialmath import *
from spatialmath.base import *

import numpy as np
from sympy import *
from sympy import Symbol, Matrix, simplify
from sympy.matrices import rot_axis3

# Configuración para imprimir números pequeños como 0
np.set_printoptions(
    formatter={'float': lambda x: f"{0:8.4g}" if abs(x) < 1e-10 else f"{x:8.4g}"}
)

# =========================
# Definición de funciones
# =========================

def trotz(theta):
    """Matriz de rotación homogénea alrededor del eje Z"""
    return Matrix([
        [cos(theta), -sin(theta), 0, 0],
        [sin(theta),  cos(theta), 0, 0],
        [0,           0,          1, 0],
        [0,           0,          0, 1]
    ])

def transl(x, y, z):
    """Matriz de traslación homogénea"""
    return Matrix([
        [1, 0, 0, x],
        [0, 1, 0, y],
        [0, 0, 1, z],
        [0, 0, 0, 1]
    ])

# =========================
# Variables simbólicas
# =========================

theta1, L1, theta2, L2 = symbols("theta1 L1 theta2 L2")

# =========================
# Transformaciones
# =========================

T01 = trotz(theta1) @ transl(L1, 0, 0)
print(f"Primera transformación:\n{T01}\n")

T12 = trotz(theta2) @ transl(L2, 0, 0)
print(f"Segunda transformación:\n{T12}\n")

# Transformación completa
T02 = T01 @ T12
print(f"Transformación completa:\n{T02}\n")

# =========================
# Simplificación
# =========================

M = Matrix(T02)
M_simplified = M.applyfunc(simplify)

# =========================
# Mejor visualización
# =========================

def nice_print_matrix(matrix):
    return '\n'.join(
        [' '.join([str(entry.evalf()) for entry in row]) 
         for row in matrix.tolist()]
    )

print("Matriz simplificada:")
print(nice_print_matrix(M_simplified))
print("\n")

M_evaluated = M_simplified.subs({theta1: np.deg2rad(30), L1: 4, theta2: np.deg2rad(0), L2: 3}).evalf()
print(nice_print_matrix(M_evaluated))
