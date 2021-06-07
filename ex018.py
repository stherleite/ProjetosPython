import math
ang = float(input('Digite um ângulo:'))
sen = math.sin(math.radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang,sen))
cos = math.cos(math.radians(ang))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang,cos))
tag = math.tan(math.radians(ang))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang,tag))



