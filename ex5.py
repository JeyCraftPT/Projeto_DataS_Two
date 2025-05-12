import pandas as pd

file_path = 'ghcnd_daily_com_media.csv'
chunk_size = 100000
grouped_chunks = []

for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    # Converter coluna de temperatura para numérica
    chunk['daily_avg_temp'] = pd.to_numeric(chunk['daily_avg_temp'], errors='coerce')

    # Criar coluna 'year' se necessário
    if 'year' not in chunk.columns:
        if 'date' in chunk.columns:
            chunk['year'] = pd.to_datetime(chunk['date']).dt.year
        elif 'YYYYMM' in chunk.columns:
            chunk['year'] = chunk['YYYYMM'].astype(str).str[:4].astype(int)
        else:
            raise ValueError("Coluna de ano ('year', 'date' ou 'YYYYMM') não encontrada.")

    # Agrupar por id e ano
    grouped = chunk.groupby(['id', 'year'])['daily_avg_temp'].mean().reset_index()
    grouped_chunks.append(grouped)

# Concatenar e consolidar
final_result = pd.concat(grouped_chunks)
final_result = final_result.groupby(['id', 'year'])['daily_avg_temp'].mean().reset_index()

# Associar com nomes das estações
stations = pd.read_fwf('global_climate_data/ghcnd-stations.txt', colspecs=[(0,11), (12, 42)], names=['id', 'station_name'])
final_result = final_result.merge(stations, on='id', how='left')

print(final_result.head())
