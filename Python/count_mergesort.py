


def contador_mergesort(vetor):
    n = len(vetor)
    if n <=1 :
        return 0,vetor
    else:
        meio = n//2
        inversoes_esquerda,vetor_esquerda = contador_mergesort(vetor[:meio])
        inversoes_direita,vetor_direita = contador_mergesort(vetor[meio:])
        inversoes,vetor_resultado = contador_intercala(vetor_esquerda,vetor_direita)
        return (inversoes+inversoes_direita+inversoes_esquerda),vetor_resultado

def main():
    vetor = random.sample(range(1, 101), 100)
    print("Vetor Aleatório: ", vetor)
    inversoes,vetor = contador_mergesort(vetor)
    print("Número de Inversões: ", inversoes)
    print("Vetor Ordenado: ",vetor)




if __name__ == "__main__":
	main()