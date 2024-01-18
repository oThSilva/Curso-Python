numero = int(input('Digite um numero: ' ))
while numero > 0:
    if numero % 2 == 0:
        print(f'{numero} PAR')
        numero = numero - 1
    else:
        print(f'{numero} ÍMPAR')
        numero = numero - 1
print('Fim do loop')