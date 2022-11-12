import pandas as pd
from os import system

system('cls')

df1 = pd.read_csv('Documentos/SW_EpisodeIV_ptBR.csv')

df2 = pd.read_csv('Documentos/SW_EpisodeV_ptBR.csv')

df3 = pd.read_csv('Documentos/SW_EpisodeVI_ptBR.csv')

print(df1['personagem'].value_counts().head())
print(df2['personagem'].value_counts().head())
print(df3['personagem'].value_counts().head())