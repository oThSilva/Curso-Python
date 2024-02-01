# # kwargs(keyword arguments)
# def contatenar(**palavras):
#     frase = ""
#     for palavra in palavras.values():
#         frase += palavra + " "
#     print(frase)


# contatenar(a="Sou", b="Um", c="'Pythonista", d="Autodidata")


def funcao(nome, *args, **kwargs):
    print(nome)
    print(args)
    print(kwargs)
    for arg in args:
        print(arg)
    for kwarg in kwargs.values():
        print(kwarg)


funcao("Th", 5, 6, 7, 8, 9, a=1, b=2, c=3)


def exibir_carros(*kwarks):
    lista_de_carro = " "
    for carro in kwarks:
        lista_de_carro += carro + " "
    print(lista_de_carro)


exibir_carros("Gol", "Vectra", "Celta")
