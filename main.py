#from livro import Livro
#from usuario import Usuario
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database = "trabalhobd"
)
cursor = mydb.cursor()


menu = '1'
'''livro_cad = []
usuario_cad = []
'''
while menu != '0':
    menu = input('Digite: \n-0 para sair \n-1 para cadastrar um livro \n-2 para cadastrar um usuário \n-3 para Atualizar'
                 'um livro \n-4 para atualizar um usuário \n-5 para buscar um livro \n-6 para buscar um usuáro\n-7 para'
                 ' excluir um livro \n-8 para excluir um usuário \n-9 para realizar um empréstimo ')

#Essa função irá cadastrar um livro no banco de dados;
    if menu == '1':
        nome = input('Digite o nome do livro a ser cadastrado ')
        codigo = input('Digite o codigo do livro a ser cadastrado ')
        autores = input('Digite o(s) autor(es) do livro a ser cadastrado ')
        edicao = input('Digite a edicao do livro a ser cadastrado ')
        editora = input('Digite a editora do livro a ser cadastrado ')
        ano = input('Digite o ano do livro a ser cadastrado ')
        cursor.execute(f'INSERT INTO livro (nome, codigo, autores, edicao, editora, ano) VALUES ("{nome}", {codigo},'
                       f' "{autores}", "{edicao}", "{editora}", {ano});')
        mydb.commit()

 #       livro = Livro(nome, codigo, autores, edicao, editora, ano)
 #       livro_cad.append(livro)

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

  #      usuario = Usuario(cpf, nome, tipo, email, telefone)
  #      usuario_cad.append(usuario)

#Essa função irá atualizar um usuário no banco de dados;
    elif menu == '3':
        print('Digite:\n-0 se você deseja atualizar nome do usuário\n-1 se você deseja atualizar o cpf do usuário\n'
            '-2 se você deseja atualizar o email do usuário\n-3 se você deseja atualizar o telefone do usuário')
        aux = input('Digite ação a ser tomada ')
        if aux == '0':
            nome_at = input('Digite qual nome deseja alterar')
            nome_att = input('Digite o nome a ser atualizado')
            cursor.execute(f'UPDATE usuario SET "{nome_at}" = "{nome_att}";')
            mydb.commit()
        elif aux == '1':
            cpf_at = input('Digite qual cpf deseja alterar')
            cpf_att = input('Digite o cpf a ser atualizado')
            cursor.execute(f'UPDATE usuario SET {cpf_at} = {cpf_att};')
            mydb.commit()
        elif aux == '2':
            email_at = input('Digite qual email deseja alterar')
            email_att = input('Digite o email a ser atualizado')
            cursor.execute(f'UPDATE usuario SET "{email_at}" = "{email_att}";')
            mydb.commit()
        elif aux == '3':
            telefone_at = input('Digite qual telefone deseja alterar')
            telefone_att = input('Digite o telefone a ser atualizado')
            cursor.execute(f'UPDATE usuario SET {telefone_at} = {telefone_att};')
            mydb.commit()

#Essa função irá atualizar os dados de um livro;

    elif menu == '4':
        print('Digite:\n-0 se você deseja atualizar o nome de um livro \n-1 se você deseja atualizar o codigo'
              ' de um livro \n-2 se você deseja atualizar os autores de um livro \n-3  se você deseja atualizar'
              ' a edicao de um livro \n-4 se você deseja atualizar o ano de um livro \n-5  se você deseja'
              ' atualizar a editora de um livro ')

        aux = input('Digite ação a ser tomada ')

        if aux == '0':
            nome_at = input('Digite qual nome deseja alterar')
            nome_att = input('Digite o nome a ser atualizado')
            cursor.execute(f'UPDATE livro SET nome = "{nome_att}" WHERE nome = "{nome_at}";')
            mydb.commit()
        elif aux == '1':
            cod_at = input('Digite qual codigo deseja alterar')
            cod_att = input('Digite o codigo a ser atualizado')
            cursor.execute(f'UPDATE livro SET codigo = "{cod_att}" WHERE codigo = "{cod_at}";')
            mydb.commit()
        elif aux == '2':
            aut_at = input('Digite qual autor deseja alterar')
            aut_att = input('Digite o autor a ser atualizado')
            cursor.execute(f'UPDATE livro SET autores = "{aut_att}" WHERE  autores = "{aut_at}";')
            mydb.commit()
        elif aux == '3':
            edi_at = input('Digite qual edição deseja alterar')
            edi_att = input('Digite o edição a ser atualizado')
            cursor.execute(f'UPDATE livro SET edicao = "{edi_att}" WHERE edicao = "{edi_at}";')
            mydb.commit()
        elif aux == '4':
            ano_at = input('Digite qual ano deseja alterar')
            ano_att = input('Digite o ano a ser atualizado')
            cursor.execute(f'UPDATE livro SET ano = "{ano_att}" WHERE ano = "{ano_at}";')
            mydb.commit()
        elif aux == '5':
            edit_at = input('Digite qual editora deseja alterar')
            edit_att = input('Digite o editora a ser atualizado')
            cursor.execute(f'UPDATE livro SET editora = "{edit_att}" WHERE editora = "{edit_at}";')
            mydb.commit()


