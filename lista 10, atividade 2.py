import random

n_linhas, n_colunas = 10, 3 

notas_alunos = [[round(random.random()*10, 0) for x in range(n_colunas)] for y in range(n_linhas)] 

provas_menor_nota = {"p1": 0, "p2": 0, "p3":0} 

for indice_aluno, aluno in enumerate(notas_alunos):

   menor_nota = {"prova": 1, "nota": aluno[0]} 
   if(aluno[1]<menor_nota["nota"]):

       menor_nota["prova"] = 2

       menor_nota["nota"] = aluno[1]

   if(aluno[2]<menor_nota["nota"]):

       menor_nota["prova"] = 3

       menor_nota["nota"] = aluno[2]


   if(menor_nota["prova"] == 1):

       provas_menor_nota["p1"] += 1

   if(menor_nota["prova"] == 2):

       provas_menor_nota["p2"] += 1

   if(menor_nota["prova"] == 3):

       provas_menor_nota["p3"] += 1

   

   print(f'Aluno {indice_aluno}. Menor nota na prova {menor_nota["prova"]}: {menor_nota["nota"]}')

print(f'Menor nota por prova. Prova 1: {provas_menor_nota["p1"]}; Prova 2: {provas_menor_nota["p2"]}; Prova 3: {provas_menor_nota["p3"]};')
