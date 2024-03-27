import math

def elipsoides():
    print("Seleccione el elipsoide a utilizar:")
    print("1) Internacional (1924)")
    print("2) GRS - 80")
    print("3) WGS - 84")
    print("4) Airy (1830)")
    print("5) Bessel (1841)")
    print("6) Clarke (1866)")
    print("7) Everest (1830)")
    print("8) Hayford (1910)")
    print("9) Krassovsky (1940)")
    print("10) WGS - 72")
    
    Seleccionar_variable = int(input("Ingrese el número correspondiente al elipsoide: "))
    
    if Seleccionar_variable == 1:
        a = 6378388.0
        e = 0.00672267002278908
    elif Seleccionar_variable == 2:
        a = 6378137.0
        e = 0.00669438002290
    elif Seleccionar_variable == 3:
        a = 6378137.0
        e = 0.006694379990
    elif Seleccionar_variable == 4:
        a = 6377563.396
        e = 0.00667054004120
    elif Seleccionar_variable == 5:
        a = 6377397.155
        e = 0.006674372229629
    elif Seleccionar_variable == 6:
        a = 6378206.4
        e = 0.006768658
    elif Seleccionar_variable == 7:
        a = 6377276.345
        e = 0.006637847
    elif Seleccionar_variable == 8:
        a = 6378388.0
        e = 0.00672267002278908
    elif Seleccionar_variable == 9:
        a = 6378245.0
        e = 0.006693421622965943
    elif Seleccionar_variable == 10:
        a = 6378135.0
        e = 0.006694318
    else:
        print("OPCIÓN NO VÁLIDA")
    
    return a, e

def seleccionar_phi():
    Seleccionar_norte_sur = int(input("Seleccione (1) si su latitud es norte, o a su vez seleccione (2) si su latitud es sur: "))
    valor_phi_grados = float(input("Ingrese el valor de φ en grados: "))
    valor_phi_minutos = float(input("Ingrese el valor de φ en minutos: "))
    valor_phi_segundos = float(input("Ingrese el valor de φ en segundos: "))
    
    Calculo_de_phi_decimal = valor_phi_grados + valor_phi_minutos/60 + valor_phi_segundos/3600
    
    if Seleccionar_norte_sur == 1:
        resultado_ns = Calculo_de_phi_decimal * 1
    elif Seleccionar_norte_sur == 2:
        resultado_ns = Calculo_de_phi_decimal * -1
    else:
        print("NO VALIDO")
        
    resultado_ns_rad = math.radians (resultado_ns)
        
    return (resultado_ns_rad)

def seleccionar_lambda():
    Seleccionar_lambda_e_w = int(input("Seleccione (1) si su longitud es ESTE, o a su vez seleccione (2) si su longitud es WEST: "))
    valor_lambda_grados = float(input("Ingrese el valor de λ en grados: "))
    valor_lambda_minutos = float(input("Ingrese el valor de λ en minutos: "))
    valor_lambda_segundos = float(input("Ingrese el valor de λ en segundos: "))
    
    Calculo_de_lambda_decimal = valor_lambda_grados + valor_lambda_minutos/60 + valor_lambda_segundos/3600
    
    if Seleccionar_lambda_e_w == 1:
        resultado_ew = Calculo_de_lambda_decimal * 1
    elif Seleccionar_lambda_e_w == 2:
        resultado_ew = Calculo_de_lambda_decimal * -1
    else:
        print("NO VALIDO")
        
    resultado_ew_rad = math.radians (resultado_ew)
        
    return (resultado_ew_rad)
def seleccionar_altura():
    altura_ortometrica = float(input("Djite a altura sobre el nuvel del mar en M: "))
    return(altura_ortometrica)

def calculo_N_xyz (a, e, resultado_ns_rad):
    calculo_N =  a / math.sqrt(1 - e * (math.sin(resultado_ns_rad)**2))
    return(calculo_N)
def calculo_x_h (a, e, calculo_N, altura_ortometrica, resultado_ew_rad, resultado_ns_rad):
    calculo_x = (calculo_N + altura_ortometrica)*math.cos(resultado_ns_rad)*math.cos(resultado_ew_rad)
    print ("el valor de X = ", calculo_x)
    return()
def calculo_y_h (a, e, calculo_N, altura_ortometrica, resultado_ew_rad, resultado_ns_rad):
    calculo_y = (calculo_N + altura_ortometrica)*math.cos(resultado_ns_rad)*math.sin(resultado_ew_rad)
    print ("el valor de Y = ", calculo_y)
    return()
def calculo_z_h (a, e, calculo_N, altura_ortometrica, resultado_ns_rad):
    calculo_z = (calculo_N*(1-e)+altura_ortometrica)*math.sin(resultado_ns_rad)
    print ("el valor de Z = ", calculo_z)
    return()

a,e = elipsoides()
resultado_ns_rad = seleccionar_phi()
resultado_ew_rad = seleccionar_lambda()
altura_ortometrica = seleccionar_altura()
calculo_N = calculo_N_xyz (a, e, resultado_ns_rad)
calculo_x_h (a, e, calculo_N, altura_ortometrica, resultado_ew_rad, resultado_ns_rad)
calculo_y_h (a, e, calculo_N, altura_ortometrica, resultado_ew_rad, resultado_ns_rad)
calculo_z_h (a, e, calculo_N, altura_ortometrica, resultado_ns_rad)

