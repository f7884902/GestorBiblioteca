def atualizarLivro(cursor, mydb):
    aux = '1'
    while aux != '0':
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