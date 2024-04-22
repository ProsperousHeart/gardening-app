""" file with SQL setup strings """

# # create a table where plant diseases are stored, what plants are affected by them, and how to treat them
# def create_diseases_table():
#     conn = sqlite3.connect('gardening.db')
#     c = conn.cursor()
#     c.execute('''CREATE TABLE IF NOT EXISTS diseases (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         disease_name TEXT,
#         plant_type TEXT,
#         affected_plants TEXT,
#         treatment TEXT,
#         created_on DATE,
#         created_by TEXT
#     )''')
#     # conn.commit()
#     # conn.close()

import datetime

PLANT_TYPES = [
    ('flower', datetime.datetime.now(), 'ProsperousHeart'),
    ('fruit', datetime.datetime.now(), 'ProsperousHeart'),
    ('vegetable', datetime.datetime.now(), 'ProsperousHeart'),
    ('tree', datetime.datetime.now(), 'ProsperousHeart')
]

SQL_SETUP_DICT = {
    'plant_types': '''CREATE TABLE IF NOT EXISTS plant_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT UNIQUE,
    created_on DATE,
    created_by TEXT
)''',
    'plant_urls': '''CREATE TABLE IF NOT EXISTS plant_urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    plant_id INTEGER,
    url TEXT,
    description TEXT,
    url_type TEXT CHECK(url_type IN ('image', 'info')),
    created_on DATE,
    created_by TEXT,
    FOREIGN KEY(plant_id) REFERENCES plants(id)
)''',
    'plants': '''CREATE TABLE IF NOT EXISTS plants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    plant_type_id INTEGER,
    scientific_name TEXT,
    common_name TEXT,
    description TEXT,
    germination_days_start INTEGER,
    germination_days_end INTEGER,
    germination_temp_start INTEGER,
    germination_temp_end INTEGER,
    hardiness_zone_start INTEGER,
    hardiness_zone_end INTEGER,
    days_to_harvest INTEGER,
    days_to_maturation INTEGER,
    created_on DATE,
    created_by TEXT,
    FOREIGN KEY(plant_type_id) REFERENCES plant_types(id)
)'''
}
