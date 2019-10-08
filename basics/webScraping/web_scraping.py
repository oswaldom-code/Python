
# pip install requests, bs4, urllib3


import requests
from bs4 import BeautifulSoup
import urllib3



def run():
       ## http = urllib3.PoolManager() # creamos un objeto pool manager para manejar las conexiones
        print("Hello!!")

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
