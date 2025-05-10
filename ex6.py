import pandas as pd

# Caminhos
dados_path = 'ghcnd_daily_processado.csv'
stations_path = 'global_climate_data/ghcnd-stations.txt'
output_path = 'estacoesPT.csv'

# Estações a procurar
estacoes_pt = ['HORTA', 'FUNCHAL', 'LISBOA', 'CASTELO BRANCO', 'FARO']

# Ler ficheiro de estações
stations_cols = ['id', 'latitude', 'longitude', 'elevation', 'state', 'name']
stations = pd.read_fwf(stations_path, header=None, widths=[11, 9, 10, 7, 3, 31], names=stations_cols)

# Filtrar pelas estações portuguesas
stations_pt = stations[stations['name'].str.contains('|'.join(estacoes_pt), case=False)]
ids_pt = stations_pt['id'].tolist()

# Colunas a manter
colunas = ['id', 'year', 'month', 'element'] + [f'value{i}' for i in range(1, 32)]

# Filtrar os dados por ID
chunk_size = 100000
for i, chunk in enumerate(pd.read_csv(dados_path, usecols=colunas, chunksize=chunk_size)):
    chunk_filtrado = chunk[chunk['id'].isin(ids_pt)]
    chunk_filtrado.to_csv(output_path, mode='a', header=(i == 0), index=False)

print("✅ Dados das estações portuguesas extraídos para 'estacoePT.csv'.")
