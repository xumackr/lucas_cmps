print("Bem Vindo a Loja do Lucas Campos - RU(4461530)")
valor_produto = float(input("Entre com Valor do Produto: "))
valor_qntd = int(input("Entre com Valor da Quantidade: "))
# Existem outros modos de fazer esse programa, porém escolhi uma forma com base na matematica

if valor_qntd <= 9:
    print("Está Quantidade Não Tem Desconto Aplicado!")
    print(f"Valor Sem Desconto Foi: R$ {valor_produto * valor_qntd:.2f}")  # Aqui está uma outra forma de formatar a variavél sobre o texto
    print("Valor Com Desconto Foi: R$ {:.2f}".format(
    valor_produto * valor_qntd))  # Porém somente essa se enquadra nas versões anterios de python
elif (valor_qntd >= 10) and (valor_qntd <= 99):
    desconto = valor_produto * valor_qntd * (5 / 100)
    print("Valor Sem Desconto Foi: R$ {:.2f}".format(valor_produto * valor_qntd))
    print("Valor Com Desconto Foi: R$ {:.2f} (Desconto 5%)".format(valor_produto * valor_qntd - desconto))
elif (valor_qntd >= 100) and (valor_qntd <= 999):
    desconto = valor_produto * valor_qntd * (10 / 100)
    print("Valor Sem Desconto Foi: R$ {:.2f}".format(valor_produto * valor_qntd))
    print("Valor Com Desconto Foi: R$ {:.2f} (Desconto 10%)".format(valor_produto * valor_qntd - desconto))
else:
    desconto = valor_produto * valor_qntd * (10 / 100)
    print("Valor Sem Desconto Foi: R$ {:.2f}".format(valor_produto * valor_qntd))
    print("Valor Com Desconto Foi: R$ {:.2f} (Desconto 15%)".format(valor_produto * valor_qntd - desconto))

print("Lucas Campos dos Santos - RU(4461530)")