import csv
from wordcloud import (WordCloud, get_single_color_func)
import matplotlib.pyplot as plt
from nltk import FreqDist
from deep_translator import GoogleTranslator
from monkeylearn import MonkeyLearn

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

texto = importarArquivos(["./Documentos/episodioIVThreepio.csv", "./Documentos/episodioVThreepio.csv", "./Documentos/episodioVIThreepio.csv"])

for x in texto:
    translated = GoogleTranslator(source='auto', target='en').translate(x)

    ml = MonkeyLearn('d76ff41fc801fe7b756112f46acaec550f93a468')
    data = [translated]
    model_id = 'cl_pi3C7JiL'
    result = ml.classifiers.classify(model_id, data)
    print(result.body)
    if (result.body[0]['classifications'][0]['tag_name'] == 'Positive'):
        positivos += 1
        positivos += result.body[0]['classifications'][0]['confidence']
    else:
        negativos += 1
        negativos += result.body[0]['classifications'][0]['confidence']

print(100 * '-')
print('Programa finalizado')
print(f'Positivos: {positivos}')
print(f'Negativos: {negativos}')
print(100 * '-')