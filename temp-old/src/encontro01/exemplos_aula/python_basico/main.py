import random

frases = [
    "A vida é como uma bicicleta: você precisa se manter em movimento para manter o equilíbrio. - Albert Einstein",
    "A única maneira de fazer um ótimo trabalho é amar o que você faz. - Steve Jobs",
    "A imaginação é mais importante que o conhecimento. - Albert Einstein",
    "Não tenha medo de desistir do bom para perseguir o ótimo. - John D. Rockefeller",
    "O sucesso é a soma de pequenos esforços repetidos dia após dia. - Robert Collier"
]

def sorteia_frase(numero):
    if numero <= 0 or numero > len(frases):
        return "Número inválido. Informe um número entre 1 e {}.".format(len(frases))

    frase_sorteada = random.choice(frases[:numero])
    return frase_sorteada

def main():
    try:
        numero = int(input("Informe um número para sortear uma frase (1 a {}): ".format(len(frases))))
        frase = sorteia_frase(numero)
        print("\nFrase sorteada:")
        print(frase)
    except ValueError:
        print("Entrada inválida. Por favor, informe um número válido.")

if __name__ == "__main__":
    main()
