
frase = input("Digite uma frase: ") #exibe texto e capita a resposta do usuário
frase = frase.lower() #transforma a frase em minúsculo
contador = 0 #variavel contador

for letra in frase: #for, vai separar letra por petra na variavel frase
    if letra in 'aeiou': #if faz a validação de cada vogal dentro da variavel letra
        contador = contador + 1 #adiciona mais 1 a cada vogal encontrada na variavelk
 
print("Total de vogais:", contador) # exibe a quatidade de vogais na variavel