
from math import log10, sqrt

"""
Serie Fibonacci
La secuencia de Fibonacci es una secuencia de números con la relación:
𝐹𝑛=𝐹𝑛-1𝐹𝑛-2, donde 𝐹1=1 y 𝐹2=1
Resulta que 𝐹541 contiene 113 dígitos y es el primer número de Fibonacci donde los
últimos 9 dígitos son una secuencia pan-digital (que contiene todos los números del 1 al 9,
pero no es necesario que estén en orden). Por otro lado 𝐹2749 contiene 757 dígitos y es el
primer número de Fibonacci donde los primeros 9 dígitos son una secuencia pan-digital. 𝐹𝑘 es
el primer número de Fibonacci donde los primeros 9 dígitos son una secuencia pan-digital y
donde los últimos 9 dígitos también son una secuencia pan-digital.
¿Cuánto es 𝐾?

serie fibonacci es una serie infinita en la que la suma de dos números consecutivos 
siempre da como resultado el siguiente número (1+1=2; 13+21=34).

Los números y las fórmulas pandigitales son aquellas expresiones matemáticas en cuya construcción 
aparecen al menos una vez todos los dígitos que constituyen la base de numeración en la que están escritos. La base 10 es la más usada para construir expresiones 
pandigitales, pues se trata de la base más pequeña que usa todos los guarismos existentes (0, 1, 2, ,3 ,4 ,5, 6, 7, 8, 9) para denotar números.

"""

# en este caso se utiliza una formula racion de oro
M = 1000000000
# segun la formula se le saca la raiz cuadrada a 5
sqrt5 = sqrt(5)
# esto da  solo los primeros 10 digitos
fn = (sqrt5+1)/2
# siguiendo la formula halla el logaritmo de fn
phi = log10(fn)
# y luego se procede a hallar el logaritmo a raiz cuadrada de 5
logsqrt5 = log10(sqrt5)

def test(n):
    """fucion que valida si n es un numero pan digital mientras no contenga todos los numeros"""
    if n < 100000000: return False
    flags = [0]*10
    flags[0] = 1
    while n > 0:
        n, m = n//10, n%10
        if flags[m]: return False
        flags[m] = 1
    return True

def run():
    a, b, k = 1, 1, 2
    while True:
        """ while que buscar la serie fibonacci entre todos los numeros de la serie hasta llegar a  𝐹2749  """
        a, b, k = b, a+b, k+1
        a, b, k = b % M, (a+b)%M, k+1
        # se comprueba si el numero cumple con las condiciones de pan digital
        if test(b):
            # se k se multiplica por el log de fn y se le resta el logaritmo de la raiz cuadrada de 5
            phik = phi*k-logsqrt5
            # se halla n donde 10 elevenado a la potencia de la variable donde se almaceno el resultado de la multiplicacion anterior 
            # menos el logaritmo de fn por el valor de k mas 9 y luego se usa // para hacer una divicion entre 10 el resultado sera un numero entero
            n = int(10**(phik-int(phi*k)+9))//10
            # se usa de forma recursiva esta funcion para determinar si el valor de n cumple las condiciones para ser pandigital
            if test(n): break

    print("el valor de k es", k)

run()

