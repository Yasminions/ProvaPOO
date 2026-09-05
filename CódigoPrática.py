#Este é o código em python, prova prática com o tema em PenhaS, este código foi baseado em um diagrama de classes feito no Astah e em sala de aula por grupo formado pelas seguintes integrantes: Annaly Lima, Yasmin Almeida, Larissa De Castro e Júlia Do Carmo.

#Essa é a classe Cadastro, esses abaixo são os atributos e metodos da classe, a qual tem relação de herança com a classe Usuário, aonde o atributo informações pessoais (de usuário) tem todas os atributos da classe cadastro.
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
        
        def confimar_senha(self, boolean):
            pass 
        
        def responder_questionario(self):
            pass
        
        def ativar_modo_camuflado(self, boolean):
            pass

class Usuario(Cadastro):
    def __init__(self, informacoes_pessoais: str, modoCamuflado: bool, configuracoes: bool, sobre_o_penhaS: str, manualDeFuga: list, chat: int, pontosDeApoio: list):
        self._informacoes_pessoais = informacoes_pessoais
        self._modoCamuflado = modoCamuflado
        self._configuracoes = configuracoes
        self._sobre_o_penhaS = sobre_o_penhaS
        self._manualDeFuga = manualDeFuga
        self._chat = chat
        self._pontosDeApoio = pontosDeApoio