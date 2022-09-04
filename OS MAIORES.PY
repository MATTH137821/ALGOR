print('SEJA BEM-vindo')
print('para efetuarmos a validação')
print('precisaremos dos numeros')
num1= int(input('escreva o primeiro numero: '))
num2=int(input('escreva o segundo numero : '))
num3= int(input('escreva o terceiro numero: '))
if num1 > num2 and num2 > num3 :
    print('{}{}{}.'.format(num1,num2,num3))
elif num2 > num1 and num1 > num3:
    print('{}{}{}.'.format(num2, num1, num3))
elif num3 > num1 and num2 > num1:
    print('{}{}{}.'.format(num1, num2, num3))
