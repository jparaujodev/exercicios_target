#1
"""
indice = 13 
soma = 0
k = 0

while k < indice:
    k = k + 1
    soma = soma + k

print(soma)
"""

#2
def fibonacci(numero):
    sequencia = [0, 1]
    while len(sequencia) < numero:
        proximo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo)
    return sequencia

numero = 2
print(fibonacci(numero))


#5

palavra_original = "target"


palavra_invertida = ""


for letra in palavra_original:
    palavra_invertida = letra + palavra_invertida

print("palavra original:", palavra_original)
print("palavra invertida:", palavra_invertida)



        