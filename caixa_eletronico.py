#Caixa Eletrônico

valor = int(input('Digite o valor a ser sacado: '))
total = valor
cedula_atual = 100
total_cedulas = 0

while True:
    if total >= cedula_atual:
        total = total - cedula_atual
        total_cedulas = total_cedulas + 1
    else:
        print(f'Total de {total_cedulas} cédula(s) de R$ {cedula_atual}')
        if cedula_atual == 100:
         cedula_atual = 50
        elif cedula_atual == 50:
           cedula_atual = 20
        elif cedula_atual ==20:
           cedula_atual = 10
        elif cedula_atual == 10:
           cedula_atual = 5
        elif cedula_atual == 5:
           cedula_atual = 1
        total_cedulas = 0
        if total == 0:
               break




