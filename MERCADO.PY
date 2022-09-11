
print('Seja bem-vindo')
print('Pronto para fazer algumas comprinhas?')
print('Então você vai ter que digitar o produto desejado: ')
print('11-Feijão(R$ 10) , 22- Macarrão(R$ 15), 33-Uva(R$ 20),44- beterraba(R$ 30)')
resultado:int
resultado1:int
codigo = input()
code = int(input('digite uma quantidade:'))
while(codigo!= '11' and codigo!= '22' and codigo!= '33' and codigo!= '44'):
    print('Codigo invalido')
    print('11-Feijão(R$ 10) , 22- Macarrão(R$ 15), 33-Uva(R$ 20),44- beterraba(R$ 30)')
    codigo = input()
    resultado = 0.0
    resultado1= 0.0
if codigo == '11':
   resultado = code * 10
   if resultado < 250:
      resultado1 = resultado - (resultado * 5)/100

elif codigo == '22':
     resultado = code * 15
     if resultado > 250 and resultado <= 500:
        resultado1 = resultado - (resultado * 10) / 100


elif codigo == '33':
     resultado = code * 20
     if resultado > 50:
        resultado1= resultado - (resultado * 15) / 100


elif codigo == '44' :
     resultado = code * 30




print('escolhido:',str(codigo))
print('quant:' ,str(code))
print('Total a pagar:',str(resultado), 'Com desconto:',str(resultado1))






