from ex1 import Livro

livro1 = Livro('O Ultimo Olimpiano', 'Rick Riordan', 2002)
livro2 = Livro('O Caminho Jedi', 'LucasFilms', 2007)
livro3 = Livro('God of War I', 'Sony Playstation', 2022)

livro1.emprestar()
livro1.imprimir_disponibilidade()

def main():
    pass

if __name__ == '__main__':
    main()