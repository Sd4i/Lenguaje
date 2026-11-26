from sly import Lexer
from .errores import ErrorLexico

class LEXICO(Lexer):
    tokens = {
        NUMERO, CADENA, ID, BOOLEANO,
        SUMA, RESTA, MULTIPLICACION, DIVISION, ASIGNACION,
        PARENTESIS_I, PARENTESIS_D,
        Y_LOGICO, O_LOGICO, NO_LOGICO,
    }
    
    # Elementos a ignorar
    ignore          = " \t"

    # Definiciones RegEx
    SUMA            = r"\+"
    RESTA           = r"\-"
    MULTIPLICACION  = r"\*"
    DIVISION        = r"\/"
    ASIGNACION      = r"\="
    PARENTESIS_I    = r"\("
    PARENTESIS_D    = r"\)"
    Y_LOGICO        = r"&&"
    O_LOGICO        = r"\|\|"
    NO_LOGICO       = r"!"
    
    @_(r"\d+\.\d+", r"\d+")
    def NUMERO(self, t):
        t.value = float(t.value) if "." in t.value else int(t.value)
        return t

    @_(r'"[^"\\]*(\\.[^"\\]*)*"', r"'[^'\\]*(\\.[^'\\]*)*'")
    def CADENA(self, t):
        t.value = t.value[1:-1]
        return t

    ID = r"[a-zA-Z_][a-zA-Z0-9_]*"
    ID['True'] = BOOLEANO
    ID['False'] = BOOLEANO

    def error(self, t):
        raise ErrorLexico(f"Caracter inesperado {t.value[0]!r}")
    