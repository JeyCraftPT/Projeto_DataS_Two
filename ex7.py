import pandas as pd

# Caminhos
dados_path = 'estacoesPT.csv'
stations_path = 'global_climate_data/ghcnd-stations.txt'
output_path = 'id_estacoesPT.csv'

# Ler ficheiro de estações
stations_cols = ['id', 'latitude', 'longitude', 'elevation', 'state', 'name']
stations = pd.read_fwf(stations_path, header=None, widths=[11, 9, 10, 7, 3, 31], names=stations_cols)
stations = stations[['id', 'name']].drop_duplicates()

# Carregar os dados filtrados e substituir IDs por nomes
df = pd.read_csv(dados_path)
df = df.merge(stations, on='id', how='left')
df.drop(columns=['id'], inplace=True)
df.rename(columns={'name': 'station_name'}, inplace=True)

# Guardar resultado
df.to_csv(output_path, index=False)

print("✅ IDs substituídos por nomes das estações em 'id_estacoesPT.csv'.")
