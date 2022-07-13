def atualizarUsuario(cursor, mydb):
    aux = '1'
    while aux != '0':
        print('Digite:\n-0 para sair\n-1 se você deseja atualizar nome do usuário\n-2 se você deseja atualizar o cpf do usuário\n'
              '-3 se você deseja atualizar o email do usuário\n-4 se você deseja atualizar o telefone do usuário\n')
        aux = input('Digite ação a ser tomada ')
        if aux == '1':
            nome_at = input('Digite qual nome deseja alterar')
            nome_att = input('Digite o novo nome ')
            cursor.execute(f'UPDATE usuario SET nome = "{nome_att}" WHERE nome = "{nome_at}";')
            mydb.commit()
        elif aux == '2':
            cpf_at = input('Digite qual cpf deseja alterar')
            cpf_att = input('Digite o novo cpf ')
            cursor.execute(f'UPDATE usuario SET cpf = {cpf_att} WHERE cpf = {cpf_at};')
            mydb.commit()
        elif aux == '3':
            email_at = input('Digite qual email deseja alterar')
            email_att = input('Digite o novo email ')
            cursor.execute(f'UPDATE usuario SET email = "{email_att}" WHERE email = "{email_at}";')
            mydb.commit()
        elif aux == '4':
            telefone_at = input('Digite qual telefone deseja alterar')
            telefone_att = input('Digite o novo telefone ')
            cursor.execute(f'UPDATE usuario SET telefone = {telefone_att} WHERE telefone = {telefone_at};')
            mydb.commit()
        elif aux == '0':
            quit()
        else:
            print('Opção invalida')