n= float(input('Quanto você tem na carteira? R$'))
print('Com R${:.2f} você pode comprar: \nUS$ {:.2f};\n£ {:.2f};\n{:.2f} IENE'.format(n,n / 5.55,n / 6.68, n / 0.05 ))