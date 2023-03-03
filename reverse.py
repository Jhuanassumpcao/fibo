# entrada da string a ser invertida

string = input("Digite uma string: ")

# variável que armazenará a string invertida

string_invertida = ""

# percorre a string de trás para frente e adiciona cada caractere na string invertida

for i in range(len(string)-1, -1, -1):

    string_invertida += string[i]

# imprime a string invertida

print("A string invertida é:", string_invertida)

