import csv
def obtener_fichero_calificaciones():
    lista =[]
    #Abre el archivo en modo lectura
    with open(r"C:\Users\cetecom\Desktop\calificaciones.csv","r",newline="") as archivo:
    #Crea un letor CSV
        lector_csv =csv.reader(archivo, delimiter=";")
        pos = 0
        for linea in lector_csv:
            if pos != 0:
                for i in range(2,len(linea)):
                    if linea[i] == "":
                        linea[i] = "0.0"

                Apellidos = linea[0]
                Nombres = linea[1]
                Asistencia = float(linea[2].replace('%',''))
                Parcial1 =float(linea[3].replace(',','.'))
                Parcial2 = float(linea[4].replace(',','.'))
                Ordinario1 = float(linea[5].replace(',','.'))
                Ordinario2 = float(linea[6].replace(',','.'))
                Praticas = float(linea[7].replace(',','.'))
                OrdinarioPracticas = float(linea[8].replace(',','.'))
                lista.append({
                    'Apellidos' : Apellidos,
                    'nombre':Nombres,
                    'Asistencia' : Asistencia,
                    'Parcial1':Parcial1,
                    'Parcial2':Parcial2,
                    'Ordinario1':Ordinario1,
                    'Ordinario2':Ordinario2,
                    'Practicas' : Praticas,
                    'OrdinarioPracticas': OrdinarioPracticas,
                })
                print(lista)
            else:
                pos= 1
    return lista

obtener_fichero_calificaciones()