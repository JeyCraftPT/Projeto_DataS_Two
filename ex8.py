# ex8_corrigido_v2.py

import pandas as pd
import folium

# Caminho para o ficheiro de estações
stations_path = 'global_climate_data/ghcnd-stations.txt'

# Lista de nomes-chave a procurar (case-insensitive)
keywords_pt = ['HORTA', 'FUNCHAL', 'LISBOA', 'CASTELO BRANCO', 'FARO', 'LISBON']

# Ler ficheiro de estações
stations_cols = ['id', 'latitude', 'longitude', 'elevation', 'state', 'name']
stations = pd.read_fwf(
    stations_path, header=None,
    widths=[11, 9, 10, 7, 3, 31],
    names=stations_cols
)

# Normalizar nomes e procurar qualquer das palavras-chave
stations['name_clean'] = stations['name'].str.upper()
mask = stations['name_clean'].str.contains('|'.join(keywords_pt), case=False, regex=True)
stations_pt = stations[mask].copy()

# Mostrar para verificação
print("\n📍 Estações encontradas:")
print(stations_pt[['id', 'name', 'latitude', 'longitude']])

# Criar o mapa centrado em Portugal
m = folium.Map(location=[39.5, -8.0], zoom_start=6)

# Adicionar marcadores
for _, row in stations_pt.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=row['name'].strip(),
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

# Guardar como HTML
m.save('mapa.html')
print("🗺️ Mapa criado: 'mapa_estacoes_portuguesas.html'")
