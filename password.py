"""Contraseñas
Un método de seguridad comúnmente utilizado por los bancos es preguntar tres
caracteres aleatorios de una contraseña. Por ejemplo, si la contraseña es 531278, el banco
puede preguntar por el 2do, 3er, y 5to, carácter; esperando que el usuario responda con la
secuencia 3-1-7. El archivo keylog.txt contiene 50 secuencias correctas para una contraseña
específica. Dado que cada una de las secuencias está en orden de primer carácter a último
carácter, ¿cuál es la contraseña más corta para la cual todas las secuencias son correctas?
"""

import pandas as pd
import numpy as np
# data = pd.read_csv('keylog.txt', index_col=False,header=None)

data = np.loadtxt('keylog.txt', dtype=int)


data_split = []

elements_no_repeat = []
def splitNumber(number):
    return [int(i) for i in str(number)]


def get_distinct():
    for key in data:
        value = splitNumber(key)
        for i in value:
            data_split.append(i)
    return set(data_split)

def get_near(value):
    temp = []
    for i in range(len(data_split)):
        if data_split[i] == value:
            print("aqui hay un numero")
            print(data_split[i])
            count = 0
            for j in range(i+1, len(data_split)):
                temp.append(data_split[j])
                if count == 1:
                    break
                count+=1
    return temp



def get_pass(elements, data_split):
    array_temp = []
    for i in elements:
        data = get_near(i)
        if i in array_temp:
            for j in data:
                if 
        else:
            for j in range(len(array_temp)):
                if array_temp[j] in data:
                    array_temp.append(,i
                
    

def run():
    elements_no_repeat = get_distinct()
    get_pass(elements_no_repeat, data_split)
    # print(elements_no_repeat)



run()
# insertToDataframe()
# print(data)
# fileName = "keylog.txt"
# fileObj = open(fileName, "r")
# array = fileObj.read().splitlines()
# print(array)


# secuencias = [[3,1,9],[1,6,2],[2,8,9]]