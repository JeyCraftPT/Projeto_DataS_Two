# anos_por_estacao.py

import pandas as pd

# Caminho para o ficheiro processado
file_path = 'ghcnd_daily_processado.csv'

# Dicionários para armazenar os anos mínimos e máximos por estação
min_years = {}
max_years = {}

# Processar em chunks
chunk_size = 100000
for chunk in pd.read_csv(file_path, usecols=['id', 'year'], chunksize=chunk_size):
    grouped = chunk.groupby('id')['year'].agg(['min', 'max'])
    
    for station_id, row in grouped.iterrows():
        # Atualizar anos mínimos
        if station_id in min_years:
            min_years[station_id] = min(min_years[station_id], row['min'])
            max_years[station_id] = max(max_years[station_id], row['max'])
        else:
            min_years[station_id] = row['min']
            max_years[station_id] = row['max']

# Criar DataFrame final com os resultados
df_anos = pd.DataFrame({
    'min_year': pd.Series(min_years),
    'max_year': pd.Series(max_years)
})

# Reset do índice para ter a coluna 'id'
df_anos.reset_index(inplace=True)
df_anos.rename(columns={'index': 'station_id'}, inplace=True)

# Mostrar amostra dos dados
print("\n📅 Intervalo de anos por estação:")
print(df_anos.head())

# Guardar em CSV, se quiseres
# df_anos.to_csv('anos_por_estacao.csv', index=False)
