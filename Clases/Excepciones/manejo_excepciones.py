resultado = None
try:
    a = int(input('Ingrese un numero: '))
    b = int(input('Ingrese un numero: '))
    resultado = a/b
    print(f'Bloque Try: {resultado}')

except ZeroDivisionError as EZ:
    print('Error de division para 0')

except ValueError as EZ:
    print('Error en el dato escrito')

except TypeError as EZ:
    print('Error tipo de dato')

except Exception as e:
    print('Error en ejecucion')
    print(f'{e}')
    print(f'Bloque Except: {resultado}')
    print(type(e))
else:
    print('Si se ejecuta correctamente el bloque try')
    print(f'Bloque Elese: {resultado}')
finally:
    print('Bloque que siempre se ejecuta')
    print(f'Bloque Finally: {resultado}')

