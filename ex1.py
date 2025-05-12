import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore")

# Caminho para o ficheiro original
input_path = 'global_climate_data/ghcnd_daily/ghcnd_daily.csv'
output_path = 'ghcnd_daily_processado.csv'

# Colunas a manter
columns_to_keep = ['id', 'year', 'month', 'element'] + [f'value{i}' for i in range(1, 32)]
value_cols = [f'value{i}' for i in range(1, 32)]

# Função para processar cada chunk
def process_chunk(chunk):
    chunk.replace(-9999, np.nan, inplace=True)
    chunk = chunk[columns_to_keep]

    # Otimização de tipos
    chunk['year'] = chunk['year'].astype('int16')
    chunk['month'] = chunk['month'].astype('int8')
    chunk['element'] = chunk['element'].astype('category')
    chunk['id'] = chunk['id'].astype('category')

    # Converter os valores e dividir por 10 para obter °C
    for col in value_cols:
        chunk[col] = chunk[col].astype('float32') / 10.0

    return chunk

# Processar em chunks e guardar no novo ficheiro
chunk_size = 100000
with pd.read_csv(input_path, chunksize=chunk_size) as reader:
    for i, chunk in enumerate(reader):
        processed = process_chunk(chunk)
        processed.to_csv(output_path, mode='a', header=(i == 0), index=False)

print("✅ Processamento completo. Dados guardados em 'ghcnd_daily_processado.csv' com temperaturas em °C.")
