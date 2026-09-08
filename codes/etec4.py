numero: int = 0
valor: int = 0
def calcular(numero: int):
    if numero == 1:
        return 1
    else:
        return numero + calcular(numero - 1)
    
numero = 2 
valor = (numero * 2 +(numero - 2)) * numero / 2
print(calcular(valor))

