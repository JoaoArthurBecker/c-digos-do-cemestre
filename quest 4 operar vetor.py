vetor = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
executando = True
while executando == True:
    opicoes = int(input("precione 1 para adicionar um número no vetor, 2 para mostrar o vetor, 3 para consultar um número do vetor, 4 para excluir um número do vetor, 5 para esvaziá-lo e 6 para finalizar o programa"))
    if opicoes == 6:
        executando = False
        print("fim do programa")
    if opicoes == 1:
        ad_numero = int(input("qual número deseja adicionar?"))
        vetor.append(ad_numero)
        print(vetor)
    if opicoes == 2:
        print(vetor)
    if opicoes == 3:
        op3 = int(input("digite o número do qual deseja buscar a posissão:"))
        index = vetor. index(op3)
        print(index)
    if opicoes == 4:
        op4 = int (input ( "digite o índice do número que deseja remover:"))
        vetor.pop (op4)
        print (vetor)
    if opicoes ==5:
        vetor.clear ()
        print (vetor)