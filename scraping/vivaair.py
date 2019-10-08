from bs4 import BeautifulSoup
import requests

## https://www.vivaair.com/co/es/vuelo?DepartureCity=BOG&ArrivalCity=LIM&DepartureDate=2019-08-07&ReturnDate=2019-08-28&Adults=1&Currency=COP

urlSemilla = ("https://www.vivaair.com/co/es/vuelo?DepartureCity=BOG&ArrivalCity=LIM&DepartureDate=2019-08-07&ReturnDate=2019-08-28&Adults=1&Currency=COP")


response = requests.get(urlSemilla)

soup = BeautifulSoup(response.content , 'html.parser')

#print (soup.text)

if response.status_code == 200:
    print(response.content)
    file = open('vivaair.html', 'wb')
    file.write(response.content)
    file.close()
    print (response.content)
   
        
else:
    print("Error de conexión: Codigo ", requests.status_code)


