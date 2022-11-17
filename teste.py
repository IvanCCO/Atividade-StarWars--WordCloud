import csv
from wordcloud import (WordCloud, get_single_color_func)
import matplotlib.pyplot as plt
from nltk import FreqDist
from deep_translator import GoogleTranslator
from monkeylearn import MonkeyLearn
import os
from time import sleep

positivos = 0
negativos = 0

# Retorna string de palavras separadas por espaço
def importarArquivos(listaArquivos):
    frases = []

    for arquivo in listaArquivos:
        with open(arquivo, 'r', encoding='utf-8') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                frases.append(row[2])
    
    return frases

texto = importarArquivos(["./Documentos/episodioIVThreepio.csv"])

contador = 0
for x in texto:
    contador += 1
    if contador == 9:
        os.system('clear')
        contador = 0

    translated = GoogleTranslator(source='auto', target='en').translate(x)

    ml = MonkeyLearn('8bcdb9e1b53ec19c7deffc5d712cd126430047f7')
    data = [translated]
    model_id = 'cl_NDBChtr7'
    result = ml.classifiers.classify(model_id, data)
    print(result.body)

    if (result.body[0]['classifications'][0]['tag_name'] == 'Positive'):
        positivos += 1
        positivos += float(result.body[0]['classifications'][0]['confidence'])
    else:
        negativos += 1
        negativos += float(result.body[0]['classifications'][0]['confidence'])

    print(100 * '-')
    print(f'Positivos: {positivos}')
    print(f'Negativos: {negativos}')
    print(100 * '-')