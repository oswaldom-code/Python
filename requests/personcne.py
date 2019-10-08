"""
Autor: @OSWALDOM-CODE
DESCRIPCIÓN: Código que hace escraping a la web del Consejo Nacional Electoral de Venezuela
para capturar datos básicos de los ciudadanos registrados dado su número de identidad 
(nombre completo, Centro electoral, Estado, Municipio).
"""

# requiere python3

import requests
from bs4 import BeautifulSoup

class Person:
    def __init__(self):
        id = ''
        fullName = ''
        state = ''
        municipality = ''
        parish = ''

    def print_id(self):
        print (self.id)

    def print_fullName(self):
        print (self.fullName)

    def print_state(self):
        print (self.state)

    def print_municipality(self):
        print (self.municipality)

    def print_parish(self):
        print (self.parish)

    def print_info(self):
        info_string = '\
            \n>>>>>>> DATOS <<<<<<<<<'  + \
            '\nCedula: '                + str(self.id) + \
            '\nNombres y Apellidos: '   + str(self.fullName) + \
            '\nEstado: '                + str(self.state) + \
            '\nMunicipio: '             + str(self.municipality) + \
            '\nParroquia: '             + str(self.parish)
        print(info_string)

    def get_info(self):
        id = self.id
        fullName = self.fullName
        state = self.state
        municipality = self.municipality
        parish = self.parish
        return (self )






def consulta(numID='14147067'):
    url = "http://www.cne.gob.ve/web/registro_electoral/ce.php?nacionalidad=V&cedula=" + numID
    person = Person()
    person.id = numID
    
    global requests
    requests = requests.get(url)
    soup = BeautifulSoup(requests.content, "html.parser")

    if requests.status_code == 200:      
        """contenList = []
        for contenido  in soup.find_all('td')[10: 20]:# 10:20 los <td> del arbol que me interezan
            palabra = contenido.text
            contenList.append(palabra.strip())
        print(contenList)
        """

        if ("Objeción: FALLECIDO (3)" != soup.find_all('td')[21].text):
            print('Fallecido')
            print(len("Objeción: FALLECIDO (3)"))
            print (len(soup.find_all('td')[21].text))
            
        else:
                
            person.fullName = soup.find_all('td')[13].text
            person.state = soup.find_all('td')[15].text
            person.municipality = soup.find_all('td')[17].text
            person.parish = soup.find_all('td')[19].text

            print (person.print_info())
            print (soup.find_all('td')[19].text)
        

    else:
        print("Error de conexión: Codigo ", requests.status_code)
 


consulta('1')
    

