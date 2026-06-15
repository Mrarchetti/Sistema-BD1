import re
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

def pedir_hasta_valido(info, validador):
    while True:
        valor = input(info)
        if validador(valor):
            return valor

def pedir_hasta_valido_modif(info, anterior, validador):
    while True:
        valor = input(info)
        if valor == "":
            return anterior
        elif validador(valor):
            return valor
