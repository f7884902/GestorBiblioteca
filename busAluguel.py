def buscarAluguel(cursor, mydb):
    print('Digite:\n-1 para listar todos os alugueis \n-2 para buscar um aluguel pelo id')
    aux = input('Digite ação a ser tomada ')
    if aux == '1':
        list = []
        cursor.execute('select * from aluguel;')
        i = 1
        for x in cursor:
            for col in x:
                list.append(col)
            print('\n'+'*'*25)
            print(f'Aluguel {i}')
            print('*'*25)
            print(f'ID: {list[0]}\nData inicio: {list[1]}\nData final: {list[2]}\nCodigo do livro: {list[3]}\nCPF Logradouro: {list[4]}')
            print('*'*25+'\n')
            list = []
            i += 1
    elif aux == '2':
        list = []
        id = input('Digite o id do aluguel: ')
        cursor.execute(f'select * from aluguel WHERE id_aluguel = {id};')
        for x in cursor:
            for col in x:
                list.append(col)
            print('\n'+'*'*25)
            print(f'ID: {list[0]}\nData inicio: {list[1]}\nData final: {list[2]}\nCodigo do livro: {list[3]}\nCPF Logradouro: {list[4]}')
            print('*'*25+'\n')
            list = []