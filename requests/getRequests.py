"""
Autor: @OSWALDOM-CODE
DESCRIPCIÓN: Código que hace escraping a la web del Consejo Nacional Electoral de Venezuela
para capturar datos básicos de los ciudadanos registrados dado su número de identidad 
(nombre completo, Centro electoral, Estado, Municipio).
"""

# requiere python3

import requests
from bs4 import BeautifulSoup

url = "http://www.cne.gob.ve/web/registro_electoral/ce.php?nacionalidad=V&cedula=18043038"

requests = requests.get(url)
soup = BeautifulSoup(requests.content, "html.parser")

if requests.status_code == 200:      
    file = open('infoCNE.html', 'wb')
    file.write(requests.content)
    file.close()

    contenList = []
    for contenido  in soup.find_all('td')[10: 24]:# 10:24 los <td> del arbol que nos intereza
        palabra = contenido.text

        contenList.append(palabra.strip())
    
    print(contenList)


else:
    print("Error de conexión: Codigo ", requests.status_code)



