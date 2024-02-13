from ex1 import Livro

livro1 = Livro('O Filho de Netuno', 'Rick Riordan', 2011)
livro2 = Livro('O Caminho Jedi', 'LucasFilm', 2007)
livro3 = Livro('God of War I', 'Sony Playstation', 2022)

livro1.emprestar()
livro1.imprimir_disponibilidade()

def main():
    pass

if __name__ == '__main__':
    main()
