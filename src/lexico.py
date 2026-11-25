from sly import Lexer

class LEXICO(Lexer):
    tokens = {
        # Número
        NUMERO,
        # Operaciones Aritmeticas
        SUMA,
        RESTA,
        MULTIPLICACION,
        DIVISION,
        ASIGNACION,
        # Juego de parentesis
        PARENTESIS_I,
        PARENTESIS_D,
        # Cadena (String)
        CADENA,
        # Identificador
        ID,
    }
    
    # Elementos a ignorar
    ignore          = r" \t"
    literals        = {".", "!"}

    # Definiciones RegEx
    SUMA            = r"\+"
    RESTA           = r"\-"
    MULTIPLICACION  = r"\*"
    DIVISION        = r"\/"
    ASIGNACION      = r"\="
    PARENTESIS_I    = r"\("
    PARENTESIS_D    = r"\)"
    
    @_(r"[0-9]+")
    def NUMERO(self, t):
        t.value = int(t.value)
        return t
    
    @_(r'''("[^"\\]*(\\.[^"\\]*)*"|'[^'\\]*(\\.[^'\\]*)*')''')
    def CADENA(self , t):
        t.value = self.eliminar_comillas(t.value)
        return t
    
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

    def eliminar_comillas(self, text: str):
        if text.startswith('\"') or text.startswith('\''):
            return text[1:-1]
        return text