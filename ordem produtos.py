import random
prod1 = input('Digite seu 1ºproduto:')
prod2 = input('Digite seu 2ºproduto:')
prod3 = input('Digite seu 3ºproduto:')
prod4 = input('Digite seu 4º produto:')
prod5 = input('Digite seu 5ºproduto:')
prod6 = input('Digite seu 6ºproduto:')
lista=[prod1,prod2,prod3,prod4,prod5,prod6]
random.shuffle(lista)
print('A ordem de seus produtos são:')
print(lista)