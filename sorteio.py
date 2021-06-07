import random
nm1 = input('Digite o primeiro nome:')
nm2 = input('Digite o segundo nome:')
nm3 = input('Digite o terceiro nome:')
nm4 = input('Digite o quarto nome:')
nm5 = input('Digite o quinto nome:')
lista=[nm1,nm2,nm3,nm4,nm5]
print('O nome sorteado foi: {}'.format(random.choice(lista)))
