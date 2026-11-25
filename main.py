from src.lexico import LEXICO
from src.analizador import ANALIZADOR

def main():
    lexer = LEXICO()
    parser = ANALIZADOR()
    while True:
        text = input(">>> ")
        if text == "exit":
            break
        else:
            tokens = lexer.tokenize(text)
            print(parser.parse(tokens))

if __name__ == '__main__':
    main()