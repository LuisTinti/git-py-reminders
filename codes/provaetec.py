S = int(input("Qual é o seu salário"))
t = int(input("Quantas horas você trabalha?"))
a = (t + 0.10)
SF = S * (S * a * t)
print(SF)
# 0,10 ao invés de 0.10, por isso tava dando erro, mas agora ta certo, o problema era a vírgula, tem que ser ponto.