import math #
numero_de_zonas = int(input("Introduzca el numero de zonas: "))

contador_de_zonas = 0
resta_area = 0
total_de_antenas_de_zonas = 0
numero_de_antenas_a_instalar = 0
cont_a = 0
cont_b = 0
cont_c = 0
cont_d = 0
cont_e = 0

if numero_de_zonas <= 0:
    numero_de_zonas = 0
while contador_de_zonas < numero_de_zonas:
    contador_de_zonas += 1
    area_de_la_zona = float(input("Introduzca el area de la zona: "))
    numero_antenas_antiguas = int(input("Introduzca el numero de antenas antiguas: "))
    tipo_de_antena_nueva = input("Introduzca el tipo de antena nueva a instalar: ")
    if area_de_la_zona <= 0 or numero_antenas_antiguas < 0 or tipo_de_antena_nueva != "a" and tipo_de_antena_nueva != "b" and tipo_de_antena_nueva != "c" and tipo_de_antena_nueva != "d" and tipo_de_antena_nueva != "e":
        area_de_la_zona = 0
        numero_antenas_antiguas = 0
        numero_de_antenas_a_instalar = 0
    elif area_de_la_zona > 0 and numero_antenas_antiguas >= 0 and tipo_de_antena_nueva == "a" or tipo_de_antena_nueva == "b" or tipo_de_antena_nueva == "c" or tipo_de_antena_nueva == "d" or tipo_de_antena_nueva == "e":
        resta_area = area_de_la_zona - (36900 * numero_antenas_antiguas)
        if resta_area <= 0:
            numero_de_antenas_a_instalar = 0
        if resta_area > 0 and tipo_de_antena_nueva == "a":
            numero_de_antenas_a_instalar = (resta_area / 44600)
            numero_de_antenas_a_instalar = math.ceil(numero_de_antenas_a_instalar)
            cont_a = cont_a + numero_de_antenas_a_instalar
        elif resta_area > 0 and tipo_de_antena_nueva == "b":
            numero_de_antenas_a_instalar = (resta_area / 51800)
            numero_de_antenas_a_instalar = math.ceil(numero_de_antenas_a_instalar)
            cont_b = cont_b + numero_de_antenas_a_instalar
        elif resta_area > 0 and tipo_de_antena_nueva == "c":
            numero_de_antenas_a_instalar = (resta_area / 9600)
            numero_de_antenas_a_instalar = math.ceil(numero_de_antenas_a_instalar)
            cont_c = cont_c + numero_de_antenas_a_instalar
        elif resta_area > 0 and tipo_de_antena_nueva == "d":
            numero_de_antenas_a_instalar = (resta_area / 15300)
            numero_de_antenas_a_instalar = math.ceil(numero_de_antenas_a_instalar)
            cont_d = cont_d + numero_de_antenas_a_instalar
        elif resta_area > 0 and tipo_de_antena_nueva == "e":
            numero_de_antenas_a_instalar = (resta_area / 13900)
            numero_de_antenas_a_instalar = math.ceil(numero_de_antenas_a_instalar)
            cont_e = cont_e + numero_de_antenas_a_instalar

total_de_antenas_de_zonas = cont_a + cont_b + cont_c + cont_d + cont_e

if total_de_antenas_de_zonas == 0:
    porcentaje_cont_a = 0
else:
    porcentaje_cont_a = (cont_a / total_de_antenas_de_zonas) * 100    

if total_de_antenas_de_zonas == 0:
    porcentaje_cont_b = 0
else:
    porcentaje_cont_b = (cont_b / total_de_antenas_de_zonas) * 100


if total_de_antenas_de_zonas == 0:
    porcentaje_cont_c = 0
else:
    porcentaje_cont_c = (cont_c / total_de_antenas_de_zonas) * 100


if total_de_antenas_de_zonas == 0:
    porcentaje_cont_d = 0
else:
    porcentaje_cont_d = (cont_d / total_de_antenas_de_zonas) * 100


if total_de_antenas_de_zonas == 0:
    porcentaje_cont_e = 0
else:
    porcentaje_cont_e = (cont_e / total_de_antenas_de_zonas) * 100

print(total_de_antenas_de_zonas)
print("a ", "{0:.2f}%".format(porcentaje_cont_a))
print("b ", "{0:.2f}%".format(porcentaje_cont_b))
print("c ", "{0:.2f}%".format(porcentaje_cont_c))
print("d ", "{0:.2f}%".format(porcentaje_cont_d))
print("e ", "{0:.2f}%".format(porcentaje_cont_e))





     





            

     

    

    
    
        
