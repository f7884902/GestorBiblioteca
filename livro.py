class Livro:
    def __init__ (self, nome, codigo, autores, edicao, editora, ano):
        self.nome = nome
        self.codigo = codigo
        self.autores = autores
        self.edicao = edicao
        self.editora = editora
        self.ano = ano

    def __str__(self):
        string = f'Nome: {self.nome} \nCodigo do livro: {self.codigo}\nAutor: {self.autores}' \
                 f'\nEdição: {self.edicao}\nEditora: {self.editora} \nAno de publicação: {self.ano}\n'
        return string
