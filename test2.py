import folium
import pandas as pd

m = folium.Map(location=[52.2297, 21.0122], zoom_start=12)

# 1. Популярные места в Варшаве
popular_places_data = {
    'Place': [
        'Stare Miasto', 'Plac Zamkowy', 'Zamek Królewski', 
        'Pałac Kultury i Nauki', 'Park Łazienkowski', 
        'Pałac w Wilanowie', 'POLIN Museum', 
        'Warsaw Uprising Museum', 'Copernicus Science Centre', 'Złote Tarasy'
    ],
    'Latitude': [
        52.2497, 52.24750, 52.24778, 52.23167, 52.21278, 
        52.16528, 52.24944, 52.2322, 52.2413, 52.23016
    ],
    'Longitude': [
        21.0122, 21.01361, 21.01417, 21.00639, 21.03278, 
        21.09028, 20.99306, 20.9813, 21.0289, 21.00241
    ],
    'Description': [
        "Старый город (исторический центр)", 
        "Дворцовая площадь", 
        "Королевский замок", 
        "Дворец культуры и науки", 
        "Парк Лазенки", 
        "Вилянувский дворец", 
        "Музей истории польских евреев POLIN", 
        "Музей Варшавского восстания", 
        "Научный центр Коперника", 
        "Торговый центр Złote Tarasy"
    ]
}

popular_df = pd.DataFrame(popular_places_data)
popular_group = folium.FeatureGroup(name="Популярные места")
for _, row in popular_df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"{row['Place']}<br>{row['Description']}",
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(popular_group)
m.add_child(popular_group)

# 2. Станции метро с пассажиропотоком
metro_data = {
    'Station': [
        'Kabaty', 'Natolin', 'Imielin', 'Stokłosy', 'Ursynów', 'Służew', 
        'Wilanowska', 'Wierzbno', 'Racławicka', 'Pole Mokotowskie', 
        'Politechnika', 'Centrum', 'Świętokrzyska', 'Ratusz Arsenał', 
        'Dworzec Gdański', 'Plac Wilsona', 'Marymont', 'Słodowiec', 
        'Stare Bielany', 'Wawrzyszew', 'Młociny'
    ],
    'Latitude': [
        52.13194, 52.13472, 52.14444, 52.15500, 52.16333, 52.17222, 
        52.18139, 52.18972, 52.19694, 52.21917, 52.21972, 52.22917, 
        52.23528, 52.24306, 52.25083, 52.26861, 52.27583, 52.28333, 
        52.29111, 52.29361, 52.29110
    ],
    'Longitude': [
        21.06500, 21.06028, 21.05833, 21.03417, 21.02472, 21.02083, 
        21.02306, 21.01694, 21.01028, 21.00250, 21.01417, 21.00389, 
        21.00833, 21.00528, 20.99417, 20.99333, 20.98056, 20.95389, 
        20.93528, 20.92250, 20.92890
    ],
    'Passenger_Flow': [
        5580000, 5280000, 5760000, 4890000, 3860000, 5750000,
        9670000, 6780000, 4340000, 6630000, 12350000, 20690000,
        13480000, 8840000, 7710000, 5090000, 3250000, 3410000,
        2870000, 3770000, 9090000
    ]
}
metro_df = pd.DataFrame(metro_data)
metro_group = folium.FeatureGroup(name="Станции метро")
for _, row in metro_df.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=row['Passenger_Flow'] / 4000000,  
        popup=f"{row['Station']}<br>{row['Passenger_Flow']} входов/выходов",
        color='blue',
        fill=True,
        fill_color='blue'
    ).add_to(metro_group)

metro_coords = list(zip(metro_df['Latitude'], metro_df['Longitude']))
folium.PolyLine(metro_coords, color="red", weight=3, opacity=0.8, popup="Маршрут метро").add_to(metro_group)

m.add_child(metro_group)

# 3. Учебные заведения
edu_data = {
    'Institution': [
        'Uniwersytet Warszawski', 'Politechnika Warszawska', 
        'SGH', 'Warszawski Uniwersytet Medyczny', 'SGGW', 'WAT'
    ],
    'Latitude': [52.2375, 52.2203, 52.2089, 52.2059, 52.1625, 52.2532],
    'Longitude': [21.0182, 21.0106, 21.0089, 20.9856, 21.0467, 20.9002],
    'Description': [
        'Варшавский университет (~50 тыс. студентов)',
        'Варшавская политехника (~30 тыс. студентов)',
        'Szkoła Główna Handlowa (~14 тыс. студентов)',
        'Медицинский университет',
        'Варшавский университет естественных наук (SGGW)',
        'Военная техническая академия (WAT)'
    ]
}
edu_df = pd.DataFrame(edu_data)
edu_group = folium.FeatureGroup(name="Учебные заведения")
for _, row in edu_df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"{row['Institution']}<br>{row['Description']}",
        icon=folium.Icon(color='purple', icon='book')
    ).add_to(edu_group)
m.add_child(edu_group)

# 4. Автобусные остановки
bus_data = {
    'Bus_Node': [
        'Dworzec Centralny', 'Dworzec Zachodni', 'Metro Politechnika (узел)',
        'Metro Młociny', 'Metro Wilanowska', 'Rondo Wiatraczna'
    ],
    'Latitude': [
        52.2298, 52.2208, 52.219, 52.29099, 52.1796, 52.2386
    ],
    'Longitude': [
        21.0038, 20.9679, 21.017, 20.92745, 21.0233, 21.0283
    ],
    'Passenger_Flow': [
        46400, 30000, 27800, 21000, 25000, 20000  
    ]
}
bus_df = pd.DataFrame(bus_data)
bus_group = folium.FeatureGroup(name="Автобусные узлы")
for _, row in bus_df.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=row['Passenger_Flow'] / 4000,
        popup=f"{row['Bus_Node']}<br>{row['Passenger_Flow']} пассажиров/день",
        color='orange',
        fill=True,
        fill_color='orange'
    ).add_to(bus_group)
m.add_child(bus_group)

# 5. ТОП-5 пиццерий в Варшаве
pizza_data = {
    'Pizzeria': [
        'Nonna Pizzeria', 'Ciao a Tutti', 'drożdż', 
        'Pizzaiolo (ul. Krucza)', 'Va Bene'
    ],
    'Latitude': [
        52.23795, 52.21729, 52.25233, 52.22662, 52.23861
    ],
    'Longitude': [
        21.01978, 21.00452, 20.99876, 21.01846, 21.02826
    ],
    'Rating': [5.0, 4.9, 4.8, 4.7, 4.6],
    'Description': [
        '№1 в списке лучших', '№2 в городе', 
        '№3 в рейтинге', '№4 в городе', 'Входит в топ-5'
    ]
}
pizza_df = pd.DataFrame(pizza_data)
pizza_group = folium.FeatureGroup(name="Пиццерии")
for _, row in pizza_df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"{row['Pizzeria']}<br>{row['Description']}<br>Рейтинг: {row['Rating']}",
        icon=folium.Icon(color='red', icon='cutlery')
    ).add_to(pizza_group)
m.add_child(pizza_group)

folium.LayerControl().add_to(m)

m.save("warsaw_analysis.html")
