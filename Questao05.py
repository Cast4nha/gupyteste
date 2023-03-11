# Definindo uma string de exemplo
string_exemplo = input("Digite uma frase: ")

# Criando uma string vazia para armazenar o resultado
string_invertida = ""

# Percorrendo a string de trás para frente e adicionando cada caractere na nova string
for i in range(len(string_exemplo) - 1, -1, -1):
    string_invertida += string_exemplo[i]

# Imprimindo o resultado
print("String original:", string_exemplo)
print("String invertida:", string_invertida)


