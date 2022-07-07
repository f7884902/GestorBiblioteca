def buscarUsuario(cursor, mydb):
    aux = '1'
    while aux != '0':
        print('Digite:\n-1 se você deseja buscar pelo nome de um usuario \n- 2 se você deseja buscar pelo cpf'
              ' de um usuario \n-3 se você deseja buscar pelo e-mail de um usuario \n-4  se você deseja buscar pelo'
              ' telefone de um usuario\n-0 se você deseja sair')
        aux = input('Digite ação a ser tomada ')

        if aux == '1':
            nome_B = input('Digite qual nome do usuario do qual deseja visualizar')
            cursor.execute(f'select * from usuario where nome = "{nome_B}";')
            for x in cursor:
                print(x)
        elif aux == '2':
            cpf_B = input('Digite qual o CPF do usuario do qual deseja visualizar')
            cursor.execute(f'select * from usuario where cpf = {cpf_B};')
            for x in cursor:
                print(x)
        elif aux == '3':
            email_B = input('Digite qual email do usuario do qual deseja visualizar')
            cursor.execute(f'select * from usuario where email = "{email_B}";')
            for x in cursor:
                print(x)
        elif aux == '4':
            tel_B = input('Digite o numero do usuario que você deseja visualizar')
            cursor.execute(f'select * from usuario where telefone = "{tel_B}";')
            for x in cursor:
                print(x)
        elif aux == '0':
            quit()
        else:
            print('Opção invalida')