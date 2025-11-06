print("==Medidor de IMC==")

try: 
    peso = float("Digite o seu peso(kg): ")
    altura = float("(Digite a sua altura(cm): ")

    if altura <= 0 or peso <= 0:
        print("Erro: Peso e altura devem ser maiores que zero!")
    else:
        imc = peso / (altura ** 2)

        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obesidade"


    print(f"\n O seu IMC é :{imc:.2f}")
    print(f"Classificação: {classificacao}")

except ValueError:
    print("Erro: Digite apenas números válidos!")
except Exception as e:
    print(f"Erro inesperado: {e}")