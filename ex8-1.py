import pandas as pd
import folium

# Caminhos
stations_path = 'global_climate_data/ghcnd-stations.txt'
estacoes_pt_nomes = ['HORTA', 'FUNCHAL', 'LISBOA', 'CASTELO BRANCO', 'FARO']
stations_cols = ['id', 'latitude', 'longitude', 'elevation', 'state', 'name']

# Ler dados
stations = pd.read_fwf(stations_path, header=None, widths=[11, 9, 10, 7, 3, 31], names=stations_cols)

# Filtrar por nome e por prefixo de país (PO ou POM → Portugal)
stations_pt = stations[
    stations['name'].str.contains('|'.join(estacoes_pt_nomes), case=False) &
    stations['id'].str.startswith(('PO', 'POM'))
]

# Mostrar resultado no terminal
print("📍 Estações meteorológicas portuguesas encontradas:")
print(stations_pt[['id', 'name', 'latitude', 'longitude']].to_string(index=False))

# Criar mapa centrado em Portugal
mapa = folium.Map(location=[39.5, -8.0], zoom_start=6)

# Adicionar marcadores
for _, row in stations_pt.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=f"{row['name']} ({row['id']})",
        tooltip=row['name'],
        icon=folium.Icon(color='blue', icon='cloud')
    ).add_to(mapa)

# Guardar mapa
mapa.save("estacoes_portuguesas.html")
print("🗺️ Mapa gerado como 'estacoes_portuguesas.html'")
