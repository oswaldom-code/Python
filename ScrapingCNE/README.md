# ScrapingCNE
======================

_  El [Consejo Nacional Electoral (CNE)](http://www.cne.gob.ve) en Venezuela es la institución dedicada de regir el tema electoral en el país, en su web  se puede consultar dónde le corresponde ejercer el derecho del voto a una persona conociendo su número de identidad conocido también como número de cédula.

_  Como respuesta la web nos devuelve nombre completo de la persona y los datos de ubicación del centro de votación (Estado, Municipio, Parroquia y dirección)  en el cual le corresponde ejercer el derecho al sufragio dicha persona.

_  Cuando queremos realizar un par de consulta se puede realizar de forma manual directamente en la web de la institución, sin embargo cuando se trata de gran cantidad de datos debemos recurrir a las técnicas de Scripting a fin de hacernos de la información necesaria.

_  El objeto de este código es solo con fines didácticos. 

## busquedaCNE.py
======================
_  Aun cuando creo que el código está suficientemente documentado, vamos a dar un poco más de detalle.
Lo primero es importar las librerías que nos permitirán manipular el contenido HTML, para ello en la línea 3 importamos requests, a través de esta librerías podemos realizar solicitudes a los servidores simulando la petición que realiza un usuario a través de un navegador web. En la línea 4 utilizamos Beautifulsoup de bs4, que a diferencia que requests no viene por defecto en nuestra instalación de Python, para hacer uso de ella es necesario instalarla primero con "pip install bs4" desde la terminal.

```
1. # requiere python3
2.
3. import requests
4. from bs4 import BeautifulSoup
```

**Nota:** *Coloco numeración a cada línea solo como referencia para ser más explícito en la documentación pero no tiene correlación al número de línea del código fuente real.*

**url_semilla** es una variable que almacena la url base, aún sin los parámetros necesarios para la consulta

```
# Url destino
url_semilla = "http://www.cne.gob.ve/web/registro_electoral/ce.php?"

```
_  Los valores como mencionamos anteriormente son la nacionalidad, que deberá ser un carácter en mayúscula **V** para ciudadano venezolano o **E** para ciudadanos extranjeros. Y **cedula** que es el número de identidad, por ahora creo que rondan por los 30millones, es decir, la cedula es un numero entero de máximo ocho (8) dígitos.

# Parámetros a incluir en la url 
======================

```
nacionalidad = 'V'
cedula = '14147067'

```

_  Ya conociendo la **url_semilla** y los datos a consultar, construimos lo que yo denominé la **url_compuesta**, que es la url_semilla concatenada con los valores necesarios para realizar la consulta.

```
# Url final
url_compuesta = url_semilla + 'nacionalidad=' + nacionalidad + '&' + 'cedula=' + cedula
```

_  Se realiza la solicitud para obtenemos la respuesta almacenada en la variable **requests** del tipo requests.

```
# Petición
requests = requests.get(url_compuesta)
```

_  Seguidamente, tomamos lo que nos devuelve el servidor y que tenemos almacenado en requests y lo parseamos como html para asignarlo a soup que será la que contendrá toda la estructura HTML.

```
# Tomamos el requests, lo parseamos a html para obtener un tipo de dato soup
soup = BeautifulSoup(requests.content, "html.parser")

```

_  Toda petición realizada a un servidor devuelve un código del estatus resultante de dicha  solicitud, por ejemplo un código 500, bien  sabido por dodos hace referencia a una web no encontrada posiblemente movida a otra url o simplemente borrada y así otros tantos códigos. Pero a nosotros nos interesa validar que el estatus de solicitud de  nuestra solicitud sea 200. Ya que es el que nos indica que nuestra solicitud ha sido atendida correctamente, y en consecuencia tendremos en nuestra variable **requests** en contenido necesario para raspar con nuestro código.

```
1. # status_code 200 es OK, en caso contrario web no disponible he imprimimos mensaje y código de error
2. if requests.status_code == 200:      
3.      contenList = []
4.
5.      for contenido  in soup.find_all('td')[10: 24]:# 10:24 los <td> del árbol que nos interesa
6.          dato = contenido.text
7.          contenList.append(dato.strip())
8.
9.      datosPersona = '\nCedula:' + contenList[1] + '\n' + 'Nombre y Apellido: ' + contenList[3]
10.
11.     datosCentro  =  '\nEsdato:' + contenList[5] + '\n' + 'Municipio: ' + contenList[7]
12. 
13.     print(datosPersona + datosCentro)
14.  
15. else:
16.     print("Error de conexión: Codigo ", requests.status_code)

```

_  Es por eso que en la línea 2 iniciamos un condicional **if – else** que nos permita tomar nos caminos de acción, uno en el **if** cuando el código sea igual a 200 (solicitud exitosa) y un segundo camino de acción cuando el código sea distinto a 200, en este caso no fue posible acceder a la información y en consecuencia lanzamos un mensaje de error seguido del número del mismo.


_  **Una vez dicho todo lo anterior solo nos queda centrarnos en la verdadera lógica y el corazón de este ejercicio, que es cómo vamos a raspar la información de la web.**


_  En la línea 3 declaro una lista vacía, en ella voy a almacenar los datos raspados.

_  En la línea 5 inicio un bucle **for** para recorrer la estructura HTML. Haciendo uso de la función **find_all** buscamos todas las etiquetas de tipo **<td>**, ya que previamente inspeccionamos la web y sabemos que los datos que nos interesan están dentro de unas etiquetas **<td>**.

_  Pero resulta que en el HTML hay varias etiquetas **<td>** de diferentes niveles, y revisando con detalle evidenciamos que las que nos interesan están entre el nivel 10 y el 24. El resto de los niveles también contienen los datos pero con mucha “basura” o texto que no es de nuestro interés.

_  Al recorrer las etiquetas <td> que se encuentra entre los niveles  10 al 24 tomará el contenido de dicha etiquetas y los almacenará en la variable **contenido**, posteriormente en la  línea 6 extraemos de la variable **contenido** el texto  y se lo asignamos a la variable **dato**.

_  En la línea 7 retiramos los espacios en blanco con el método strip() y lo agregamos a la lista que irá almacenando los datos de nuestro interés.

======================


