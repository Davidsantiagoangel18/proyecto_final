import folium
import sqlite3
from folium import plugins
import webbrowser

# Crear un objeto de mapa centrado en una ubicación específica
mapa = folium.Map(location=[4.631542830676619, -74.0661021466547], zoom_start=17)  # Latitud y longitud de Bogotá, Barrio Sucre

# Conectar nuevamente para leer y escribir datos en la base de datos
conn = sqlite3.connect('barber_shops.db')
cursor = conn.cursor()

# Leer los marcadores desde la base de datos
cursor.execute('SELECT * FROM barber_shops')
rows = cursor.fetchall()

# Añadir marcadores al mapa
for row in rows:
    marcador = {
        'ubicacion': [row[2], row[3]],
        'nombre': row[1],
        'imagen': row[5],
        'descripcion': row[6]
    }

    popup_html = f"""
        <b>{marcador['nombre']}</b><br>
        <img src='{marcador['imagen']}' alt='Imagen del lugar' style='max-width:300px;'><br>
        Descripción: {marcador['descripcion']}<br>
        <form id="form_{marcador['nombre']}">
            <textarea id="descripcion_{marcador['nombre']}" rows="4" cols="50"></textarea><br>
            <input type="button" value="Guardar Descripción" onclick="guardarDescripcion('{marcador['nombre']}')">
        </form>
    """
    
    icono = folium.CustomIcon(icon_image=marcador['imagen'], icon_size=(50, 50))
    folium.Marker(
        location=marcador['ubicacion'],
        popup=folium.Popup(popup_html, max_width=300),
        icon=icono
    ).add_to(mapa)

# Agregar control de dibujo al mapa
draw = plugins.Draw(export=True)
draw.add_to(mapa)

# Guardar el mapa como un archivo HTML
mapa.save('peluquerias_del_barrio_sucre_con_agregar.html')

# Función para agregar una nueva ubicación a la base de datos
def agregar_ubicacion(nombre, latitud, longitud, descripcion):
    cursor.execute('''
        INSERT INTO barber_shops (nombre, latitud, longitud, descripcion)
        VALUES (?, ?, ?, ?)
    ''', (nombre, latitud, longitud, descripcion))
    conn.commit()

# Función para guardar la descripción en la base de datos
def guardar_descripcion(nombre, descripcion):
    cursor.execute('''
        UPDATE barber_shops
        SET descripcion = ?
        WHERE nombre = ?
    ''', (descripcion, nombre))
    conn.commit()

# Función para procesar el archivo cargado por el usuario
def cargar_coordenadas(file):
    for line in file:
        data = line.strip().split(',')
        nombre = data[0]
        latitud = float(data[1])
        longitud = float(data[2])
        descripcion = data[3] if len(data) > 3 else ''
        agregar_ubicacion(nombre, latitud, longitud, descripcion)

# Agregar un formulario para cargar un archivo con coordenadas y descripción
formulario_html = """
    <form id="form_cargar_coordenadas">
        <input type="file" id="archivo_coordenadas" accept=".csv">
        <input type="button" value="Cargar Coordenadas" onclick="cargarCoordenadas()">
    </form>
"""

mapa.get_root().html.add_child(folium.Element(formulario_html))

# Agregar código JavaScript para manejar la carga de coordenadas
script_js = """
    function cargarCoordenadas() {
        var input = document.getElementById('archivo_coordenadas');
        var file = input.files[0];
        
        if (file) {
            var reader = new FileReader();
            reader.onload = function(e) {
                var lines = e.target.result.split('\\n');
                for (var i = 0; i < lines.length; i++) {
                    var data = lines[i].split(',');
                    if (data.length >= 3) {
                        var nombre = data[0].trim();
                        var latitud = parseFloat(data[1].trim());
                        var longitud = parseFloat(data[2].trim());
                        var descripcion = (data.length > 3) ? data[3].trim() : '';
                        agregarMarcador(nombre, latitud, longitud, descripcion);
                    }
                }
            };
            reader.readAsText(file);
        }
    }

    function agregarMarcador(nombre, latitud, longitud, descripcion) {
        var marker = L.marker([latitud, longitud]).addTo(map);
        var popup = `<b>${nombre}</b><br>Descripción: ${descripcion}`;
        marker.bindPopup(popup);
        agregar_ubicacion(nombre, latitud, longitud, descripcion);
    }
"""

mapa.get_root().script.add_child(folium.Element(script_js))

# Abrir el mapa en el navegador web predeterminado
webbrowser.open('peluquerias_del_barrio_sucre_con_agregar.html')






