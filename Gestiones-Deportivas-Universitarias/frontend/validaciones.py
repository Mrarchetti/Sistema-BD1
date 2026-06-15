import re
from datetime import datetime
# Las funciones de validacion siempre devuelve True o False

def validar_no_vacio(valor):
	if valor.strip() == "":
		print("El valor no puede estar vacío.")
		return False

	return True


def validar_entero_positivo(valor):
    if not validar_no_vacio(valor):
        return False

    if not valor.isdigit():
        print("El valor debe ser un entero positivo.")
        return False

    if int(valor) <= 0:
        print("El valor debe ser un entero positivo.")
        return False

    return True


def validar_documento_uruguayo(documento):
    if not validar_no_vacio(documento):
        return False

    documento = str(documento).strip()
    if not re.fullmatch(r"\d{8}", documento):
        print("El documento debe ser una cédula uruguaya de 8 números.")
        return False

    return True


def validar_fecha(valor):
    if not validar_no_vacio(valor):
        return False

    try:
        datetime.strptime(valor.strip(), "%Y-%m-%d")
        return True
    except ValueError:
        print("La fecha debe tener el formato AAAA-MM-DD.")
        return False

def pedir_hasta_valido(info, validador):
    while True:
        valor = input(info)
        if validador(valor):
            return valor


def pedir_fecha(info):
    while True:
        valor = input(info)
        if validar_fecha(valor):
            return datetime.strptime(valor.strip(), "%Y-%m-%d").date()

def pedir_hasta_valido_modif(info, anterior, validador):
    while True:
        valor = input(info)
        if valor == "":
            return anterior
        elif validador(valor):
            return valor

def validar_estado(valor):
    if valor in ["CONFIRMADA", "ESPERA"]:
        return True
    return False

def validar_horario(valor):
    if not validar_no_vacio(valor):
        return False

    try:
        datetime.strptime(valor.strip(), "%H:%M:%S")
        return True
    except ValueError:
        print("El horario debe tener el formato HH:MM:SS")
        return False
    
def validar_confirmacion(valor):
    if valor in ["S", "N"]:
        return True
    print("La asistencia debe ser S o N")
    return False