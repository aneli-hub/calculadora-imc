def calcular_imc(peso, altura):
    return peso / (altura ** 2)


def classificar_imc(imc):
    if imc < 18.5:
        return "baixo peso"
    elif imc <= 24.9:
        return "peso adequado"
    elif imc <= 29.9:
        return "sobrepeso"
    elif imc <= 34.9:
        return "obesidade grau I"
    elif imc <= 39.9:
        return "obesidade grau II"
    else:
        return "obesidade grau III"


def main():
    try:
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        print(f"\nClassificação: {classificacao}")
    except ValueError:
        print("Erro: Digite valores numéricos válidos. Use ponto (.) para decimais.")


if __name__ == "__main__":
    main()
