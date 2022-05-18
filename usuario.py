class Usuario:
    def  __init__(self, cpf, nome, tipo, email, telefone):
        self.cpf =  cpf 
        self.nome = nome
        self.tipo = tipo
        self.email = email
        self.telefone = telefone


    def __str__(self):
        string = f'Nome: {self.nome} \nCPF: {self.cpf}\ntipo: {self.tipo}' \
                 f'\nE-mail: {self.email}\nTelefone: {self.telefone} \n'
        return string
