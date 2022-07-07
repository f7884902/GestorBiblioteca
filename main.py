import mysql.connector
from cadLivro import *
from cadUsuario import *
from cadAluguel import *
from attLivro import *
from attUsuario import *
from busLivro import *
from busUsuario import *
from busAluguel import *
from excAluguel import *
from excLivro import *
from excUsuario import *

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database = "trabalhobd"
)
cursor = mydb.cursor()
menu = '1'

while True:
    login = input('Digite o login: ')
    senha = input('Digite a senha: ')
    cursor.execute(f'select * from senhas where login = "{login}" && senha = "{senha}";')
    for x in cursor:
        loginUsuario = x[0]
        senhaUsuario = x[1]

    if loginUsuario == login and senhaUsuario == senha:
        while menu != '0':
            menu = input('Digite:\n-0 para sair \n-1 para cadastrar um livro \n-2 para cadastrar um usuário \n-3 para Atualizar'
                         ' um usuário\n-4 para atualizar um livro \n-5 para buscar um livro \n-6 para buscar um usuáro\n-7 para'
                         ' excluir um livro \n-8 para excluir um usuário \n-9 para cadastrar um aluguel\n-10 para realizar uma'
                         ' devolução\n-11 para listar os alugueis\n')

            if menu == '1':
                cadastrarLivro(cursor, mydb)

            elif menu == '2':
                cadastrarUsuario(cursor, mydb)

            elif menu == '3':
                atualizarUsuario(cursor, mydb)

            elif menu == '4':
                atualizarLivro(cursor, mydb)

            elif menu == '5':
                buscarLivro(cursor, mydb)

            elif menu == '6':
                buscarUsuario(cursor, mydb)

            elif menu == '7':
                excluirLivro(cursor, mydb)

            elif menu == '8':
                excluirUsuario(cursor, mydb)

            elif menu == '9':
                cadastrarAluguel(cursor, mydb)

            elif menu == '10':
                excluirAluguel(cursor, mydb)

            elif menu == '11':
                buscarAluguel(cursor, mydb)
    else:
        print('Login ou senha invalido')