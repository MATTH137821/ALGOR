print('  Seja bem-vindo   ')
print('Ajudaremos a saber a sua categoria')

idade = int(input('Digite sua idade : '))
if idade < 5:
      print('Você não está apto a participar')
elif  idade >= 5 and idade <= 7:
                     print('infantil')
elif idade >= 8 and idade <= 10:
                     print('juvenil')
elif idade >= 11 and idade <=15:
                     print("adolescente")
elif idade >= 16 and idade <= 30:
                     print('adulto')
else:
                     print('senior')





