def buscarLivro(cursor, mydb):
    aux = '1'
    while aux != '0':
        print('Digite:\n-0 para sair\n-1 se você deseja buscar pelo nome de um livro\n-2 se você deseja buscar pelo codigo'
              ' de um livro\n-3 se você deseja buscar pela edicao de um livro\n-4 se você deseja buscar pelo ano de um'
              ' livro\n-5 se você deseja buscar pela editora de um livro\n')

        aux = input('Digite ação a ser tomada ')

        if aux == '1':
            nome_B = input('Digite qual nome do livro do qual deseja visualizar ')
            cursor.execute(f'select * from livros where nome = "{nome_B}";')
            for x in cursor:
                print(x)
        elif aux == '2':
            cod_B = input('Digite qual código do livro do qual deseja visualizar ')
            cursor.execute(f'select * from livros where codigo = {cod_B};')
            for x in cursor:
                print(x)
            cursor.execute(f'select * from autores where nome = "{nome_B}";')
            print('\nAutores: \n')
            for x in cursor:
                print(x)
        elif aux == '3':
            edi_B = input('Digite qual edição do livro do qual deseja visualizar ')
            cursor.execute(f'select * from livros where edicao = "{edi_B}";')
            for x in cursor:
                print(x)
        elif aux == '4':
            ano_B = input('Digite qual ano do livro do qual deseja visualizar ')
            cursor.execute(f'select * from livros where ano = {ano_B};')
            for x in cursor:
                print(x)
        elif aux == '5':
            edit_B = input('Digite qual editora do livro do qual deseja visualizar ')
            cursor.execute(f'select * from livros where editora = "{edit_B}";')
            for x in cursor:
                print(x)
        elif aux == '0':
            quit()
        else:
            print('Opção invalida')