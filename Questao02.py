def fibonacci(num):
    # Verificar se o número é 0 ou 1
    if num == 0:
        return [0]
    elif num == 1:
        return [0, 1]
    else:
        # Iniciar a sequência com os dois primeiros números
        fib = [0, 1]
        
        # Loop para calcular os demais números da sequência
        while fib[-1] < num:
            # Cada novo número é a soma dos dois anteriores
            proximo = fib[-1] + fib[-2]
            # Adicionar o novo número à sequência
            fib.append(proximo)
        
        # Verificar se o número informado pertence à sequência
        if num in fib:
            return f"O número {num} pertence à sequência de Fibonacci: {fib}"
        else:
            return f"O número {num} não pertence à sequência de Fibonacci: {fib}"


num = 21
resultado = fibonacci(num)
print(resultado)
