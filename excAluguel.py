def excluirAluguel(cursor, mydb):
    cpf_u = input('Digite o cpf do usuario que deseja devolver o livro')
    codigo_l = input('Digite o codigo do livro esta alugado')
    cursor.execute(f'DELETE from aluguel WHERE codigo = {codigo_l} and cpf = {cpf_u};')
    mydb.commit()