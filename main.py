from utils import *

def main():
	DataFrames = to_df()
	df = pd.concat(DataFrames)
	df_clean = remove_empty(df)
	df_clean.to_excel('resultado.xlsx', index=False)
	print('Finalizado!')
if __name__ == '__main__': 
	main()
