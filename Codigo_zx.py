import math
import numpy as np
import matplotlib.pyplot as plt

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

def seleccionar_tipo_de_transformacion():
    print ("Seleccione el tipo de latitud a ingresar: ")
    print ("1) ELIPSOIDAL")
    print ("2) GEOCENTRICA")
    print ("3) PARAMETRICA")
    Seleccionar_variable = int(input("Ingrese aqui:  "))
    
    if Seleccionar_variable == 1:
        def nortesur():
            Seleccionar_norte_sur = int(input("Seleccione (1) si su latitud es norte, o a su vez seleccione (2) si su latitud es sur: "))
            valor_phi_grados = float(input("Ingrese el valor para φ en grados: "))
            valor_phi_minutos = float(input("Ingrese el valor para φ en minutos: "))
            valor_phi_segundos = float(input("Ingrese el valor para φ en segundos: "))
    
            Calculo_de_phi_decimal = valor_phi_grados + valor_phi_minutos/60 + valor_phi_segundos/3600
    
            if Seleccionar_norte_sur == 1:
                resultado_ns = Calculo_de_phi_decimal * 1
            elif Seleccionar_norte_sur == 2:
                resultado_ns = Calculo_de_phi_decimal * -1
            else:
                print("NO VALIDO")
        
            resultado_ns_rad = math.radians (resultado_ns)
        
            return (resultado_ns_rad)

        def calculo_de_transformacion(a, e, resultado_ns_rad):
            calculo_de_w = math.degrees(math.atan((math.tan(resultado_ns_rad) * (1 - e))))
            ang_w_rad = math.radians(calculo_de_w)
    
            grados_0 = abs(int(calculo_de_w))
            grados_0_sin_abs = int(calculo_de_w)
            minutos_dec_0 = (calculo_de_w - grados_0_sin_abs) * 60
            minutos_0 = abs(int(minutos_dec_0))
            minutos_0_sin_abs = int(minutos_dec_0)
            segundos_0 = abs((minutos_dec_0 - minutos_0_sin_abs) * 60)
            visualizacion_phi = f"{grados_0}° {minutos_0}' {segundos_0:.5f}\""
    
            if calculo_de_w >= 0:
                print("Su valor de ω:", visualizacion_phi, "N")
            elif calculo_de_w <= 0:
                print("Su valor de ω:", visualizacion_phi, "S")
            else:
                print("Su valor de ω:", visualizacion_phi, "ECUADOR")
        
            return ang_w_rad
        def calculo_de_phi_en_tetha(a, e, resultado_ns_rad):
            calculo_de_tetha = math.degrees(math.atan(math.tan(resultado_ns_rad) * math.sqrt(1 - e)))
            ang_tetha_rad = math.radians(calculo_de_tetha)
    
            grados_0 = abs(int(calculo_de_tetha))
            grados_0_sin_abs = int(calculo_de_tetha)
            minutos_dec_0 = (calculo_de_tetha - grados_0_sin_abs) * 60
            minutos_0 = abs(int(minutos_dec_0))
            minutos_0_sin_abs = int(minutos_dec_0)
            segundos_0 = abs((minutos_dec_0 - minutos_0_sin_abs) * 60)
            visualizacion_phi = f"{grados_0}° {minutos_0}' {segundos_0:.5f}\""
    
            if calculo_de_tetha >= 0:
                print("Su valor de θ:", visualizacion_phi, "N")
            elif calculo_de_tetha <= 0:
                print("Su valor de θ:", visualizacion_phi, "S")
            else:
                print("Su valor de θ:", visualizacion_phi, "ECUADOR")
                
            return ang_tetha_rad 
        def calculo_de_coodernadas_xz_phi(a, e, resultado_ns_rad):
            
            N = a / math.sqrt(1 - e * (math.sin(resultado_ns_rad) ** 2))
            x_phi = N * math.cos(resultado_ns_rad)
            z_phi = N * (1 - e) * math.sin(resultado_ns_rad)
    
            print("Los valores de x en φ= ", x_phi)
            print("Los valores de z en φ= ", z_phi)
    
    
            return x_phi, z_phi

        def calculo_de_coordendas_xz_w(a, e, ang_w_rad):
            
            RgP = a * math.sqrt(1 - e)
            w = math.sqrt(1 - e * (math.cos(ang_w_rad) ** 2))
            Rg = RgP / w
            x_w = Rg * math.cos(ang_w_rad)
            z_w = Rg * math.sin(ang_w_rad)
    
            print("Los valores de x en ω= ",x_w)
            print("Los valores de z en ω= ",z_w)
    
            return x_w, z_w     

        def calculo_de_coordendas_xz_0(a, e, ang_tetha_rad):
            b = a * math.sqrt(1 - e)
            x_0 = a * math.cos(ang_tetha_rad)
            z_0 = b * math.sin(ang_tetha_rad)
    
            print("Los valores de x en θ= ", x_0)
            print("Los valores de z en θ= ", z_0)
    
            return x_0, z_0
        
        def elipse_meridiana(a, e,x_0, z_0, x_w, z_w, x_phi, z_phi ):
            semieje_a = a
            semieje_b = a * math.sqrt(1 - e)
 
            theta = np.linspace(-np.pi/2, np.pi/2, 100)  

            x = semieje_a * np.cos(theta)
            y = semieje_b * np.sin(theta)
    
            plt.figure()
            plt.scatter(x_0, z_0, color='blue', label='Punto θ')
            plt.scatter(x_w*1.001, z_w*1.001, color='red', label='Punto ω')
            plt.scatter(x_phi*1.002, z_phi*1.002, color='green', label='Punto φ')
            plt.plot(x, y)
            plt.axhline(0, color='black', linestyle='-', linewidth=1, label = "Ecuador")
            plt.scatter(0, 0, color='black')
            plt.xlabel('Eje x')
            plt.ylabel('Eje z')
            plt.title('Elipse Meridiana')
            plt.gca().set_aspect('equal', adjustable='box')
            plt.grid(True)
            plt.legend()
            plt.show()
            
        resultado_ns_rad = nortesur()
        ang_w_rad = calculo_de_transformacion(a, e, resultado_ns_rad)
        ang_tetha_rad = calculo_de_phi_en_tetha(a, e, resultado_ns_rad)
        x_phi, z_phi = calculo_de_coodernadas_xz_phi(a, e, resultado_ns_rad)
        x_w, z_w = calculo_de_coordendas_xz_w(a, e, ang_w_rad)
        x_0, z_0 = calculo_de_coordendas_xz_0(a, e, ang_tetha_rad)
        elipse_meridiana(a, e,x_0, z_0, x_w, z_w, x_phi, z_phi )
        
    elif Seleccionar_variable == 2:
        def nortesur():
            Seleccionar_norte_sur = int(input("Seleccione (1) si su latitud es norte, o a su vez seleccione (2) si su latitud es sur: "))
            valor_w_grados = float(input("Ingrese el valor de ω en grados: "))
            valor_w_minutos = float(input("Ingrese el valor de ω en minutos: "))
            valor_w_segundos = float(input("Ingrese el valor de ω en segundos: "))
    
            Calculo_de_w_decimal = valor_w_grados + valor_w_minutos/60 + valor_w_segundos/3600
    
            if Seleccionar_norte_sur == 1:
                resultado_ns_w = Calculo_de_w_decimal * 1
            elif Seleccionar_norte_sur == 2:
                resultado_ns_w = Calculo_de_w_decimal * -1
            else:
                print("NO VALIDO")
        
            resultado_ns_rad_w = math.radians (resultado_ns_w)
        
            return (resultado_ns_rad_w)
        
        def calculo_de_phi_en_w(resultado_ns_rad_w, e):
            calculo_w_phi = math.degrees(math.atan(math.tan(resultado_ns_rad_w)/(1-e)))
            ang_phi_rad = math.radians(calculo_w_phi)
    
            grados_0 = abs(int(calculo_w_phi))
            grados_0_sin_abs = int(calculo_w_phi)
            minutos_dec_0 = (calculo_w_phi - grados_0_sin_abs) * 60
            minutos_0 = abs(int(minutos_dec_0))
            minutos_0_sin_abs = int(minutos_dec_0)
            segundos_0 = abs((minutos_dec_0 - minutos_0_sin_abs) * 60)
            visualizacion_phi = f"{grados_0}° {minutos_0}' {segundos_0:.5f}\""
    
            if calculo_w_phi >= 0:
                print("Su valor de φ:", visualizacion_phi, "N")
            elif calculo_w_phi <= 0:
                print("Su valor de φ:", visualizacion_phi, "S")
            else:
                print("Su valor de φ:", visualizacion_phi, "ECUADOR")
        
            return ang_phi_rad
        
        def calculo_de_w_en_theta(resultado_ns_rad_w, e):
            calculo_w_0 = math.degrees(math.atan(math.tan(resultado_ns_rad_w)/math.sqrt(1-e)))
            ang_0_rad = math.radians(calculo_w_0)
            grados_0 = abs(int(calculo_w_0))
            grados_0_sin_abs = int(calculo_w_0)
            minutos_dec_0 = (calculo_w_0 - grados_0_sin_abs) * 60
            minutos_0 = abs(int(minutos_dec_0))
            minutos_0_sin_abs = int(minutos_dec_0)
            segundos_0 = abs((minutos_dec_0 - minutos_0_sin_abs) * 60)
            visualizacion_phi = f"{grados_0}° {minutos_0}' {segundos_0:.5f}\""
    
            if calculo_w_0 >= 0:
                print("Su valor de θ:", visualizacion_phi, "N")
            elif calculo_w_0 <= 0:
                print("Su valor de θ:", visualizacion_phi, "S")
            else:
                print("Su valor de θ:", visualizacion_phi, "ECUADOR")
        
            return ang_0_rad
        
        def calculo_de_coodernadas_xz_phi(a, e, ang_phi_rad):
            
            N = a / math.sqrt(1 - e * (math.sin(ang_phi_rad) ** 2))
            x_phi = N * math.cos(ang_phi_rad)
            z_phi = N * (1 - e) * math.sin(ang_phi_rad)
    
            print("Los valores de x en φ= ", x_phi)
            print("Los valores de z en φ= ", z_phi)
    
    
            return x_phi, z_phi

        def calculo_de_coordendas_xz_w(a, e, resultado_ns_rad_w):
            
            RgP = a * math.sqrt(1 - e)
            w = math.sqrt(1 - e * (math.cos(resultado_ns_rad_w) ** 2))
            Rg = RgP / w
            x_w = Rg * math.cos(resultado_ns_rad_w)
            z_w = Rg * math.sin(resultado_ns_rad_w)
    
            print("Los valores de x en ω= ",x_w)
            print("Los valores de z en ω= ",z_w)
    
            return x_w, z_w     

        def calculo_de_coordendas_xz_0(a, e, ang_0_rad):
            b = a * math.sqrt(1 - e)
            x_0 = a * math.cos(ang_0_rad)
            z_0 = b * math.sin(ang_0_rad)
    
            print("Los valores de x en θ= ", x_0)
            print("Los valores de z en θ= ", z_0)
    
            return x_0, z_0
        
        def elipse_meridiana(a, e,x_0, z_0, x_w, z_w, x_phi, z_phi ):
            semieje_a = a
            semieje_b = a * math.sqrt(1 - e)
 
            theta = np.linspace(-np.pi/2, np.pi/2, 100)  

            x = semieje_a * np.cos(theta)
            y = semieje_b * np.sin(theta)
    
            plt.figure()
            plt.scatter(x_0, z_0, color='blue', label='Punto θ')
            plt.scatter(x_w*1.001, z_w*1.001, color='red', label='Punto ω')
            plt.scatter(x_phi*1.002, z_phi*1.002, color='green', label='Punto φ')
            plt.plot(x, y)
            plt.axhline(0, color='black', linestyle='-', linewidth=1, label = "Ecuador")
            plt.scatter(0, 0, color='black')
            plt.xlabel('Eje x')
            plt.ylabel('Eje z')
            plt.title('Elipse Meridiana')
            plt.gca().set_aspect('equal', adjustable='box')
            plt.grid(True)
            plt.legend()
            plt.show()
            
        resultado_ns_rad_w = nortesur()
        ang_phi_rad = calculo_de_phi_en_w(resultado_ns_rad_w, e)
        ang_0_rad = calculo_de_w_en_theta(resultado_ns_rad_w, e)
        x_phi, z_phi = calculo_de_coodernadas_xz_phi(a, e, ang_phi_rad)
        x_w, z_w = calculo_de_coordendas_xz_w(a, e, resultado_ns_rad_w)
        x_0, z_0 = calculo_de_coordendas_xz_0(a, e, ang_0_rad)
        elipse_meridiana(a, e,x_0, z_0, x_w, z_w, x_phi, z_phi )

    elif Seleccionar_variable == 3:
        def nortesur():
            Seleccionar_norte_sur = int(input("Seleccione (1) si su latitud es norte, o a su vez seleccione (2) si su latitud es sur: "))
            valor_0_grados = float(input("Ingrese el valor de θ en grados: "))
            valor_0_minutos = float(input("Ingrese el valor de θ en minutos: "))
            valor_0_segundos = float(input("Ingrese el valor de θ en segundos: "))
    
            Calculo_de_0_decimal = valor_0_grados + valor_0_minutos/60 + valor_0_segundos/3600
    
            if Seleccionar_norte_sur == 1:
                resultado_ns_0 = Calculo_de_0_decimal * 1
            elif Seleccionar_norte_sur == 2:
                resultado_ns_0 = Calculo_de_0_decimal * -1
            else:
                print("NO VALIDO")
        
            resultado_ns_rad_0 = math.radians (resultado_ns_0)
        
            return (resultado_ns_rad_0)
        
        def calculo_phi_en_0(resultado_ns_rad_0, e):
            calculo_phi_con_0 = math.degrees(math.atan(math.tan(resultado_ns_rad_0)/math.sqrt(1-e)))
            phi_rad = math.radians(calculo_phi_con_0)
            
            grados_0 = abs(int(calculo_phi_con_0))
            grados_0_sin_abs = int(calculo_phi_con_0)
            minutos_dec_0 = (calculo_phi_con_0 - grados_0_sin_abs) * 60
            minutos_0 = abs(int(minutos_dec_0))
            minutos_0_sin_abs = int(minutos_dec_0)
            segundos_0 = abs((minutos_dec_0 - minutos_0_sin_abs) * 60)
            visualizacion_phi = f"{grados_0}° {minutos_0}' {segundos_0:.5f}\""
    
            if calculo_phi_con_0 >= 0:
                print("Su valor de φ:", visualizacion_phi, "N")
            elif calculo_phi_con_0 <= 0:
                print("Su valor de φ:", visualizacion_phi, "S")
            else:
                print("Su valor de φ:", visualizacion_phi, "ECUADOR")
        
            return phi_rad
        
        def calculo_de_w_0(resultado_ns_rad_0, e):
            calculo_de_w_con_0 = math.degrees(math.atan(math.tan(resultado_ns_rad_0)*math.sqrt(1-e)))
            w_rad_0 = math.radians(calculo_de_w_con_0)
            
            grados_0 = abs(int(calculo_de_w_con_0))
            grados_0_sin_abs = int(calculo_de_w_con_0)
            minutos_dec_0 = (calculo_de_w_con_0 - grados_0_sin_abs) * 60
            minutos_0 = abs(int(minutos_dec_0))
            minutos_0_sin_abs = int(minutos_dec_0)
            segundos_0 = abs((minutos_dec_0 - minutos_0_sin_abs) * 60)
            visualizacion_phi = f"{grados_0}° {minutos_0}' {segundos_0:.5f}\""
    
            if calculo_de_w_con_0 >= 0:
                print("Su valor de ω:", visualizacion_phi, "N")
            elif calculo_de_w_con_0 <= 0:
                print("Su valor de ω:", visualizacion_phi, "S")
            else:
                print("Su valor de ω:", visualizacion_phi, "ECUADOR")
        
            return w_rad_0
        
        def calculo_de_coodernadas_xz_phi(a, e, phi_rad):
            
            N = a / math.sqrt(1 - e * (math.sin(phi_rad) ** 2))
            x_phi = N * math.cos(phi_rad)
            z_phi = N * (1 - e) * math.sin(phi_rad)
    
            print("Los valores de x en φ= ", x_phi)
            print("Los valores de z en φ= ", z_phi)
    
    
            return x_phi, z_phi

        def calculo_de_coordendas_xz_w(a, e, w_rad_0):
            
            RgP = a * math.sqrt(1 - e)
            w = math.sqrt(1 - e * (math.cos(w_rad_0) ** 2))
            Rg = RgP / w
            x_w = Rg * math.cos(w_rad_0)
            z_w = Rg * math.sin(w_rad_0)
    
            print("Los valores de x en ω= ",x_w)
            print("Los valores de z en ω= ",z_w)
    
            return x_w, z_w     

        def calculo_de_coordendas_xz_0(a, e, resultado_ns_rad_0):
            b = a * math.sqrt(1 - e)
            x_0 = a * math.cos(resultado_ns_rad_0)
            z_0 = b * math.sin(resultado_ns_rad_0)
    
            print("Los valores de x en θ= ", x_0)
            print("Los valores de z en θ= ", z_0)
    
            return x_0, z_0
        
        def elipse_meridiana(a, e,x_0, z_0, x_w, z_w, x_phi, z_phi ):
            semieje_a = a
            semieje_b = a * math.sqrt(1 - e)
 
            theta = np.linspace(-np.pi/2, np.pi/2, 100)  

            x = semieje_a * np.cos(theta)
            y = semieje_b * np.sin(theta)
    
            plt.figure()
            plt.scatter(x_0, z_0, color='blue', label='Punto θ')
            plt.scatter(x_w*1.001, z_w*1.001, color='red', label='Punto ω')
            plt.scatter(x_phi*1.002, z_phi*1.002, color='green', label='Punto φ')
            plt.plot(x, y)
            plt.axhline(0, color='black', linestyle='-', linewidth=1, label = "Ecuador")
            plt.scatter(0, 0, color='black')
            plt.xlabel('Eje x')
            plt.ylabel('Eje z')
            plt.title('Elipse Meridiana')
            plt.gca().set_aspect('equal', adjustable='box')
            plt.grid(True)
            plt.legend()
            plt.show()
            
        resultado_ns_rad_0 = nortesur()
        phi_rad = calculo_phi_en_0(resultado_ns_rad_0, e)
        w_rad_0 = calculo_de_w_0(resultado_ns_rad_0, e)
        x_phi, z_phi = calculo_de_coodernadas_xz_phi(a, e, phi_rad)
        x_w, z_w = calculo_de_coordendas_xz_w(a, e, w_rad_0)
        x_0, z_0 = calculo_de_coordendas_xz_0(a, e, resultado_ns_rad_0)
        elipse_meridiana(a, e,x_0, z_0, x_w, z_w, x_phi, z_phi )
        
    else:
        print ("No valido, intentelo despues")
a,e = elipsoides()        
seleccionar_tipo_de_transformacion()    


               