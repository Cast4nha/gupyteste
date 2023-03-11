# a) 1, 3, 5, 7, ___
def proximo_elemento_a(n):
    return n + 2

# b) 2, 4, 8, 16, 32, 64, ____
def proximo_elemento_b(n):
    return n * 2

# c) 0, 1, 4, 9, 16, 25, 36, ____
def proximo_elemento_c(n):
    return n ** 2

# d) 4, 16, 36, 64, ____
def proximo_elemento_d(n):
    return (int(n ** 0.5) + 2) ** 2

# e) 1, 1, 2, 3, 5, 8, ____
def proximo_elemento_e(n1, n2):
    return n1 + n2

# f) 2, 10, 12, 16, 17, 18, 19, ____
def proximo_elemento_f(n):
    if n == 2:
        return 10
    elif n == 10:
        return 12
    elif n == 12:
        return 16
    elif n == 16:
        return 17
    elif n == 17:
        return 18
    elif n == 18:
        return 19
    else:
        return None  # Caso não seja possível determinar o próximo elemento

# Testando as funções
print(proximo_elemento_a(7))  
print(proximo_elemento_b(64))  
print(proximo_elemento_c(36))  
print(proximo_elemento_d(64))  
print(proximo_elemento_e(8, 5)) 
print(proximo_elemento_f(19))  
