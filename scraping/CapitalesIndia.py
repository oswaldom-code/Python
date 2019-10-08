from urllib.request import  urlopen
from bs4 import BeautifulSoup
import pandas as pd

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"


page = urlopen (wiki)

soup = BeautifulSoup(page, 'html.parser')

#print (soup.find_all('table',class_='wikitable sortable plainrowheaders'))
tabla = soup.find('table', class_='wikitable sortable plainrowheaders')
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]


for row in tabla.findAll('tr'):
    cells = row.findAll('td')
    state = row.findAll('th') # Para resolver que el nombre del estado está dentro de una etiqueta th en vez de una td
    if len(cells)==6: #Only extract table body not heading
        A.append(cells[0].find(text=True))
        B.append(state[0].find(text=True)) #resolviendo anomalia en la columna estado
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))

df=pd.DataFrame(A,columns=['No.'])
df['Estado/UT']=B
df['Capital Administrativa']=C
df['Capital Legislativa']=D
df['Capital Judicial']=E
df['Año de Fundación']=F
df['Antigua Capita']=G


print (df)