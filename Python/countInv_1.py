import random


def contador_divisao_inversoes(array):
    
    return 1

def contador_inversoes(array):
    n = len(array)
    if n == 0  or n == 1:
        return 0
    else:
        meio = n//2
        inversoes_esquerda = contador_inversoes(array[meio:])
        inversoes_direita = contador_inversoes(array[:meio])
        inversoes_divisao = contador_divisao_inversoes(array)
    
    return inversoes_direita + inversoes_esquerda + inversoes_divisao
        
        
        

def main():
    vetor = random.sample(range(1, 101), 100)
    inversoes = contador_inversoes(vetor)
    print(vetor)
    print("Número de inversoes:", inversoes)
 
    vetor.sort()
    print(vetor)
    inversoes = contador_inversoes(vetor)
    print("Número de inversoes:",inversoes);



if __name__ == "__main__":
    main()