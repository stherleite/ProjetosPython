n = float(input('Digite um número em metros:'))
Km = n / 1000
Hm = n / 100
Dam = n / 10
Dm = n * 10
Cm = n * 100
Mm = n * 1000
print('A medida de {} metros corresponde a: \n{:.2f} Km; \n{:.2f} Hm; \n{:.2f} Dam; \n{:.1f} Dm; \n{:.1f} Cm; \n{:.1f} Mm'.format(n,Km,Hm,Dam,Dm,Cm,Mm))