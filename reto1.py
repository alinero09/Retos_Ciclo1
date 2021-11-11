area_de_la_zona = float(input(" "))
numero_antenas_antiguas = int(input(" "))
tipo_de_antena_nueva = str(input(" "))
numero_de_antenas_a_instalar = 0
resta_area = 0
if area_de_la_zona <= 0 or numero_antenas_antiguas < 0 or tipo_de_antena_nueva != "a" and tipo_de_antena_nueva != "b" and tipo_de_antena_nueva != "c" and tipo_de_antena_nueva != "d" and tipo_de_antena_nueva != "e" and tipo_de_antena_nueva != "A" and tipo_de_antena_nueva != "B" and tipo_de_antena_nueva != "C" and tipo_de_antena_nueva != "D" and tipo_de_antena_nueva != "E":
    print("error en los datos")
elif area_de_la_zona > 0 and numero_antenas_antiguas >= 0 and tipo_de_antena_nueva == "a" or tipo_de_antena_nueva == "b" or tipo_de_antena_nueva == "c" or tipo_de_antena_nueva == "d" or tipo_de_antena_nueva == "e" or tipo_de_antena_nueva != "A" or tipo_de_antena_nueva != "B" or tipo_de_antena_nueva != "C" or tipo_de_antena_nueva != "D" or tipo_de_antena_nueva != "E":
    resta_area = area_de_la_zona - (36900 * numero_antenas_antiguas)
    if resta_area <= 0:
            print(numero_de_antenas_a_instalar)
    elif resta_area > 0 and tipo_de_antena_nueva == "a" or tipo_de_antena_nueva == "A":
        numero_de_antenas_a_instalar = (resta_area / 44600)
        print(round(numero_de_antenas_a_instalar))
    elif resta_area > 0 and tipo_de_antena_nueva == "b" or tipo_de_antena_nueva == "B":
        numero_de_antenas_a_instalar = (resta_area / 51800)
        print(round(numero_de_antenas_a_instalar))
    elif resta_area > 0 and tipo_de_antena_nueva == "c" or tipo_de_antena_nueva == "C":
        numero_de_antenas_a_instalar = (resta_area / 9600)
        print(round(numero_de_antenas_a_instalar))
    elif resta_area > 0 and tipo_de_antena_nueva == "d" or tipo_de_antena_nueva == "D":
        numero_de_antenas_a_instalar = (resta_area / 15300)
        print(round(numero_de_antenas_a_instalar))
    elif resta_area > 0 and tipo_de_antena_nueva == "e" or tipo_de_antena_nueva == "E":
        numero_de_antenas_a_instalar = (resta_area / 13900)
        print(round(numero_de_antenas_a_instalar))
