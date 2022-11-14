import csv
from nltk import FreqDist

frase = []
# palavras_inuteis = ['que', 'você', 'de', 'não', 'o', 'a', 'para', 'eu', 'está', 'um', 'é', ]

# Replace as , . ! ? -(sepah mais) por ""

letras_idiotas = [',', '!', '_', ';', '.', '"', '[', ']',':', '-',]
def isLetraInvalida(letra):

    for i in letras_idiotas:
        if i == letra:
            return True
    
    return False
    



with open("./Documentos/episodioIVLuke.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    frase.append(row[2])

with open("./Documentos/episodioVLuke.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    frase.append(row[2])

with open("./Documentos/episodioVILuke.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    frase.append(row[2])


text = ''.join(frase)

for k in text:
    if(isLetraInvalida(k)):
        k.replace('')
words = text.split()
fdist1 = FreqDist(words)


linha = fdist1.most_common()
frasesCertas = []
for i in linha:
    if i[1] > 1 and i[1] <= 8:
        frasesCertas.append(i)


for l in frasesCertas:
    print(l)

