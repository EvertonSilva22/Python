Dias = float(input('Quantos dias alugados? '))
KM = float(input('Quantos KM rodados? '))
Total = (Dias * 60) + (KM * 0.15)
print('O total a pagar é de R${:.2f}'.format(Total))