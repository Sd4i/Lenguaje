from src.lexico import LEXICO
from src.analizador import ANALIZADOR
from src.interprete import Interprete
from src.errores import ErrorLenguaje

def main():
    lexer, parser, interprete = LEXICO(), ANALIZADOR(), Interprete()
    while True:
        try:
            texto = input(">>> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not texto:
            continue
        if texto.lower() in {"exit", "salir"}:
            break
        try:
            ast = parser.parse(lexer.tokenize(texto))
            if ast is not None:
                resultado = interprete.ejecutar(ast)
                if resultado is not None:
                    print(resultado)
        except ErrorLenguaje as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
