#!/bin/python3

import random

continuar = 'si'

while continuar == 'si':
  chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

  length = input('Introduzca la longitud de la contraseña (entre 10 y 14)')
  length = int(length)

  if length < 4 or length > 16:
    print('La contraseña debe ser mayor a 4 y menor a 16 caracteres')
    continuar = 'si'
  else:
    print('\nContraseña : ')

    password = ''
    for c in range(length):
      password += random.choice(chars)
    print(password)
    continuar = input('¿Desea generar otra contraseña? (si/no)')
