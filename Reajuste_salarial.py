Salario = float(input('Qual é o salario do funcionario? R$'))
Novo_Salario = Salario +(Salario * 15/100)
print('Um funcionário que ganhava R${:.3f}, com 15% de aumento, passa a receber R${:.3f}'.format(Salario, Novo_Salario))