def makeVocabulary(words):
  newLista = []
  result = []
  for i in enumerate(words):
    i = i[1]
    x = 0
    while x < len(i):
      result.append(f"{i[x]}")
      x += 1
      
  for i in result:
    i = re.sub(r'[^\w\s]','', f"{i}")
    if i != "":
      newLista.append(i)
  return list(set(newLista))


def createVector(document, vocabulary):
  vector = np.zeros(len(vocabulary))
  for word in document:
    words = word.text.split()
    for w in words:
      for x, voc in enumerate(vocabulary):
        if voc == w:
          vector[x] += 1
  return list(vector)

words = lista1 + lista2 + lista3 + lista4 + lista5

vocabulary = makeVocabulary(words)
vector = createVector(words, vocabulary)

print(vocabulary)
print(vector)
