import random
#data 08/02/2024
# versão modificada do mergesort que alem de ordenar conta o numero de inversoes que faz
def contador_intercala(vetor_A, vetor_B):
    inversoes = 0
    i = j = 0
    n = len(vetor_A)+len(vetor_B)
    vetor = []
    for k in range(n):
        if i == len(vetor_A):
            vetor.append(vetor_B[j])
            j+=1
        elif j ==len(vetor_B):
            vetor.append(vetor_A[i])
            i+=1
        elif vetor_A[i] < vetor_B[j]:
            vetor.append(vetor_A[i])
            i+=1
        else:
            vetor.append(vetor_B[j])
            j+=1
            inversoes += len(vetor_A)-i
     
    return inversoes,vetor

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
    inversoes,vetor_ordenado = contador_mergesort(vetor)
    print("Número de Inversões: ", inversoes)
    print("Vetor Ordenado: ",vetor_ordenado)




if __name__ == "__main__":
	main()