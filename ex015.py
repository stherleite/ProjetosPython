nd = int(input('Coloque o número de dias:'))
nk = float(input('Coloque o número de Km rodados:'))
x = nd * 60
y = nk * 0.15
xy = x + y
print('O preço a se pagar é de R${:.2f}'.format(xy))
