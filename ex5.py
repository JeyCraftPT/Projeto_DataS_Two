# media_diaria_temp.py

import pandas as pd

# Caminho para o ficheiro de entrada
file_path = 'ghcnd_daily_processado.csv'

# Colunas de temperaturas diárias
value_cols = [f'value{i}' for i in range(1, 32)]

# Tamanho do chunk
chunk_size = 100000

# Processar só o primeiro chunk para exemplo
for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    # Converter para °C (dividir por 10)
    chunk[value_cols] = chunk[value_cols]
    
    # Calcular média das temperaturas por linha
    chunk['daily_avg_temp'] = chunk[value_cols].mean(axis=1)
    
    # Mostrar as primeiras 5 linhas
    print("\n📊 Exemplo de observações com temperatura média diária:")
    print(chunk[['id', 'year', 'month', 'element', 'daily_avg_temp']].head())
    
    break  # Só precisamos do primeiro chunk como exemplo
