from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import spacy
import numpy as np

def createList(url):
  nlp = spacy.load('en_core_web_sm')
  html = urlopen(url)
  soup = BeautifulSoup(html, 'lxml')
  [s.extract() for s in soup(['style', 'script', 'document', 'head', 'title', 'footer', 'img', 'input', 'header', 'noscript','meta', 'a', 'nav', 'span', 'h1', 'h2', 'h3', 'time', 'persistent-banner', 'option', 'svg', 'button', 'ul', 'link'])]
  texto = soup.getText()

  linhas = (linha.strip() for linha in texto.splitlines())
  separaTexto = (frase.strip() for linha in linhas for frase in linha.split('  '))
  texto = '\n'.join(st for st in separaTexto if st)
  texto = re.sub('\n', '  ', texto)

  text = nlp(texto)
  sentencas = list(text.sents)

  return sentencas


lista1 = createList('https://www.ibm.com/cloud/learn/natural-language-processing')
lista2 = createList('https://www.tableau.com/learn/articles/natural-language-processing-examples')
lista3 = createList('https://www.sas.com/en_us/insights/analytics/what-is-natural-language-processing-nlp.html')
lista4 = createList('https://aliz.ai/en/blog/natural-language-processing-a-short-introduction-to-get-you-started/')
lista5 = createList('https://hbr.org/2022/04/the-power-of-natural-language-processing')

print(f'Primeira lista: \n{lista1}')
print(f'\nSegunda lista: \n{lista2}')
print(f'\nTerceira lista: \n{lista3}')
print(f'\nQuarta lista: \n{lista4}')
print(f'\nQuinta lista: \n{lista5}')
