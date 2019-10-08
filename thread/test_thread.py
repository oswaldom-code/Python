import threading
import  time

def worker():
    """funcion que realiza el trabajo en el thread"""
    print ('Estoy trabajando para Genbeta Dev')
    return

threads = list()

while True: #Thhread infinito
    
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()