"""Solo gramatica: reconoce la sintaxis y construye el AST. No calcula nada."""
from sly import Parser
from .lexico import LEXICO as lexico
from .nodos import *
from .errores import ErrorSintactico

class ANALIZADOR(Parser):
    tokens = lexico.tokens
    start = "sentencia"

    precedence = (
        ("left", O_LOGICO),
        ("left", Y_LOGICO),
        ("right", NO_LOGICO),
        ("left", SUMA, RESTA),
        ("left", MULTIPLICACION, DIVISION),
        ("right", UMENOS),
    )

    @_("ID ASIGNACION expr")
    def sentencia(self, p):
        return Asignacion(p.ID, p.expr)

    @_("expr")
    def sentencia(self, p):
        return p.expr

    @_("expr SUMA expr",
       "expr RESTA expr",
       "expr MULTIPLICACION expr",
       "expr DIVISION expr")
    def expr(self, p):
        return OperacionBinaria(p[1], p.expr0, p.expr1)

    @_("RESTA expr %prec UMENOS")
    def expr(self, p):
        return OperacionUnaria("-", p.expr)
    
    @_("expr Y_LOGICO expr",
       "expr O_LOGICO expr")
    def expr(self, p):
        return OperacionBinaria(p[1], p.expr0, p.expr1)
    
    @_("NO_LOGICO expr")
    def expr(self, p):
        return OperacionUnaria("!", p.expr)

    @_("PARENTESIS_I expr PARENTESIS_D")
    def expr(self, p):
        return p.expr

    @_("NUMERO", "CADENA")
    def expr(self, p):
        return Literal(p[0])
    
    @_("BOOLEANO")
    def expr(self, p):
        return Literal(p.BOOLEANO == "True")

    @_("ID")
    def expr(self, p):
        return Variable(p.ID)

    def error(self, token):
        if token is None:
            raise ErrorSintactico("La expresion esta incompleta")
        raise ErrorSintactico(f"Token inesperado {token.value!r}")