#Essa função irá buscar um livro no banco de dados;
    elif menu == '5':
        print('Digite:\n-0 se você deseja buscar pelo nome de um livro \n-1 se você deseja buscar pelo codigo'
              ' de um livro \n-2 se você deseja buscar pelos autores de um livro \n-3  se você deseja buscar pela'
              ' edicao de um livro \n-4 se você deseja buscar pelo ano de um livro \n-5  se você deseja'
              ' buscar pela editora de um livro')

        aux = input('Digite ação a ser tomada ')

        if aux == '0':
            nome_B = input('Digite qual nome do livro do qual deseja visualizar')
            print('Digite o cóigo do livro que deseja buscar')
            cursor.execute(f'select * from livro where nome = "{nome_B}";')
            for x in cursor:
                print(x)

        elif aux == '1':
            cod_B = input('Digite qual código do livro do qual deseja visualizar')
            print('Digite o cóigo do livro que deseja buscar')
            cursor.execute(f'select * from livro where codigo = {cod_B};')
            for x in cursor:
                print(x)
        elif aux == '2':
            aut_B = input('Digite qual autor do livro do qual deseja visualizar')
            print('Digite o cóigo do livro que deseja buscar')
            cursor.execute(f'select * from livro where autores = "{aut_B}";')
            for x in cursor:
                print(x)
        elif aux == '3':
            edi_B = input('Digite qual edição do livro do qual deseja visualizar')
            print('Digite o cóigo do livro que deseja buscar')
            cursor.execute(f'select * from livro where edicao = "{edi_B}";')
            for x in cursor:
                print(x)
        elif aux == '4':
            ano_B = input('Digite qual nome do livro do qual deseja visualizar')
            print('Digite o cóigo do livro que deseja buscar')
            cursor.execute(f'select * from livro where ano = {ano_B};')
            for x in cursor:
                print(x)
        elif aux == '5':
            edit_B = input('Digite qual editora do livro do qual deseja visualizar')
            print('Digite o cóigo do livro que deseja buscar')
            cursor.execute(f'select * from livro where editora = "{edit_B}";')
            for x in cursor:
                print(x)

#Essa função irá buscar um usuário no banco de dados;
    elif menu == '6':
        print('Digite:\n-0 se você deseja buscar pelo nome de um usuario \n-1 se você deseja buscar pelo cpf'
              ' de um usuario \n-2 se você deseja buscar pelo e-mail de um usuario \n-3  se você deseja buscar pelo'
              ' telefone de um usuario')
        aux = input('Digite ação a ser tomada ')

        if aux == '0':
            nome_B = input('Digite qual nome do livro do qual deseja visualizar')
            print('Digite o cóigo do livro que deseja buscar')
            cursor.execute(f'select * from usuario where nome = "{nome_B}";')
            for x in cursor:
                print(x)

        elif aux == '1':
            cpf_B = input('Digite qual código do livro do qual deseja visualizar')
            print('Digite o cóigo do livro que deseja buscar')
            cursor.execute(f'select * from usuario where cpf = {cpf_B};')
            for x in cursor:
                print(x)
        elif aux == '2':
            email_B = input('Digite qual autor do livro do qual deseja visualizar')
            print('Digite o cóigo do livro que deseja buscar')
            cursor.execute(f'select * from usuario where email = "{email_B}";')
            for x in cursor:
                print(x)
        elif aux == '3':
            tel_B = input('Digite qual edição do livro do qual deseja visualizar')
            print('Digite o cóigo do livro que deseja buscar')
            cursor.execute(f'select * from usuario where telefone = "{tel_B}";')
            for x in cursor:
                print(x)

#Essa função irá excluir um livro do banco de dados;
    elif menu == '7':
            cod_E = input('Digite o código do livro a ser excluido')
            cursor.execute(f'DELETE from livro WHERE codigo = {cod_E};')
            mydb.commit()
'''


#Essa função irá excluir um usuário do banco de dados;
    elif menu == '8':

#Essa função realizará um empréstimo;
    elif menu == '9':

for x in livro_cad:
    print(x)

for x in usuario_cad:
    print(x)
'''

cursor.execute('select * from usuario;')
for x in cursor:
  print(x)
