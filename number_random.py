#########################################
## Name: number_random.py
## By @oswaldom876
########################################

# -*- coding: utf-8 -*-
import random
import os

def run():
    number_found = False
    os.system('cls') #Clear the console
    print('=====================================')
    print('..:: EN BUSCA DEL NÚMERO SECRETO ::..')
    print('=====================================')
    aleatorio = calc_random()
   
    while not number_found:
        number = int(input('\aAdivida el numero secreto: '))

        if number == aleatorio:
            os.system('cls') #Clear the console
            print('=================================')
            print('****         E X I T O       **** ')
            print('****  Encontraste el Número! ****')
            print('=================================')
            
            number_found = True
            pass
        elif number > aleatorio:
            print('\aMejor intenta con un número más bajo...')
               
        else:
            print('\aMejor intenta con un número más alto..')       
  


#funtion of  aleatorio number claculation
def calc_random ():
    
    print('>>> Primero definamos el rango <<<')
    numberInit = int(input('>Desde el número: '))
    numberEnd = int(input('>Hasta el número: '))
    os.system('cls') #Clear the console
    print('======================')
    print(' ****   A JUGAR   **** ')
    print('======================')
    aleatorio = random.randint(numberInit,numberEnd)
    return aleatorio
 
if __name__ == '__main__':
    run()


   