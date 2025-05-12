import pandas as pd
import folium

# Caminho para o ficheiro de estações
stations_path = 'global_climate_data/ghcnd-stations.txt'

# Procurar apenas "CASTELO BRANCO"
keywords_pt = ['CASTELO BRANCO']

# Ler ficheiro de estações
stations_cols = ['id', 'latitude', 'longitude', 'elevation', 'state', 'name']
stations = pd.read_fwf(
    stations_path, header=None,
    widths=[11, 9, 10, 7, 3, 31],
    names=stations_cols
)

# Filtrar apenas CASTELO BRANCO
stations['name_clean'] = stations['name'].str.upper()
mask = stations['name_clean'].str.contains('|'.join(keywords_pt), case=False, regex=True)
stations_cb = stations[mask].copy()

# Verificar se encontrou
print("\n📍 Estação encontrada:")
print(stations_cb[['id', 'name', 'latitude', 'longitude']])

# Criar o mapa centrado em Castelo Branco (ou usar a localização da estação)
if not stations_cb.empty:
    cb_lat = stations_cb.iloc[0]['latitude']
    cb_lon = stations_cb.iloc[0]['longitude']
    m = folium.Map(location=[cb_lat, cb_lon], zoom_start=10)

    # Adicionar marcador
    folium.Marker(
        location=[cb_lat, cb_lon],
        popup=stations_cb.iloc[0]['name'].strip(),
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

    # Guardar como HTML
    m.save('mapa.html')
    print("🗺️ Mapa criado: 'mapa.html'")
else:
    print("⚠️ Nenhuma estação encontrada com o nome 'CASTELO BRANCO'.")
