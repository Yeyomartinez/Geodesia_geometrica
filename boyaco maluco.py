import math

def calcular_volumen_y_area(opcion):
    if opcion == 1:
        a_axis = 6378388
        b_axis = 6356911.946129013
    elif opcion == 2:
        a_axis = 1
        b_axis = 1
    else:
        return "Opción no válida"

    a = a_axis
    b = b_axis
    volumen = (4/3) * math.pi * (a**2) * b
    area = 4 * math.pi * a * b
    return volumen, area


print("Seleccione el tipo de elipsoide:")
print("1. Elipsoide Internacional")
print("2. WGS84")
opcion = int(input("Ingrese su opción: "))
resultado_volumen, resultado_area = calcular_volumen_y_area(opcion)
if isinstance(resultado_volumen, str):
    print(resultado_volumen)
else:
    print("El volumen es:", resultado_volumen)
    print("El área es:",resultado_area)