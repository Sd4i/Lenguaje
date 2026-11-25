from sly import Parser
from .lexico import LEXICO as lexico

class ANALIZADOR(Parser):
    # Importar los tokens de "Lexico.py"
    tokens = lexico.tokens
    
    # Orden de lectura
    precedence = (
        ('left', 'SUMA', 'RESTA'),
        ('left', 'MULTIPLICACION', 'DIVISION'),
    )
    
    # Al iniciar
    def __init__(self, variable : dict = None):
        self.variables = variable or {}
    
    # "OperacionAritmetica" es una expresion
    @_('OperacionAritmetica')
    def expresion(self, p):
        return p[0]

    # "literal" es una expresion
    @_('literal')
    def expresion(self, p):
        return p[0]
    
    # Suma
    @_('expresion SUMA expresion')
    def OperacionAritmetica(self, p):
        try:
            return p[0] + p[2]
        except TypeError:
            return None
            
    # Resta
    @_('expresion RESTA expresion')
    def OperacionAritmetica(self, p):
        try:
            return p[0] - p[2]
        except TypeError:
            return None
            
    # Multiplicacion
    @_('expresion MULTIPLICACION expresion')
    def OperacionAritmetica(self, p):
        try:
            return p[0] * p[2]
        except TypeError:
            return None
            
    # Division
    @_('expresion DIVISION expresion')
    def OperacionAritmetica(self, p):
        try:
            return p[0] / p[2]
        except TypeError:
            return None
            
    @_('NUMERO',
       'NUMERO "." NUMERO',
       'CADENA')
    def literal(self, p):
        if len(p) > 1:
            return float(f"{p.NUMERO0}.{p.NUMERO1}")
        return p[0]

    @_('ID') 
    def literal(self, p):
        return self.variables.get(p[0], 0)
        