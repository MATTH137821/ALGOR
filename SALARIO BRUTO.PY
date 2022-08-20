print('  Seja bem-vindo   ')
print('Ajudaremos a saber o valor total de seu salario')
print('A gratificação será calculada de acordo')

salario = int(input('Digite seu salario: '))
if salario < 350:
      print('sua gratificação é 100')
      print('seu salario menos o desconto com a gratificação',salario - (salario * 0.07)+100)
elif  salario >= 351 and salario <=600 :
      print('sua gratificação é 75')
      print('seu salario menos o desconto com a gratificação',salario - (salario * 0.07) + 75)
elif salario >= 601 and salario <= 900 :
      print('sua gratificação é 50')
      print('seu salario menos o desconto com a gratificação',salario - (salario * 0.07) + 50)
else :
      print('sua gratificação é 35')
      print('seu salario menos o desconto com a gratificação',salario - (salario * 0.07) + 35)

