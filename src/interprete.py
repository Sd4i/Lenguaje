"""Ejecuta el AST. Cada tipo de nodo tiene su metodo visitar_<Nodo>."""
import operator
from .nodos import *
from .errores import ErrorEjecucion

class Interprete:
    BINARIOS = {
        "+": operator.add, "-": operator.sub,
        "*": operator.mul, "/": operator.truediv,
    }

    def __init__(self, variables: dict | None = None):
        self.variables = variables if variables is not None else {}

    def ejecutar(self, nodo):
        metodo = getattr(self, f"visitar_{type(nodo).__name__}", None)
        if metodo is None:
            raise ErrorEjecucion(f"Nodo sin implementar: {type(nodo).__name__}")
        return metodo(nodo)

    def visitar_Literal(self, n):
        return n.valor

    def visitar_Variable(self, n):
        if n.nombre not in self.variables:
            raise ErrorEjecucion(f"Variable no definida: {n.nombre}")
        return self.variables[n.nombre]

    def visitar_Asignacion(self, n):
        valor = self.ejecutar(n.valor)
        self.variables[n.nombre] = valor
        return valor

    def visitar_OperacionUnaria(self, n):
        valor = self.ejecutar(n.operando)
        if n.operador == '-':
            return -valor
        elif n.operador == '!':
            return not valor

    def visitar_OperacionBinaria(self, n):
        izq = self.ejecutar(n.izquierda)

        if n.operador == "&&":
            return bool(izq and self.ejecutar(n.derecha))
        if n.operador == "||":
            return bool(izq or self.ejecutar(n.derecha))

        der = self.ejecutar(n.derecha)
        try:
            return self.BINARIOS[n.operador](izq, der)
        except ZeroDivisionError:
            raise ErrorEjecucion("Division entre cero")
        except TypeError:
            raise ErrorEjecucion(
                f"No se puede usar '{n.operador}' entre "
                f"{type(izq).__name__} y {type(der).__name__}"
    )