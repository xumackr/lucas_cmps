def dimensoesObjeto (): #Inicio da função dimensaoObjeto()
    while True:
        try:
            dimensoesOb = int(input("Qual a altura do Objeto sem PONTO (Em cm): "))
            comprimentoOb = int(input("Qual o comprimento do Objeto sem PONTO (Em Cm): "))
            larguraOb = int(input("Qual Largura do Objeto sem PONTO (Em Cm): "))
            total = dimensoesOb * comprimentoOb * larguraOb
            if (total < 1000 and total > 0): #Aqui caso o total seja 0 ou um valor negativo cai direto no else
                return 10
            elif (total >= 1000 and total < 10000):
                return 20
            elif (total >= 10000 and total < 30000):
                return 30
            elif (total >= 30000 and total < 100000):
                return 50
            elif (total >= 100000):
                print("O volume do Objeto é (em cm³): {}".format(total))
                print("Não aceitamos objeto com dimensões tão grandes")
                print("Por favor entre com a dimensões desejadas novamente")
                continue
            else:
             print("A soma das suas dimensões deu um valor negativo ou abaixo dos valores da tabela")
             print("Por favor entre com a dimensões desejadas novamente")
             continue
        except ValueError: #Caso o usuario digite uma letra
            print("Você Digitou Alguma dimensão errada com o valor não numérico")
            print("Por favor entre com a dimensões desejadas novamente")
            continue #Caso o usuario digite uma letra ou um numero float
# Fim da função dimensaoObjeto()

def pesoObjeto (): #Inicio da Função pesoObjeto()
    while True:
        try: #Aqui o programa vai tentar excutar um numero inteiro
            pesoOb = int(input("Digite o peso do Objeto sem PONTO (em kg): "))

            if (pesoOb <= 0.1):
                return (1)
            elif (pesoOb >= 0.1 and pesoOb < 1):
                return 1.5
            elif (pesoOb >= 1 and pesoOb < 10):
                return 2
            elif (pesoOb >= 10 and pesoOb < 30):
                return 3
            else: # Aqui é caso o ususario digite um numero fora da tabela vai repetir a exibir uma mensagem e repetir o inicio da função
                print("Não aceitamos objetos tão pesados")
                print("Por favor entre com o peso desejado novamente")
                continue
        except ValueError: #Tratamento de exceção caso o usuario digite uma letra ou um numero que nao seja inteiro (1.0)
            print("Você Digitou peso do objeto com o valor não numérico")
            print("Por favor entre com o peso desejado novamente")
            continue
# Fim da Função pesoObjeto()

def rotaObjeto (): #Inicio da Função rotaObjeto()
    while True:
        try: #Aqui o programa vai tentar excutar uma Função
            print("Selecione a rota:\n"
                  "BR - De Brasilia Para Rio de Janeiro\n"
                  "BS - De Brasilia para São paulo\n"
                  "RB - De Rio de Janeiro para Brasilia\n"
                  "RS - De Rio de janeiro para São paulo\n"
                  "SR - De São paulo para Rio de janeiro\n"
                  "SB - De São paulo para Brasilia")
            rotaOb = str(input(">>"))
            if (rotaOb in "BRbr"):
                return 1.5
            elif (rotaOb.upper() == "BS"):
                return 1.2
            elif (rotaOb.lower() in "rb"):
                return 1.5
            elif (rotaOb == "RS" or "rs"):
                return 1
            elif (rotaOb == "SR" or "sr"):
                return 1
            elif (rotaOb == "SB" or "sb"):
                return 1.2
            else:
                print("Você digitou uma rota que não existe")
                print("Por favor entre com a rota desejada novamente")
                continue
        except:#Aqui caso der qualquer erro de exceção o programa ja vai exibir duas mensagens na tela e voltar ao inicio da função
            print("Objeto Não aceito")
            print("Por favor entre com a rota desejada novamente")
            continue

print("Bem Vindo a companhia de Lógistica do Lucas Campos Dos Santos - RU(4461530)")
dimensoes = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
total = dimensoes * peso * rota
print("Total a pagar(R$): {:.2f} (dimensões: {} * peso: {} * rota: {})\n".format(total, dimensoes, peso, rota))

print("Lucas Campos dos Santos - RU(4461530)")