import datetime
def cadastrarAluguel(cursor, mydb):
    dataInicio = datetime.datetime.now()
    datai = f'{dataInicio.day}/{dataInicio.month}/{dataInicio.year}'
    dataFinal = dataInicio + datetime.timedelta(days=7)
    dataf = f'{dataFinal.day}/{dataFinal.month}/{dataFinal.year}'
    cpf_u = input('Digite o cpf do usuario que deseja alugar um livro')
    codigo_l = input('Digite o codigo do livro que será alugado')
    cursor.execute(f'INSERT INTO aluguel (datai, dataf, codigo, cpf) VALUES("{datai}", "{dataf}", {codigo_l}, {cpf_u});')
    mydb.commit()
