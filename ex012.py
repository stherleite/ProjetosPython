prod = float(input('Digite o valor do seu produto:R$'))
desc1 = prod * (5/100)
desc2 = prod - desc1
desc3 = prod - (prod * 10/100)
desc4 = prod - (prod * 15/100)
print('\n-->Seu produto era de R${:.2f}, com 5% de desconto ficará: R${:.2f} ; \ncom 10% ficará: R${:.2f} ; \ne com 15% ficará: R${:.2f}'.format(prod,desc2,desc3,desc4))
