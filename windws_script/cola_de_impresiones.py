# Aquí el script: on_offSpool.py (Así lo llamé al archivo, pueden llamarlo como deseen.)
#!/usr/bin/env python
#-*- encoding:utf-8 -*-

# By: Debianitram -> Miranda Martín.
# @ : debianitram(@)gmail.com

import os

# Directorio spool
SPOOL = os.environ['SYSTEMROOT'] + "\System32\spool"
# Directorio PRINTERS. 
SPOOLPRINTERS = SPOOL + "\PRINTERS"

# Comandos a utilizar.
on_spool  = "net start spooler"
off_spool = "net stop spooler"

# Inicio del programa.
# Borramos la pantalla.
os.system('cls')
# Nombre del Usuario
print ("##################################")
print ("Usuario:" + os.environ['USERNAME'])
# Nombre del PC.
print ("Nombre del equipo: " + os.environ['COMPUTERNAME'])
print ("##################################\n")


# Comienzan los procesos.
print ("Se inician los procesos ..." )
print ("* Cola de impresión -> Stop... ")
os.system(off_spool)

# Se eliminan los ficheros en spool/PRINTERS .
if os.path.exists(SPOOLPRINTERS):
 # Cambiamos de directorio.
 os.chdir(SPOOLPRINTERS)
 # listamos el directorio.
 resultList = os.listdir(os.getcwd())
 if len(resultList) > 0:
    # Eliminamos los archivos.
    for nameFile in resultList:
        print ("Eliminando el archivo: " + nameFile)
        os.remove(nameFile)
    print ("* Archivos eliminados ... ")
 
print ("* Cola de impresión -> Start... ")
os.system(on_spool)

# Fin del script.