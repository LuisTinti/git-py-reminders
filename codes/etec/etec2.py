X = [10, 13, 5, 9 , 1 , 25, 44, 10, 7, 32]

for i in range(0, len(X) - 1):
    menor_indice = i
    for j in range(i + 1, len(X)):
        if X[j] < X[menor_indice]:
            menor_indice = j
    if menor_indice != i:
        X[i], X[menor_indice] = X[menor_indice], X[i]
print(X)

        


        