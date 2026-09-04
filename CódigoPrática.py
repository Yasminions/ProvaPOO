#Este é o código em python, prova com o tema em PenhaS, este código foi baseado em um diagrama de classes feito no Astah e em sala de aula em grupo formado por: Annaly Lima, Yasmin Almeida, Larissa De Castro e Júlia Do Carmo.

#Essa é a classe Cadastro:
class Cadastro:
    def __init__(self, nome: str, email: str, senha: str, cep: int, cpf: int, apelido: str, genero: bool, raca: bool, data_de_nascimento: int, questionario: bool):
        self._nome = nome
        self._email = email
        self._senha = senha
        self._cep = cep
        self._cpf = cpf
        self._apelido = apelido
        self._genero = genero
        self._raca = raca
        self._data_de_nascimento = data_de_nascimento
        self._questionario = questionario