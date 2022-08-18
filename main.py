diccionario = {"codigo": ["001", "002", "003", "004", "005"],
               "nombre": ["Diego", "Mario", "Thiago", "Mauro", "Stiven"],
               "cursos": ["Algoritmos", "Soporte tec", "Laboratorio"]}

listaproductos = []
promedio = 0
resp = "s"
while resp == "s":
    codigoIn = input("Inserte el codigo del estudiante: ")
    cursoTemp = input("Inserte el nombre del curso: ")
    nota = int(input("Inserte la primera nota: "))
    nota1 = int(input("Inserte la segunda nota: "))
    nota2 = int(input("Inserte la tercera nota: "))
    x = 0
    for i in diccionario["codigo"]:
        if i == codigoIn:
            codigoTemp = i
            nombreTemp = diccionario["nombre"][x]
            promTemp = nota + nota1 + nota2
            promedio = promTemp / 3
            registro = [str(codigoTemp), '\t''\t', nombreTemp, '\t''\t', cursoTemp, '\t''\t',
                        str(nota), '\t', str(nota1), '\t', str(nota2), '\t''\t', str(promedio)]
            print()
            print("--------------------------------")
            listaproductos.append(registro)
            cadenavalores = "".join(registro)
            f = open("exadealgoritmos.txt", "a")
            f.write("\n" + cadenavalores)
            f.close()
        x += 1
    resp = input("¿Desea seguir ingresando datos?: ")
    print("------------------------------------")
    f = open("exadealgoritmos.txt")
    print(f.read())
    f.close()
print()
print("------------------------------------------------------------------------------")
print("Codigo", '\t''\t', "Nombre", '\t', "Curso", '\t''\t''\t', "Notas", '\t''\t''\t''\t''\t''\t', "Promedio")
for x in listaproductos:
    print(*x, end="\n")
print("El promedio es: ", promedio)
print("-------------------------------------------------------------------------")