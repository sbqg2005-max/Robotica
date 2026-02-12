import math

def area_esfera(radio):
    """
    Calcula el área de una esfera.
    
    Fórmula: A = 4πr²
    
    Args:
        radio: El radio de la esfera
        
    Returns:
        El área de la esfera
    """
    if radio < 0:
        raise ValueError("El radio no puede ser negativo")
    
    area = 4 * math.pi * (radio ** 2)
    return area


if __name__ == "__main__":
    # Ejemplo de uso
    radio = 5
    resultado = area_esfera(radio)
    print(f"Radio: {radio}")
    print(f"Área de la esfera: {resultado:.2f}")
