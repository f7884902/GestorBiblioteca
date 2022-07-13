def excluirLivro(cursor, mydb):
    cod_E = input('Digite o código do livro a ser excluido')
    cursor.execute(f'DELETE from livros WHERE codigo = {cod_E};')
    mydb.commit()