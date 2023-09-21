#Inicio das Variaveis Globais
import random
listaProduct = [] #Aqui eu crio uma lista por vazio para atribuir futuramente um dicionario
codigoPeca = 0 #Aqui eu crio uma variavel com valor de zero que futuramente vai ser atribuida como variavel contadora
#Fim das variaveis globais

#Inicio de cadastrarPeca()
def cadastrarPeca(codigoP):
    print("Você selecionou a Opção Cadastrar Peças\n"
          "Código da peça: {:03}".format(codigoP))# Aqui acontece Junção de dois print() Graças ao '\n' o segundo print é imprimido na linha de baixo
    print("0 - Voltar")
    nomeP = input("Por favor entre com NOME da peça:")
    fabricanteP = input("Por favor entre com FABRICANTE da peça:")
    valorP = int(input("Por favor entre com VALOR(R$) da peça:"))
    if (nomeP or fabricanteP or valorP) == False:
        

    dicionarioP = {"codigo":codigoP, "nome":nomeP, "fabricante":fabricanteP, "valor":valorP}# Aqui se faz a criação de um dicionario
    listaProduct.append(dicionarioP.copy()) # Aqui a função adiciona a lista vazia um dicionario que futuramente vai servi para buscas

#Fim de cadastrarPeca()

#Inicio de consultarPeca()
def consultarPeca():
    while True:
        opcaoConsultar = input("Você Selecionou a Opção consultar Peça\n"+ #Junção de Input aqui se coloca o sinal de + pois é um elemento de entrada de dados
                                "Escolha a opção desejada: \n" +
                                "1 - Consultar Todas as Peças\n" +
                                "2 - Consultar Peças Por Código\n" +
                                "3 - Consultar Peças por Fabricante \n" +
                                "4 - Retornar\n" +
                                ">>")
        if (opcaoConsultar == "1"):
            for consul in listaProduct: #Aqui é a criação de buscas dentro do dicionario que esta dentro da lista
                print("____________________")
                for chaves, values in consul.items():# Aqui o for imprime a busca de todos os itens que estaram dentro do dicionario
                    print("{}: {}".format(chaves, values))
                print("____________________")

        elif (opcaoConsultar == "2"):
            consultaCdg = int(input("Digite o Código da Peça: "))
            for consul in listaProduct:
                if consul["codigo"] == consultaCdg: #Aqui irá buscar um item especifico, caso seja o mesmo codigo que o usuario digitou
                    print("____________________")
                    for chaves, values in consul.items():#Impresão do item especifico
                        print("{}: {}".format(chaves, values))
                    print("____________________")
        elif (opcaoConsultar == "3"):
            consultaCdg = input("Digite o Nome do Fabricante: ")
            for consul in listaProduct:
                if consul["fabricante"] == consultaCdg:#Aqui irá buscar um item especifico, caso seja o mesmo fabricante que o usuario digitou
                    print("____________________")
                    for chaves, values in consul.items():#Impresão do item especifico
                        print("{}: {}".format(chaves, values))
                    print("____________________")

        elif (opcaoConsultar == "4"):
            return #Caso o usario digite 4 retornar ao Programa principal
        else:
            print("Opção inválida. Tente Novamente")
            continue #Caso digitar um numero fora das opções volta ao inicio da função e repete as perguntas

#Fim de consultarPeca()

#Inicio de removerPeca()
def removerPeca():
    removeP = int(input("Você selecionou a Opção Remover Peça\n"+
                    "Digite o Código da Peça a ser Removida: "))
    for consul in listaProduct:
        if consul["codigo"] == removeP:#Aqui irá buscar um item especifico, caso seja o mesmo codigo que o usuario digitou
            listaProduct.remove(consul) #Aqui ira remover o item especifico dentro do dicionario que esta dentro da lista
            print("Peça Removida com sucesso")

#Fim de removerPeca()

#Inicio do Programa Principal
print("Bem-Vindo ao Controle de Estoque da Bicicletaria do Lucas Campos dos Santos - RU(4461530)")
while True:
    menu_principal = input("\nEscolha a opção desejada: \n"+
                            "1 - Cadastrar Peças\n"+
                            "2 - Consultar Peças\n"+
                            "3 - Remover Peças\n"+
                            "4 - Sair\n"+
                            ">>")
    if (menu_principal == "1"):
        codigoPeca = random.randint(1001, 9999) #Caso ele cadastre a peça a variavel inicia do zera e atribui + 1
        cadastrarPeca(codigoPeca) #Aqui entra na função cadastrarPeca()
    elif (menu_principal == "2"):
        print("Você Selecionou a Opção consultar Peça")
        consultarPeca()#Aqui entra na função consultarPeca()
    elif (menu_principal == "3"):
        removerPeca()#Aqui entra na função removerPeca()
    elif (menu_principal == "4"): #Caso o não queira mais cadastrar peças digita o 4
        print("Fechando.....")
        break
    else:
        print("Opção inválida. Tente Novamente")
        continue
