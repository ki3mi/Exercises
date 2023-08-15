# Datos proporcionados
moles_SO2_equilibrio = 0.15  # Moles de SO2 en el equilibrio

# Cálculo de la cantidad de SO2 en el equilibrio
def calcular_cantidad_SO2_equilibrio(Kc, moles_SO2_equilibrio):
    # Definición de la ecuación cuadrática
    def equation(x):
        if x == 0:
            return float('inf')
        else:
            return (2 * x) ** 2 / (x * (moles_SO2_equilibrio ** 2)) - Kc

    # Utilizar el método de la bisección para resolver la ecuación cuadrática
    def bisection(a, b):
        while (b - a) >= 0.0001:
            c = (a + b) / 2
            if equation(c) == 0.0:
                break
            if equation(c) * equation(a) < 0:
                b = c
            else:
                a = c
        return c

    # Resolución de la ecuación
    x = bisection(0.0001, moles_SO2_equilibrio)
    return x

# Ejemplo de uso
Kc = 2.5  # Valor de Kc para la reacción a 727°C
cantidad_SO2_equilibrio = calcular_cantidad_SO2_equilibrio(Kc, moles_SO2_equilibrio)
print("Cantidad de SO2 en el equilibrio:", cantidad_SO2_equilibrio, "moles")
