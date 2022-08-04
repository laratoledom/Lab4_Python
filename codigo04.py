n = int(input())
for i in range(n):
    x = int(input())
    pares = 0
    impares = 0
    maior = x
    print("Valor inicial:", x)
    while x != 1:
        if x > maior:
            maior = x
        if (x % 2) == 0:
            pares = pares + 1
            x = x/2
        else:
            impares = impares + 1
            x = (x*3) + 1
    impares = impares + 1
    print("Numeros Pares:", pares)
    print("Numeros Impares:", impares)
    print("Maior Numero:", int(maior))
