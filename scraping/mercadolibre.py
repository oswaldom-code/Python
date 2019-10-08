"""
Autor: @oswaldom-code
Descripción: Un raspa la web de Mercado libre para optener informacion de los productos
resultantes de una busqueda.
"""

from bs4 import BeautifulSoup
import requests


urlBase = ("https://listado.mercadolibre.com.ve/laptop")

requests = requests.get(urlBase)
soup = BeautifulSoup(requests.content, "html.parser")

if requests.status_code == 200:
    for contenido  in soup.find_all('ol'):
        print(contenido.text)
    file = open('mercadolibre.html', 'wb')
    file.write(contenido.text)
    file.close()
        
else:
    print("Error de conexión: Codigo ", requests.status_code)