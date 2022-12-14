import csv
from wordcloud import (WordCloud, get_single_color_func)
import matplotlib.pyplot as plt
from nltk import FreqDist

stopwords = ['de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'é', 'com', 'uma', 'os', 'no', 'se', 'na', 'por', 'mais', 'as', 'dos', 'como', 'mas', 'foi', 'ao', 'ele', 'das', 'tem', 'à', 'seu', 'sua', 'ou', 'ser', 'quando', 'muito', 'há', 'nos', 'já', 'está', 'eu', 'também', 'só', 'pelo', 'pela', 'até', 'isso', 'ela', 'entre', 'era', 'depois', 'sem', 'mesmo', 'aos', 'ter', 'seus', 'quem', 'nas', 'me', 'esse', 'eles', 'estão', 'você', 'tinha', 'foram', 'essa', 'num', 'nem', 'suas', 'meu', 'às', 'minha', 'têm', 'numa', 'pelos', 'elas', 'havia', 'seja', 'qual', 'será', 'nós', 'tenho', 'lhe', 'deles', 'essas', 'esses', 'pelas', 'este', 'fosse', 'dele', 'tu', 'te', 'vocês', 'vos', 'lhes', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas', 'nosso', 'nossa', 'nossos', 'nossas', 'dela', 'delas', 'esta', 'estes', 'estas', 'aquele', 'aquela', 'aqueles', 'aquelas', 'isto', 'aquilo', 'estou', 'está', 'estamos', 'estão', 'estive', 'esteve', 'estivemos', 'estiveram', 'estava', 'estávamos', 'estavam', 'estivera', 'estivéramos', 'esteja', 'estejamos', 'estejam', 'estivesse', 'estivéssemos', 'estivessem', 'estiver', 'estivermos', 'estiverem', 'hei', 'há', 'havemos', 'hão', 'houve', 'houvemos', 'houveram', 'houvera', 'houvéramos', 'haja', 'hajamos', 'hajam', 'houvesse', 'houvéssemos', 'houvessem', 'houver', 'houvermos', 'houverem', 'houverei', 'houverá', 'houveremos', 'houverão', 'houveria', 'houveríamos', 'houveriam', 'sou', 'somos', 'são', 'era', 'éramos', 'eram', 'fui', 'foi', 'fomos', 'foram', 'fora', 'fôramos', 'seja', 'sejamos', 'sejam', 'fosse', 'fôssemos', 'fossem', 'for', 'formos', 'forem', 'serei', 'será', 'seremos', 'serão', 'seria', 'seríamos', 'seriam', 'tenho', 'tem', 'temos', 'tém', 'tinha', 'tínhamos', 'tinham', 'tive', 'teve', 'tivemos', 'tiveram', 'tivera', 'tivéramos', 'tenha', 'tenhamos', 'tenham', 'tivesse', 'tivéssemos', 'tivessem', 'tiver', 'tivermos', 'tiverem', 'terei', 'terá', 'teremos', 'terão', 'teria', 'teríamos', 'teriam', 'ei', 'pode', 'vai', 'vou', 'isso', 'você', 'então', 'threepio', 'lá', 'tudo', 'agora', 'ah', 'luke', 'chewie', 'sei', 'tempo', 'onde', 'vamos', 'aqui', 'garoto', 'sabe', 'lado', 'artoo', 'acho', 'oh', 'lando', 'han', 'quê', 'grande', 'nada', 'ainda', 'kenobi', 'ver', 'diz', 'imperador', 'apenas', 'única', 'parece', 'jabba', 'obiwan', 'alderaan', 'ficar', 'ajudeme', 'poderia', 'algo', 'coisa', 'uh', 'mestre', 'general', 'ben', 'espere', 'fazer', 'sobre', 'deve', 'quê', 'disso', 'tão', 'é', 'jedi', 'mim', 'diálogo', 'império', 'posso', 'owen', 'tio', 'pai', 'precisamos', 'olha', 'alguma', 'biggs', 'antes', 'droide', 'vader', 'areia', 'disse', 'acha', 'leia', 'droides', 'aí', 'ir', 'estarei', 'sistema', 'achei', 'assim', 'povo', 'qualquer', 'muita', 'poder', 'espero', 'escudo', 'código', 'passar', 'realmente', 'senado', 'certamente',' rápido', 'alguém', 'ohhh', 'hutt', 'senhor', 'deveria', 'coisas', 'irmã', 'filho', 'talvez', 'possa', 'novas', 'situação', 'colocálo', 'destino', 'comandante', 'bem']

