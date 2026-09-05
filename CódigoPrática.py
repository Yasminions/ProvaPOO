#Este é o código em python, prova prática da matéria de POO com o tema em PenhaS, este código foi baseado em um diagrama de classes feito no Astah e na sala de aula em grupo formado pelas seguintes integrantes: Annaly Lima, Yasmin Almeida, Larissa De Castro e Júlia Do Carmo.

#Se você notar outro colaborador, pode ficar tranquila que esse código foi feito apenas pela Yasmin(eu) e essa outra conta é de um parente que deixou eu usar o computador pra poder fazer o código, então não se preocupe, o código é meu e de mais ninguém.

#Essa é a classe Cadastro, esses abaixo são os atributos e metodos da classe, a qual tem relação de herança com a classe Usuário aonde a classe usuário herda de Cadastro, pois o atributo informações pessoais (de usuário) tem todas os atributos da classe Cadastro.

from chatConversas import *

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
            print("Senha confirmada com sucesso!") 
        
        def responder_questionario(self):
            pass
        
        def ativar_modo_camuflado(self, boolean):
            print("Modo camuflado ativado!")

class Usuario(Cadastro):
    def __init__(self, informacoes_pessoais: str, modoCamuflado: bool, configuracoes: bool, sobre_o_penhaS: str, manualDeFuga: list, chat: int, pontosDeApoio: list):
        self._informacoes_pessoais = informacoes_pessoais
        self._modoCamuflado = modoCamuflado
        self._configuracoes = configuracoes
        self._sobre_o_penhaS = sobre_o_penhaS
        self._manualDeFuga = manualDeFuga
        self._chat = chat
        self._pontosDeApoio = pontosDeApoio

        def editar_configuracoes(self):
            pass

        def ativar_modo_camuflado(self, boolean):
            print("Modo camuflado ativado")
        #Caso tenha notado, o metodo ativar_modo_camuflado está presente tanto na classe Cadastro quanto na classe Usuario, porque quando você vai criar uma conta, você pode ativar o modo camuflado no meio do processo do cadastro, porém quando você já tem uma conta criada, você também pode ativar e desativar o modo camuflado, então por isso que o metodo está presente nas duas classes só que em locais diferentes, apenas esclarecendo caso tenha estranhado.

        def desativar_modo_camuflado(self, boolean):
            print("Modo camuflado desativado")

        def excluir_conta(self, boolean):
            print("Conta excluída com sucesso!")
            
        def sair_da_conta(self, boolean):
            print("Você saiu da conta com sucesso!")

        def editar_informacoes_pessoais(self):
            pass 

class PontosDeApoio:
    def __init__(self, locais = str):
        self.__locais = locais

        def filtrar_pontos(self, string):
            print("Lista de pontos com filtros aplicados:")

        def pesquisar_por_endereco(self, string):
            print("Lista de resultados com filtros aplicados:")

class Chat:
    def __init__ (self, todasUsuarias, assistentePenhaS):
        self.__todasUsuarias = todasUsuarias
        self.__assistentePenhaS = assistentePenhaS

        def enviar_mensagem(self, string):
            print("Mensagem enviada")

        def receber_mensagem(self, string):
            print("Mensagem recebida")

        def receber_notificacao(self):
            pass

        def exibir_conversas(self):
            print(listaDeConversas)

        def filtrar_usuarias(self, string):
            print("Lista de usuárias com filtros aplicados:")

        def bloquear_usuaria(self):
           pass

        def apagar_usuaria(self):
            pass

#A classe PontosDeApoio tem relação de associação com a classe Usuario.