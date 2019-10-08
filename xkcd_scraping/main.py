import requests
from bs4 import BeautifulSoup
import urllib3
import os



def run():

    http = urllib3.PoolManager()

    #for item in range(1,20):
    response = http.request('GET', 'https://xkcd.com/555')
   
    soup = BeautifulSoup(response.data, 'html.parser')
    imagen_container = soup.find('div', id={'comic'})
    imagen_url = imagen_container.find('img')['src']
    imagen_titulo = imagen_container.find('img')['title']
    print(imagen_titulo)
   # print("\nTitulo: " + imagen_titulo)
    #print("\nUrl: " + imagen_url)

      



    """
    for i in range(1, 20):
        response = requests.get('https://xkcd.com/{}'.format(i))
        soup = BeautifulSoup(response.content, 'html.parser')
        image_container = soup.find(id='comic')

        image_url = image_container.find('img')['src']
        image_name = image_url.split('/')[-1]
        print('Descargando la imagen {}'.format(image_name))
        urllib.urlretrieve('https:{}'.format(image_url), image_name)
    """

if __name__ == '__main__':
    run()
