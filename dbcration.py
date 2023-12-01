import sqlite3

# Conectar a la base de datos SQLite (si no existe, se creará)
conn = sqlite3.connect('barber_shops.db')
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS barber_shops (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        latitud REAL,
        longitud REAL,
        enlace TEXT,
        imagen TEXT,
        descripcion TEXT
    )
''')

# Insertar datos en la base de datos (puedes reemplazarlo con tus propios datos)
datos_marcadores = [
    ('Master Barber Shop', 4.630522222, -74.065525, 'https://www.google.com/maps/place/Master+Barber+Shop/...', 'https://lh5.googleusercontent.com/p/AF1QipNafyDmNOGuK3cWP3LgLyEOVHxHxTCvlxrvfaCd=w408-h544-k-no', 'Carrera 13a 32 67 local 8, Bogotá, Colombia'),
    ('Berlin Barber Shop', 4.627774100535496, -74.06680007144863, 'https://www.google.com/maps/place/Barberia+Berlín+Barber+Shop/...', 'https://lh5.googleusercontent.com/p/AF1QipNtGsM1520GvkgageOVs0iqEmhUDqGOB-p1HwZp=w459-h240-k-no', 'CRA 15 # 95-33, Bogotá, Colombia'),
    ('Barber Shop Ghetto', 4.628434133840879, -74.0686184891132, 'https://www.google.com/maps/place/Barber+Shop+Ghetto/...', 'https://lh5.googleusercontent.com/p/AF1QipOjaDb9TZI0ePbaMfZg5LRq9QtqKSJVYv3yZ7Qi=w408-h726-k-no', 'Av Caracas 40A31, Bogotá, Colombia'),
    ('Cavalier Barbería Clásica Calle 40', 4.628884796836012, -74.06681250260608, 'https://www.google.com/maps/place/Cavalier+Barbería+Clásica+Calle+40/...', 'https://lh5.googleusercontent.com/p/AF1QipOH4xJ_Z0cdqtsfrTlXjdAgWtjcruAaxfCOk3Hg=w426-h240-k-no', 'Carrera 13a 32 67 local 8, Bogotá, Colombia'),
    ('Bad Boys', 4.632424560200405, -74.06700148830761, 'https://www.google.com/maps/place/Bad+Boys/...', 'https://lh5.googleusercontent.com/p/AF1QipOCAuKrVZoj7hrhnJWVxkAA8x3R-4DkW1zqyWwg=w408-h272-k-no', 'Cl. 45 #13-41, Bogotá'),
    ('Barbería All Handmade', 4.632855551818548, -74.06366459096303, 'https://www.google.com/maps/place/Barbería+All+Handmade/...', 'https://lh5.googleusercontent.com/p/AF1QipO6ev6cUo8FBdadoj20KM2uUcZ8Ms9FQ22i_que=w426-h240-k-no', ' Cra. 7, Localidad de Chapinero, Bogotá'),
    ('Figaro Barber Shop', 4.630173233930651, -74.06485513577499, 'https://www.google.com/maps/place/Figaro+Barber+Shop+42/...', 'https://lh5.googleusercontent.com/p/AF1QipNp7zH-O8j915nUh0Ea3_-Ne1Y_xT6Rq6bjZYYM=w408-h503-k-no', 'Carrera 7 N° 42-69'),
]

cursor.executemany('''
    INSERT INTO barber_shops (nombre, latitud, longitud, enlace, imagen, descripcion)
    VALUES (?, ?, ?, ?, ?, ?)
''', datos_marcadores)

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

#.