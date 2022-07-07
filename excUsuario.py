def excluirUsuario(cursor, mydb):
    cpf_E = input('Digite o cpf do usuario a ser excluido')
    cursor.execute(f'DELETE from usuario WHERE cpf = {cpf_E};')
    mydb.commit()