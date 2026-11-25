from sly import Parser
from .lexico import LEXICO as lexico

class ANALIZADOR(Parser):
    # Importar los tokens de "Lexico.py"
    tokens = lexico.tokens
    
    start = 'sentencia'
    
    # Al iniciar
    def __init__(self, variable : dict = None):
        self.variables = variable if variable is not None else {}
    
    @_('ID ASIGNACION expresion')
    def sentencia(self, p):
        self.variables[p.ID] = p.expresion
        return p.expresion

    @_('expresion')
    def sentencia(self, p):
        return p[0]
    
    # Suma
    @_('expresion SUMA termino')
    def expresion(self, p):
        try:
            return p.expresion + p.termino
        except TypeError:
            return None
            
    # Resta
    @_('expresion RESTA termino')
    def expresion(self, p):
        try:
            return p.expresion - p.termino
        except TypeError:
            return None
            
    # Multiplicacion
    @_('termino')
    def expresion(self, p):
        return p[0]

    @_('termino MULTIPLICACION factor')
    def termino(self, p):
        try:
            return p.termino * p.factor
        except TypeError:
            return None
            
    # Division
    @_('termino DIVISION factor')
    def termino(self, p):
        try:
            return p.termino / p.factor
        except TypeError:
            return None

    @_('factor')
    def termino(self, p):
        return p[0]

    @_('PARENTESIS_I expresion PARENTESIS_D')
    def factor(self, p):
        return p.expresion

    @_('literal')
    def factor(self, p):
        return p[0]
            
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
        