def inverter_string(s):
    invertida = ""
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    return invertida

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

while True:
    entrada = input("Digite um número: ")
    
    if entrada.isdigit():
        num = int(entrada)
        if fibonacci(num):
            print(f"O número {num} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {num} não pertence à sequência de Fibonacci.")
        break
    else:
        print("Entrada inválida! Por favor, digite um número válido.")
