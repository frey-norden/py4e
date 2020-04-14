#!/usr/bin/env python3
# greet.py

def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    elif lang == 'ru':
        print('Privet')
    else:
        print('Moi')

greet('es')
greet('ru')
greet('fi')
greet('fr')
