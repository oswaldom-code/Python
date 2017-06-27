# -*- coding: utf-8 -*-

def run():
    word = str(input('Escribe una palabra: '))
    if(word == word[::-1]):
        print('La palabra es un palindromo')
    else:
        print('La palabra NO es un palindromo')
    

if __name__ == '__main__':
    run()