class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo.title()
        self._autor = autor.title()
        self._ano_publicacao = ano_publicacao
        self._disponivel = True

    def __str__(self):
        return f'Titulo: {self._titulo}, Autor: {self._autor}, Ano de Publicação: {self._ano_publicacao}'
    
    def imprimir(self):
        print(f'Titulo do Livro: {self._titulo.ljust(20)} | Autor: {self._autor.ljust(20)} | Ano de Publicação: {self._ano_publicacao}')

    def emprestar(self):
        self._disponivel = False

    @property
    def disponibilidade(self):
        return 'Disponivel para Emprestimo' if self._disponivel else 'Emprestado'
    
    def imprimir_disponibilidade(self):
        print(f'Livro: {self._titulo} esta {self.disponibilidade}.')




    