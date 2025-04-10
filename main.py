def promedio (lista):
  cant_elementos = len(lista)
  suma: float = 0
  while cant_elementos > 0:
    suma = suma + lista[cant_elementos-1]
    cant_elementos -= 1
  return suma / len(lista)

lista_num = [2, 4, 6, 2, 1, 9]
print(f'El premedio de la lista es: {promedio(lista_num)}')