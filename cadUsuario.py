def cadastrarUsuario(cursor, mydb):
    cpf = input('Digite o cpf do usuário a ser cadastrado ')
    nome = input('Digite o nome do usuário a ser cadastrado ')
    email = input('Digite o email do usuário a ser cadastrado ')
    telefone = input('Digite o telefone do usuário a ser cadastrado ')

    cursor.execute(f'INSERT INTO usuario (nome, cpf, email, telefone) VALUES ("{nome}", {cpf}, "{email}", '
                   f'{telefone});')
    mydb.commit()