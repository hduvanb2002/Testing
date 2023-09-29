#!/usr/bin/env python3
# coding: utf-8 

from datetime import datetime

class TarjetaCredito:
    def __init__(self):
        pass

    @staticmethod
    def filtrar_digitos(entrada):
        return ''.join(filter(str.isdigit, entrada))

    def validar_numero(self, numero):
        if len(numero) != 16:
            print("Validación del número de tarjeta: Fallida")
            return False
        print("Validación del número de tarjeta: Exitosa")
        return True

    def validar_fecha_expiracion(self, fecha_expiracion):
        if len(fecha_expiracion) != 4:
            print("Validación de fecha de expiración: Fallida (Formato incorrecto)")
            return False
        try:
            fecha = datetime.strptime(fecha_expiracion, '%m%y')
            if fecha <= datetime.now():
                print("Validación de fecha de expiración: Fallida (Fecha expirada)")
                return False
            print("Validación de fecha de expiración: Exitosa")
            return True
        except ValueError:
            print("Validación de fecha de expiración: Fallida (Valor incorrecto)")
            return False

    def validar_cvc(self, cvc):
        if len(cvc) == 3:
            print("Validación de CVC: Exitosa")
            return True
        print("Validación de CVC: Fallida")
        return False

    def verificar_saldo(self, monto):
        # Asumimos que esta función siempre devuelve True por simplicidad.
        # En una implementación real, necesitaríamos acceder a una base de datos o servicio externo.
        print("Comprobación de saldo: Exitosa")
        return True

    def validar(self, numero, fecha_expiracion, cvc, monto):
        if not self.validar_numero(numero):
            return "Número de tarjeta inválido."
        if not self.validar_fecha_expiracion(fecha_expiracion):
            return "Fecha de expiración inválida."
        if not self.validar_cvc(cvc):
            return "CVC inválido."
        if not self.verificar_saldo(monto):
            return "Saldo insuficiente."
        return "Tarjeta de crédito válida."

def interfaz_usuario():
    tarjeta = TarjetaCredito()

    numero = tarjeta.filtrar_digitos(input("Introduce el número de tarjeta (16 dígitos): "))
    fecha_expiracion = tarjeta.filtrar_digitos(input("Introduce la fecha de expiración (MM/YY): "))
    cvc = tarjeta.filtrar_digitos(input("Introduce el CVC (3 dígitos): "))
    monto = float(input("Introduce el monto de la compra: "))

    resultado = tarjeta.validar(numero, fecha_expiracion, cvc, monto)
    print(resultado)

if __name__ == "__main__":
    interfaz_usuario()
