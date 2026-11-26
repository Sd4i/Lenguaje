"""Nodos del AST: describen QUE significa el codigo, sin ejecutarlo."""
from dataclasses import dataclass
from typing import Any

class Nodo:
    pass

@dataclass
class Literal(Nodo):
    valor: Any

@dataclass
class Variable(Nodo):
    nombre: str

@dataclass
class Asignacion(Nodo):
    nombre: str
    valor: Nodo

@dataclass
class OperacionBinaria(Nodo):
    operador: str
    izquierda: Nodo
    derecha: Nodo

@dataclass
class OperacionUnaria(Nodo):
    operador: str
    operando: Nodo
