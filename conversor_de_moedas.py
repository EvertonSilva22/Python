real = float(input('Quanto dinheiro voçê tem na carteira? R$'))
real * 5
dolar = real / 5.04
print('Com {:.2f} voçê pode comprar US${:.2f}'.format(real, dolar))