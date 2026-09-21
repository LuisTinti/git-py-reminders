def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"
    binary = "" 
    while decimal > 0:
        rest = decimal % 2 
        binary = str(rest) + binary
        decimal = decimal // 2
    return binary
print(decimal_to_binary(300))
    