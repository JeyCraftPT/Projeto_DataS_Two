# analisar_nulos.py

import pandas as pd

# Caminho para o ficheiro processado
file_path = 'ghcnd_daily_processado.csv'

# Inicializar contadores
chunk_size = 100000
null_counts = None
total_counts = 0

# Calcular valores nulos em chunks
for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    if null_counts is None:
        null_counts = chunk.isnull().sum()
    else:
        null_counts += chunk.isnull().sum()
    total_counts += len(chunk)

# Calcular percentagem de nulos
percent_nulls = (null_counts / total_counts) * 100
percent_nulls_sorted = percent_nulls.sort_values(ascending=False)

# Mostrar resultados
print("\n📊 Percentagem de valores nulos por coluna:")
print(percent_nulls_sorted)

# Mostrar variável com mais dados em falta
worst_col = percent_nulls_sorted.idxmax()
max_null_pct = percent_nulls_sorted.max()
print(f"\n❗ Variável com mais dados em falta: '{worst_col}' ({max_null_pct:.2f}%)")
