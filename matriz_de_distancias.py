""" Mikael da Silva Sirqueira

Sua tarefa será gerar uma matriz de distância, computando o cosseno do ângulo entre todos os 
vetores que encontramos usando o tf-idf. Para isso use a seguinte fórmula para o cálculo do cosseno 
use  a  fórmula  apresentada  em  Word2Vector  (frankalcantara.com) 
(https://frankalcantara.com/Aulas/Nlp/out/Aula4.html#/0/4/2) e apresentada na figura a seguir:  
 
O resultado  deste trabalho  será uma matriz que relaciona cada um dos vetores já calculados 
com todos os outros vetores disponíveis na matriz termo-documento.  
"""

matrixDistance = []

for index, a in enumerate(tf_idf):
  for b in tf_idf:
    cos_sim = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    matrixDistance.append(cos_sim)

  print(matrixDistance[index])

