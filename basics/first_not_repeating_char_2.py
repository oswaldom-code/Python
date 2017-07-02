# -*- coding: utf-8 -*-
"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y
"""


def first_not_repeating_char(char_sequence):
    not_repeating_char = "_"
    
    for i in char_sequence:
        counter_char = 0
        for j in char_sequence:
            if i == j:
                counter_char +=1
                print counter_char
        if counter_char == 1:
            not_repeating_char = i
            break
                
    return not_repeating_char

if __name__ == '__main__':
    char_sequence = str (
        raw_input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)

    if result == '_':
        print('Todos los caracteres se repiten.')
    else:
        print('El primer caracter no repetido es: {}'.format(result))