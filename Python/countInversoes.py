import random

# funcao que por força bruta calcula a quantidade de inversoes necessarias para ordenar o array
def contador_inversoes(array):
    numero_inversoes = 0
    n = len(array) 
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            if array[i]>array[j]:
                numero_inversoes += 1
    
    return numero_inversoes


# funcao principal que chamara o contador de inversoes necessarias
def main():
    vetor = random.sample(range(1, 101), 100)
    inversoes = contador_inversoes(vetor)
    print("Vetor Aleatório:", vetor)
    print("Número de Inversões:", inversoes)




if __name__ == "__main__":
	main()