# Importa os arquivos csv
# Retorna string de palavras separadas por espaço
def importarArquivos(listaArquivos):
    frases = []

    for arquivo in listaArquivos:
        with open(arquivo, 'r', encoding='utf-8') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                frases.append(row[2])
    
    texto = (' '.join(frases)).lower()

    return texto

# Verifica as top 30 palavras mais utilizadas no texto
# Retorna uma lista das 30 palavras
def topPalavras(texto):
    for letra in texto:
        if letra in [',', '!', '_', ';', '.', '"', '[', ']',':', '-']:
            texto = texto.replace(letra, '')

    freq_distribuicao = FreqDist(texto.split()).most_common()
    palavras = []

    contador = 0
    while len(palavras) < 30:
        if freq_distribuicao[contador][0] not in stopwords:
            palavras.append(freq_distribuicao[contador][0])
        contador += 1

    return palavras

class SimpleGroupedColorFunc(object):
    def __init__(self, color_to_words, default_color):
        self.word_to_color = {word: color
                              for (color, words) in color_to_words.items()
                              for word in words}

        self.default_color = default_color

    def __call__(self, word, **kwargs):
        return self.word_to_color.get(word, self.default_color)


class GroupedColorFunc(object):
    def __init__(self, color_to_words, default_color):
        self.color_func_to_words = [
            (get_single_color_func(color), set(words))
            for (color, words) in color_to_words.items()]

        self.default_color_func = get_single_color_func(default_color)

    def get_color_func(self, word):
        try:
            color_func = next(
                color_func for (color_func, words) in self.color_func_to_words
                if word in words)
        except StopIteration:
            color_func = self.default_color_func

        return color_func

    def __call__(self, word, **kwargs):
        return self.get_color_func(word)(word, **kwargs)

# texto = topPalavras(importarArquivos(["./Documentos/episodioIVLuke.csv", "./Documentos/episodioVLuke.csv", "./Documentos/episodioVILuke.csv"]))
# texto = topPalavras(importarArquivos(["./Documentos/episodioIVHan.csv", "./Documentos/episodioVHan.csv", "./Documentos/episodioVIHan.csv"]))
# texto = topPalavras(importarArquivos(["./Documentos/episodioIVLeia.csv", "./Documentos/episodioVLeia.csv", "./Documentos/episodioVILeia.csv"]))
# texto = topPalavras(importarArquivos(["./Documentos/episodioIVThreepio.csv", "./Documentos/episodioVThreepio.csv", "./Documentos/episodioVIThreepio.csv"]))
texto = topPalavras(importarArquivos(["./Documentos/episodioVIVader.csv"]))

wc = WordCloud(stopwords=stopwords, collocations=False, background_color="white").generate(' '.join(texto))

color_to_words = {
    'red': ['sim', 'bem', 'bom', 'esperança', 'força', 'certeza', 'amigo', 'ok', 'obrigado', 'ótimo', 'melhor', 'confiar'],
    'blue' : ['não', 'nunca', 'culpa', 'ruim', 'machucar', 'socorro', 'rebelde']
}

default_color = 'grey'

grouped_color_func = GroupedColorFunc(color_to_words, default_color)

wc.recolor(color_func=grouped_color_func)

plt.figure()
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()