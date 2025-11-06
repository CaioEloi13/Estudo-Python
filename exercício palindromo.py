frase = input("Digite uma frase: ")
frase = frase.lower()

invertida = frase[::-1]

if frase == invertida:
 print("é um palindromo")
else:
 print("não é um palindromo")