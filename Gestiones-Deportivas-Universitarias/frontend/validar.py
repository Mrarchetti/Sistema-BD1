import re
from datetime import datetime
from funciones.validaciones import validar_fecha



def pedir_hasta_valido(info, validador):
    while True:
        valor = input(info)
        valido, error = validador(valor)
        if valido:
            return valor
        else:
            print(error)

def pedir_fecha(info):
    while True:
        valor = input(info)
        valido, error = validar_fecha(valor)
        if valido:
            return datetime.strptime(valor.strip(), "%Y-%m-%d").date()
        else:
            print(error)

def pedir_hasta_valido_modif(info, anterior, validador):
    while True:
        valor = input(info)
        if valor == "":
            return anterior
        else:
            valido, error = validador(valor)
            if valido:
                return valor
            else:
                print(error)