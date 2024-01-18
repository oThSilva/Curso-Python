from datetime import datetime

print(datetime.now())
print(datetime.now().day)

#criar uma data
data_exemplo = datetime(2024, 2, 11)
print(data_exemplo)
print(type(data_exemplo))

#convertendo para datetime(não precisa mais)

data = datetime.strptime(input('Qual é a data? '), '%d/%m/%Y')
print(data)
print(type(data))

#para calcular o intervalo entre datas 
data_atual = datetime.now()
prazo = data_exemplo - data_atual
print(prazo.days)

#Desafio
dia_do_aniversario = datetime(2024, 2, 24)
dias_pro_aniversario = dia_do_aniversario - datetime.now()
print(dia_do_aniversario)