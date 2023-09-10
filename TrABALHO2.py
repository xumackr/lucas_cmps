def interface ():
    print("Bem Vindo a Lanchonete do Lucas Campos Dos Santos - RU(4461530)")
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
soma = float(0)
while True:
    interface()
    try:
        cod_pdt = int(input("Entre com Código do Produto: "))
    except:
        print("Código Invalido! Você digitou uma letra!")
        print("Voltando...")
        continue
    if (cod_pdt >= 100 and cod_pdt <= 105) or (cod_pdt >= 200 and cod_pdt <= 201):
        if (cod_pdt == 100):
            print("Você Pediu um Cachorro-Quente no Valor de R$ 9,00 ")
            soma += 9.00
        elif (cod_pdt == 101):
            print("Você Pediu um Cachorro-Quente Duplo no Valor de R$ 11,00 ")
            soma += 11.00
        elif (cod_pdt == 102):
            print("Você Pediu um X-Egg no Valor de R$ 12,00")
            soma += 12.00
        elif (cod_pdt == 103):
            print("Você Pediu um X-Salada no Valor de R$ 12,00")
            soma += 12.00
        elif (cod_pdt == 104):
            print("Você Pediu um X-Bacon no Valor de R$ 14,00")
            soma += 14.00
        elif (cod_pdt == 105):
            print("Você Pediu um X-Tudo no Valor de R$ 17,00")
            soma += 17.00
        elif (cod_pdt == 200):
            print("Você Pediu um Refrigenrante Lata no Valor de R$ 5,00")
            soma += 5.00
        elif (cod_pdt == 201):
            print("Você Pediu um X-Egg no Valor de R$ 4,00")
            soma += 4.00
    else:
        print("Código Invalido!")
        continue
    print("Deseja Pedir Mais Alguma Coisa ?")
    print("1 - Sim ")
    print("0 - Não ")
    sec_opc = int(input(">>"))
    if (sec_opc == 1):
        continue
    else:
        if (sec_opc > 1):
            print("Opção Invalida!")
            continue
        elif (sec_opc == 0):
            break
        else:
            continue
print("O Total a Ser Pago é: {:.2f}".format(soma))

