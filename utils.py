#imports
import pandas as pd
import os

#Pega os arquivo .xlsx e faz uma lista com os DataFrame deles
def to_df(path='./planilhas/') -> list:
	files = [f'{path}{file}' for file in os.listdir(path) if file.endswith('.xlsx')]
	print('Arquivos: ')
	for i in range(len(files)):
		print(f'    {i + 1} | {files[i]}')
	dfs = [pd.read_excel(excel) for excel in files]
	return dfs

#Remove todas as linhas de um dataframe cujo a coluna "Quantidade" é igual a 0
def remove_empty(df) -> 'DataFrame':
	 return df.loc[df["Quantidade"] != 0]