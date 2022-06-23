import mysql.connector
import datetime


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database = "trabalhobd"
)
cursor = mydb.cursor()

hoje = datetime.date
print(hoje)

menu = '1'

while menu != '0':
    menu = input('Digite: \n-0 para sair \n-1 para cadastrar um livro \n-2 para cadastrar um usuário \n-3 para Atualizar'
                 ' um usuário\n-4 para atualizar um livro \n-5 para buscar um livro \n-6 para buscar um usuáro\n-7 para'
                 ' excluir um livro \n-8 para excluir um usuário \n-9 para realizar um empréstimo\n-10 para realizar uma devolução\n')

#Essa função irá cadastrar um livro no banco de dados;
    if menu == '1':
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

#Essa função irá cadastrar um usuário no banco de dados;
    elif menu == '2':
        cpf = input('Digite o cpf do usuário a ser cadastrado ')
        nome = input('Digite o nome do usuário a ser cadastrado ')
        tipo = input('Digite o tipo do usuário a ser cadastrado ')
        email = input('Digite o email do usuário a ser cadastrado ')
        telefone = input('Digite o telefone do usuário a ser cadastrado ')

        cursor.execute(f'INSERT INTO usuario (nome, cpf, email, telefone) VALUES ("{nome}", {cpf}, "{email}", '
                       f'{telefone});')
        mydb.commit()

#Essa função irá atualizar um usuário no banco de dados;
    elif menu == '3':
        print('Digite:\n-0 para sair\n-1 se você deseja atualizar nome do usuário\n-2 se você deseja atualizar o cpf do usuário\n'
            '-3 se você deseja atualizar o email do usuário\n-4 se você deseja atualizar o telefone do usuário\n')
        aux = input('Digite ação a ser tomada ')
        if aux == '1':
            nome_at = input('Digite qual nome deseja alterar')
            nome_att = input('Digite o nome a ser atualizado')
            cursor.execute(f'UPDATE usuario SET nome = "{nome_att}" WHERE nome = "{nome_at}";')
            mydb.commit()
        elif aux == '2':
            cpf_at = input('Digite qual cpf deseja alterar')
            cpf_att = input('Digite o cpf a ser atualizado')
            cursor.execute(f'UPDATE usuario SET cpf = {cpf_att} WHERE cpf = {cpf_at};')
            mydb.commit()
        elif aux == '3':
            email_at = input('Digite qual email deseja alterar')
            email_att = input('Digite o email a ser atualizado')
            cursor.execute(f'UPDATE usuario SET email = "{email_att}" WHERE email = "{email_at}";')
            mydb.commit()
        elif aux == '4':
            telefone_at = input('Digite qual telefone deseja alterar')
            telefone_att = input('Digite o telefone a ser atualizado')
            cursor.execute(f'UPDATE usuario SET telefone = {telefone_att} WHERE telefone = {telefone_at};')
            mydb.commit()
        elif aux == '0':
            quit()
        else:
            print('Opção invalida')

#Essa função irá atualizar os dados de um livro;
    elif menu == '4':
        print('Digite:\n-0 para sair\n-1 se você deseja atualizar o nome de um livro \n-2 se você deseja atualizar o codigo'
              ' de um livro \n-3 se você deseja atualizar os autores de um livro \n-4  se você deseja atualizar'
              ' a edicao de um livro \n-5 se você deseja atualizar o ano de um livro \n-6  se você deseja'
              ' atualizar a editora de um livro \n')

        aux = input('Digite ação a ser tomada ')

        if aux == '1':
            codigo = int(input('Digite qual codigo do livro que deseja alterar o nome'))
            nome_att = input('Digite o nome a ser atualizado')
            cursor.execute(f'UPDATE livro SET nome = "{nome_att}" WHERE codigo = {codigo};')
            mydb.commit()
        elif aux == '2':
            cod_at = input('Digite o codigo do livro que deseja alterar')
            cod_att = input('Digite o codigo a ser atualizado')
            cursor.execute(f'UPDATE livro SET codigo = "{cod_att}" WHERE codigo = "{cod_at}";')
            mydb.commit()
        elif aux == '3':
            codigo = int(input('Digite o codigo do livro que deseja alterar o nome do autor'))
            aut_att = input('Digite o autor a ser atualizado')
            cursor.execute(f'UPDATE livro SET autores = "{aut_att}" WHERE  codigo = {codigo};')
            mydb.commit()
        elif aux == '4':
            codigo = int(input('Digite o codigo do livro que deseja alterar a edição'))
            edi_att = input('Digite o edição a ser atualizado')
            cursor.execute(f'UPDATE livro SET edicao = "{edi_att}" WHERE codigo = {codigo};')
            mydb.commit()
        elif aux == '5':
            codigo = int(input('Digite o codigo do livro que deseja alterar o ano'))
            ano_att = input('Digite o ano a ser atualizado')
            cursor.execute(f'UPDATE livro SET ano = "{ano_att}" WHERE codigo = {codigo};')
            mydb.commit()
        elif aux == '6':
            codigo = int(input('Digite o codigo do livro que deseja alterar a editora'))
            edit_att = input('Digite o editora a ser atualizado')
            cursor.execute(f'UPDATE livro SET editora = "{edit_att}" WHERE codigo = {codigo};')
            mydb.commit()
        elif aux == '0':
            quit()
        else:
            print('Opção invalida')

