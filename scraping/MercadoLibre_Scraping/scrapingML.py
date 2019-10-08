# -*- coding: utf8 -*-

"""
Autor: @OSWALDOM-CODE
Descripción:
"""
import requests
from bs4 import BeautifulSoup



def app():
    url_semilla = "https://listado.mercadolibre.com.ve/"
    articulo = "laptop"

    urlCompuesta = url_semilla + articulo
   # print (urlCompuesta)
    response = requests.get(urlCompuesta)
    soup = BeautifulSoup(response.content, "html.parser") 
    contador = 0
    #print (response.content)
    #Verificamos el codido devuelto por el servidor 
    if response.status_code == 200:
        lista = []
        for item in soup.find_all('li')[22:-25]:
            
            dato = item.text
            lista.append(dato.strip())
            
            contador = contador +1
        
        print(lista)
        print("bucle de :", contador)
    else:
        print("Error:  ", response.status_code)

    

if __name__ == "__main__":
    app()