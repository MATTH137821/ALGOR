print("seja bem-vindo")


despesas = int(input('Digite o   total de seus gasto: '))
entradas =int(input('Digite o  total de suas entradas: '))
patrimonio = int(input("digite o valor atual de seu patrimonio sem entradas atuais "))
vt = entradas - despesas
print('O valor subtraido e guardado de sua economia mensal {}.'.format(vt))
print('o valor total de seu patrimonio mais as entradas {}, subtraido e final {}'.format(entradas+ patrimonio,vt + patrimonio))
print ('valor a ser guardado para investimento',  vt-(vt * 0.40))
