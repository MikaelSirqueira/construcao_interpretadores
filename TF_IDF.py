"""
Sua  tarefa  será  gerar  a  matriz  termo-documento  usando  TF-IDF  por  meio  da  aplicação  das 
fórmulas TF-IDF na matriz termo-documento criada com a utilização do algoritmo Bag of Words. Sobre 
o Corpus que recuperamos anteriormente.
"""

def createTF_IDF(linhaTermoDoc, lista, vocabulary, numberDoc):
  finalMatrix = []
  for number in linhaTermoDoc:
    tf = number/len(lista)
    #tratando divisao por zero
    if number == 0:
      idf = 0
    else:
      idf = np.log(numberDoc/number)
    tf_idf = tf * idf
    finalMatrix.append(tf_idf)

  return finalMatrix

tf_idf = [vocabulary]
tf_idf.append(createTF_IDF(vector, lista1, vocabulary, 5))
tf_idf.append(createTF_IDF(vector, lista2, vocabulary, 5))
tf_idf.append(createTF_IDF(vector, lista3, vocabulary, 5))
tf_idf.append(createTF_IDF(vector, lista4, vocabulary, 5))
tf_idf.append(createTF_IDF(vector, lista5, vocabulary, 5))

print(tf_idf[0])
print(tf_idf[1])
print(tf_idf[2])
print(tf_idf[3])
print(tf_idf[4])
print(tf_idf[5])

#print(f"\n\n Matriz sem visualização completa\n {np.stack(tf_idf, axis=1)}")
