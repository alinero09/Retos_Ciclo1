import math

cont_a = 0
cont_b = 0
cont_c = 0
cont_d = 0
cont_e = 0
antena_tipo_a = "a"
antena_tipo_b = "b"
antena_tipo_c = "c"
antena_tipo_d = "d"
antena_tipo_e = "e"

n = 0
m = -1
lista_de_departamentos = []
lista_de_antenas_a = []
numero_antenas_antiguas = -1

while n < 1:
        
    datos1 = input().split(" ")
    n = int(datos1[0])
    m = int(datos1[1])

for i in range(n):
        lista_de_departamentos.append(0)
        lista_de_antenas_a.append(0)

for i in range(m):
        total_antenas_a = 0
        total_antenas_b = 0
        total_antenas_c = 0
        total_antenas_d = 0
        total_antenas_e = 0
        while numero_antenas_antiguas < 0:
            datos2 = input().split(" ")
            indice_departamento = int(datos2[0])
            area_de_la_zona = float(datos2[1])
            numero_antenas_antiguas = int(datos2[2])
            tipo_de_antena_nueva = datos2[3]
            if indice_departamento > n:
                indice_departamento = False

            if tipo_de_antena_nueva == "a" and numero_antenas_antiguas >= 0:
                area_cubierta_inicial = (numero_antenas_antiguas * 36900)
                resta_area = (area_de_la_zona - area_cubierta_inicial)
                if resta_area > 0:
                    total_antenas_a = math.ceil(resta_area/ 44600)
                else:
                    total_antenas_a = 0
                lista_de_antenas_a[indice_departamento- 1] = total_antenas_a + lista_de_antenas_a[indice_departamento - 1]
            elif tipo_de_antena_nueva == "b" and numero_antenas_antiguas >=0:
                area_cubierta_inicial = (numero_antenas_antiguas * 36900)
                resta_area = (area_de_la_zona - area_cubierta_inicial)
                if resta_area > 0:
                    total_antenas_b = math.ceil(resta_area / 51800)
                else:
                    total_antenas_b = 0
            elif tipo_de_antena_nueva == "c" and numero_antenas_antiguas >=0:
                area_cubierta_inicial = (numero_antenas_antiguas * 36900)
                resta_area = (area_de_la_zona - area_cubierta_inicial)
                if resta_area > 0:
                    total_antenas_c = math.ceil(resta_area / 9600)
                else:
                    total_antenas_c = 0
            elif tipo_de_antena_nueva == "d" and numero_antenas_antiguas >=0:
                area_cubierta_inicial = (numero_antenas_antiguas * 36900)
                resta_area = (area_de_la_zona - area_cubierta_inicial)
                if resta_area > 0:
                    total_antenas_d = math.ceil(resta_area / 15300)
                else:
                    total_antenas_d = 0
            elif tipo_de_antena_nueva == "e" and numero_antenas_antiguas >=0:
                area_cubierta_inicial = (numero_antenas_antiguas * 36900)
                resta_area = (area_de_la_zona - area_cubierta_inicial)
                if resta_area > 0:
                    total_antenas_e = math.ceil(resta_area / 13900)
                else:
                    total_antenas_e = 0
            
            else:
                tipo_de_antena_nueva = False 
        if tipo_de_antena_nueva != False and indice_departamento != False:
            total_cantidad_de_antenas = total_antenas_a + total_antenas_b + total_antenas_c + total_antenas_d + total_antenas_e
        else:
            total_cantidad_de_antenas = 0

        numero_antenas_antiguas = -1

        lista_de_departamentos[indice_departamento - 1] = total_cantidad_de_antenas + lista_de_departamentos[indice_departamento - 1]

mayoria_de_antenas = max(lista_de_departamentos)
minoria_de_antenas = min(lista_de_departamentos)
indice_menor = lista_de_departamentos.index(minoria_de_antenas) 
indice_mayor = lista_de_departamentos.index(mayoria_de_antenas)
print(indice_menor + 1, minoria_de_antenas)
print(indice_mayor + 1, mayoria_de_antenas)

for i in range(n):
    if lista_de_departamentos[i]!= 0:
        print(i + 1, "%.2f" % float(lista_de_antenas_a[i]/ lista_de_departamentos[i] * 100) + "%")
    else:
        print(i + 1, "%.2f" % 0 + "%")           