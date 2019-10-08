# -*- coding: utf8 -*-
import ScrapingCNE.busquedaCNE as busqueda

def deleteCharectes (fileName):
    _fileName = fileName + '.csv'
    file = open(_fileName)
    dato  = []
    for linea in file: 
        # Eliminamos carecteres especiales
        texto = linea.strip('\n\t')
        dato.append(texto.split(','))

        #nacionalidad = dato[linea][0]
        #cedula = dato[linea][1]
        #print(cedula.text)
        #print ("Nacionalidad: {}".nacionalidad)
    print (dato)
    file.close()


if __name__ == "__main__":
    a = "buscar"
    #deleteCharectes(a)
    busqueda.buscar()

