from src.lexico import LEXICO
from src.analizador import ANALIZADOR

def main():
    lexer = LEXICO()
    while True:
        text = input(">>> ")
        if text == "exit":
            break
        else:
            tokens = lexer.tokenize(text)
            parser = ANALIZADOR()
            print(parser.parse(tokens))

if __name__ == '__main__':
    main()