#Essa função irá buscar um livro no banco de dados;
    elif menu == '5':
        print('Digite:\n-0 para sair\n-1 se você deseja buscar pelo nome de um livro \n-2 se você deseja buscar pelo codigo'
              ' de um livro \n-3 se você deseja buscar pelos autores de um livro \n-4  se você deseja buscar pela'
              ' edicao de um livro \n-5 se você deseja buscar pelo ano de um livro \n-6  se você deseja'
              ' buscar pela editora de um livro\n')

        aux = input('Digite ação a ser tomada ')

        if aux == '1':
            nome_B = input('Digite qual nome do livro do qual deseja visualizar')
            cursor.execute(f'select * from livro where nome = "{nome_B}";')
            for x in cursor:
                print(x)

        elif aux == '2':
            cod_B = input('Digite qual código do livro do qual deseja visualizar')
            cursor.execute(f'select * from livro where codigo = {cod_B};')
            for x in cursor:
                print(x[1])
        elif aux == '3':
            aut_B = input('Digite qual autor do livro do qual deseja visualizar')
            cursor.execute(f'select * from autores where nome = "{aut_B}";')
            for x in cursor:
                print(x)
        elif aux == '4':
            edi_B = input('Digite qual edição do livro do qual deseja visualizar')
            cursor.execute(f'select * from livro where edicao = "{edi_B}";')
            for x in cursor:
                print(x)
        elif aux == '5':
            ano_B = input('Digite qual ano do livro do qual deseja visualizar')
            cursor.execute(f'select * from livro where ano = {ano_B};')
            for x in cursor:
                print(x)
        elif aux == '6':
            edit_B = input('Digite qual editora do livro do qual deseja visualizar')
            cursor.execute(f'select * from livro where editora = "{edit_B}";')
            for x in cursor:
                print(x)
        elif aux == '0':
            quit()
        else:
            print('Opção invalida')

#Essa função irá buscar um usuário no banco de dados;
    elif menu == '6':
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

#Essa função irá excluir um livro do banco de dados;
    elif menu == '7':
            cod_E = input('Digite o código do livro a ser excluido')
            cursor.execute(f'DELETE from livro WHERE codigo = {cod_E};')
            mydb.commit()

    #Essa função irá excluir um usuário do banco de dados;
    elif menu == '8':
            cpf_E = input('Digite o cpf do usuario a ser excluido')
            cursor.execute(f'DELETE from usuario WHERE cpf = {cpf_E};')
            mydb.commit()

    #Essa função realizará um empréstimo;
    elif menu == '9':
        dataInicio = datetime.datetime.now()
        datai = f'{dataInicio.day}/{dataInicio.month}/{dataInicio.year}'
        dataFinal = dataInicio + datetime.timedelta(days=7)
        dataf = f'{dataFinal.day}/{dataFinal.month}/{dataFinal.year}'
        cpf_u = input('Digite o cpf do usuario que deseja alugar um livro')
        codigo_l = input('Digite o codigo do livro que será alugado')
        cursor.execute(f'INSERT INTO loca (datai, dataf, codigo, cpf) VALUES("{datai}", "{dataf}", {codigo_l}, {cpf_u});')
        mydb.commit()

    elif menu == '10':
        cpf_u = input('Digite o cpf do usuario que deseja devolver o livro')
        codigo_l = input('Digite o codigo do livro esta alugado')
        cursor.execute(f'DELETE from loca WHERE codigo = {codigo_l} and cpf = {cpf_u};')
        mydb.commit()

cursor.execute('select * from usuario;')
for x in cursor:
  print(x)
