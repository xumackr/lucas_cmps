print("Bem Vindo a Lanchonete do Lucas Campos dos Santos - RU(4461530)")
print("***************Cardápio***************")
print("| Código |       Descrição       | Valor |")
print("|  100   |   Cachorro-Quente     |  9,00 |")
print("|  101   | Cachorro-Quente Duplo | 11,00 |")
print("|  102   |          X-Egg        | 12,00 |")
print("|  103   |        X-Salada       | 12,00 |")
print("|  104   |         X-Bacon       | 14,00 |")
print("|  105   |         X-Tudo        | 17,00 |")
print("|  200   |   Refrigerante Lata   |  5,00 |")
print("|  201   |      Chá Gelado       |  4,00 |")
soma = 0
while True:
    codigoP = (input("Entre com Código desejado: "))
    if (codigoP != "100" and codigoP != "101" and codigoP != "102" and
                codigoP != "103" and codigoP != "104" and codigoP != "105" and
            codigoP != "200" and codigoP != "201" and codigoP != " "):
        print("Opração Invalida!!")
        continue

    elif (codigoP == "100"):
        print("Você Pediu um Cachorro-Quente No Valor de R$ 9,00 ")
        soma += 9 #aqui, toda vez que o cliente fizer mais um pedido vai ser acrescentado correspondente com o valor + soma
    elif (codigoP == "101"):
        print("Você Pediu um Cachorro-Quente Duplo No Valor de R$ 11,00 ")
        soma += 11
    elif (codigoP == "102"):
        print("Você Pediu um X-Egg Duplo No Valor de R$ 12,00 ")
        soma += 12
    elif (codigoP == "103"):
        print("Você Pediu um X-Salada Duplo No Valor de R$ 12,00 ")
        soma += 12
    elif (codigoP == "104"):
        print("Você Pediu um X-Bacon Duplo No Valor de R$ 14,00 ")
        soma += 14
    elif (codigoP == "105"):
        print("Você Pediu um X-Tudo Duplo No Valor de R$ 17,00 ")
        soma += 17
    elif (codigoP == "200"):
        print("Você Pediu um Refrigerante Lata Duplo No Valor de R$ 5,00 ")
        soma += 5
    elif (codigoP == "201"):
        print("Você Pediu um Chá Gelado Duplo No Valor de R$ 4,00 ")
        soma += 4

    print("Deseja Pedir Mais Alguma Coisa ?")
    print("1 - Sim ")
    print("0 - Não ")
    secPedido = (input(">>"))
    if (secPedido == "1"):
        continue   # caso for sim o programa volta a fazer a pergunta para entrar com codigo
    elif (secPedido > "1"):# Se caso for maior que 1 o programa dar oçao invalida e repete a pergunta
        print("Opção Invalida!")
        continue
    else:
        break # Aqui encerro o programa e avança para proxima parte
print("O Total a ser Pago é: R${:.2f} ".format(soma)) #Aqui é mostrado na tela a soma total

print("Lucas Campos dos Santos - RU(4461530)")