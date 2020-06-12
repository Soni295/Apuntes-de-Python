
"""
# importo el modulo no hace falta poner ext
import Ejercicio035

# si solo importo el modulo tendre
# que usar la nomesclatura del punto
# si hice algo el en modulo
# esto aparecera en el archivo

Ejercicio035.sumar(4,5)
Ejercicio035.restar(8,2)

"""
# con esto no necesito usar el punto
# pero me seguira ejecutando lo que hice 
# en el modulo

# si sumar lo sustituyo por un *
# esto me importara todas las funciones
from Ejercicio035 import *

sumar(5,2)

restar(5,2)

multiplicar(6,2)