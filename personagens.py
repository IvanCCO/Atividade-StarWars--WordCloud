import csv
from wordcloud import (WordCloud, get_single_color_func)
import matplotlib.pyplot as plt
from nltk import FreqDist

# Importa os arquivos csv
# Retorna string de palavras separadas por espaço
def importarArquivos(listaArquivos):
    frases = []

    for arquivo in listaArquivos:
        with open(arquivo, 'r', encoding='utf-8') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                frases.append(row[1])
    
    texto = (' '.join(frases)).lower()

    return texto

# Verifica as top 10 palavras mais utilizadas no texto
# Retorna uma lista das 10 palavras
def topPalavras(texto):
    for letra in texto:
        if letra in [',', '!', '_', ';', '.', '"', '[', ']',':', '-']:
            texto = texto.replace(letra, '')

    freq_distribuicao = FreqDist(texto.split()).most_common()
    palavras = []

    contador = 0
    while len(palavras) < 10:
        palavras.append(freq_distribuicao[contador][0])
        contador += 1

    return palavras

texto = topPalavras(importarArquivos(["./Documentos/SW_EpisodeIV_ptBR.csv", "./Documentos/SW_EpisodeV_ptBR.csv", "./Documentos/SW_EpisodeVI_ptBR.csv"]))

wordcloud = WordCloud(collocations=False, background_color="white", colormap="gnuplot").generate(' '.join(texto))

plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()