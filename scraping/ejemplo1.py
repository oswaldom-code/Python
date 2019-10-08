from bs4 import BeautifulSoup
import requests

url = ("http://www.cne.gob.ve/web/registro_electoral/ce.php?nacionalidad=V&cedula=14147067")

requests = requests.get(url)
#print (requests)

soup = BeautifulSoup(requests.content, "html.parser")

#print (soup)

if requests.status_code == 200:
    #print(requests.content)
    file = open('infoCNE.html', 'wb')
    file.write(requests.content)
    file.close()
    for contenido  in soup.find_all('td')[4:7]:
        print(contenido.text)
    #tr = soup.find_all('table')
    #tds = tr.find_all('b')
    #print (tds)
    #print ("Nome: %s, Cognome: %s, Email: %s",tds[0].text, tds[1].text, tds[2].text)
else:
    print("Error de conexión: Codigo ", requests.status_code)


"""
    for tr in soup.find_all('tr')[2:]:
    tds = tr.find_all('td')
    print "Nome: %s, Cognome: %s, Email: %s" % 
          (tds[0].text, tds[1].text, tds[2].text) 
"""



#soup = BeautifulSoup()






























"""
url = ("http://www.cne.gob.ve/web/registro_electoral/ce.php?nacionalidad=V&cedula=20540124")

r = requests.get(url)



soup = BeautifulSoup(r.content, "html.parser")
cadena = soup.get_text( strip=True)
print (cadena[57:117])

"""
"""
file = open('infoCNE.csv', 'wb')
file.write(soup.get_text(";", strip=True))
file.close()
"""