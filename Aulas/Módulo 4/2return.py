# função que processa dados:
# print("Ola")


def exibir_cotacao_do_dia(moeda):
    if moeda == "usd":
        print(5.47)


exibir_cotacao_do_dia("usd")

# função que retorna dados:
cidade = input("Qual é a cidade?")


def obter_cotacao_do_dia(moeda):
    if moeda == "usd":
        return 5.47


cotacao = obter_cotacao_do_dia("usd")
if cotacao > 5:
    print("Investir na bolsa americana")
else:
    print("Não investir")
