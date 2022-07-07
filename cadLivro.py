def cadastrarLivro(cursor, mydb):
    listA = []
    nome = input('Digite o nome do livro a ser cadastrado ')
    codigo = input('Digite o codigo do livro a ser cadastrado ')
    while True:
        autor = input('Digite o(s) autor(es) do livro a ser cadastrado (Digite 0 para sair):')
        if autor == '0':
            break
        else:
            listA.append(autor)
    edicao = input('Digite a edicao do livro a ser cadastrado ')
    editora = input('Digite a editora do livro a ser cadastrado ')
    ano = input('Digite o ano do livro a ser cadastrado ')
    cursor.execute(f'INSERT INTO livro (nome, codigo, autores, edicao, editora, ano) VALUES ("{nome}",'
                   f' {codigo},"{listA[0]}", "{edicao}", "{editora}", {ano});')
    for autor in listA:
        cursor.execute(f'INSERT INTO autores (nome, codigo) VALUES ("{autor}", {codigo});')
    mydb.commit()