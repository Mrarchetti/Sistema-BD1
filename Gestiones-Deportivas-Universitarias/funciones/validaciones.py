import re
from datetime import datetime


# Las funciones de validacion devuelven True o False



def validar_no_vacio(valor):
    if not valor.strip() != "":
        return False, "El valor no puede estar vacío."

    return True, ""


def validar_entero_positivo(valor):
    if not valor.strip() != "":
        return False, "El valor no puede estar vacío."

    if not valor.isdigit():
        return False, "El valor debe ser un entero positivo."

    if int(valor) <= 0:
        return False, "El valor debe ser un entero positivo."

    return True, ""


def validar_documento_uruguayo(documento):
    if not documento.strip() != "":
        return False, "El valor no puede estar vacío."

    documento = str(documento).strip()
    if not re.fullmatch(r"\d{8}", documento):
        return False, "El documento debe ser una cédula uruguaya de 8 números."

    return True, ""


def validar_fecha(valor):
    if not valor.strip() != "":
        return False, "La fecha no puede estar vacía."

    try:
        datetime.strptime(valor.strip(), "%Y-%m-%d")
        return True, ""
    except ValueError:
        return False, "La fecha debe tener el formato AAAA-MM-DD."


def validar_estado(valor):
    if valor in ["CONFIRMADA", "ESPERA"]:
        return True, ""
    return False, "El estado debe ser CONFIRMADA o ESPERA."


def validar_horario(valor):
    if not valor.strip() != "":
        return False, "El horario no puede estar vacío."

    try:
        datetime.strptime(valor.strip(), "%H:%M:%S")
        return True, ""
    except ValueError:
        return False, "El horario debe tener el formato HH:MM:SS."


def validar_confirmacion(valor):
    if valor in ["S", "N"]:
        return True, ""
    return False, "La confirmación debe ser S o N."