import os

print("🎯 Jogo da Forca!")
palavra = input("Digite a palavra da forca: (recomendamos que seja digitada por outro jogador, para não perder a graça do jogo.) ").lower()
os.system('cls' if os.name == 'nt' else 'clear')
tamanho = len(palavra)
acertos = "_" * tamanho
erros = 0
max_erros = 5
letras_usadas = ""

print("🎯 Jogo da Forca!")
print(f"A palavra tem:  {tamanho} letras")
print("Palavra: ", " " .join(acertos) )
while erros < max_erros and "_" in acertos:
    letra = input("\nDigite uma letra:").lower().strip()

    if len(letra) != 1 or not letra.isalpha():
        print("❌ Digite apenas 1 letra!")
        continue
    if letra in letras_usadas:
        print("⚠️ Você já tentou essa letra!")
        continue

    letras_usadas += letra

    if letra in palavra:
        print("✅ Acertou!")
        nova_palavra = ""
        for i in range(tamanho):
            if palavra[i] == letra:
                nova_palavra += letra
            else:
                nova_palavra += acertos[i]
        acertos = nova_palavra
    else:
        erros += 1
        print(f"❌ Errou! ({erros}/{max_erros})")
    print(acertos)

if "_" not in acertos:
    print("🎉 Você GANHOU!")
else: 
    print(f"💀 Perdeu! A palavra era: **{palavra.upper()}**")