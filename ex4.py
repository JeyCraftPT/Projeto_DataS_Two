# media_diaria_temp.py

import pandas as pd

# Caminho para o ficheiro de entrada
file_path = 'ghcnd_daily_processado.csv'

# Ficheiro de saída
output_path = 'ghcnd_daily_com_media.csv'

# Lista de colunas de temperatura diárias
value_cols = [f'value{i}' for i in range(1, 32)]

# Processamento em chunks
chunk_size = 100000
for i, chunk in enumerate(pd.read_csv(file_path, chunksize=chunk_size)):
    # Calcular a média das temperaturas diárias por linha (ignorando NaNs)
    chunk['daily_avg_temp'] = chunk[value_cols].mean(axis=1)
    
    # Guardar com a nova coluna
    chunk.to_csv(output_path, mode='a', header=(i == 0), index=False)

print("✅ Temperatura média diária calculada e guardada em 'ghcnd_daily_com_media.csv'.")
