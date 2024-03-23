"""Setting up a gardening app."""

# Create sqlite database for gardening
# The database on a particular plant should include the type of plant (flower, fruit, vegetable, tree)
# The database on a particular plant should include the scientific and common names of the plant
# The database on a particular plant should include the plant's description such as height, width, color, and any other relevant information
# The database on a particular plant should include the plant's germination information such as how deep to sow, how far apart to sow, space between rows, and how long it takes to germinate
# The database on a particular plant should include the plant's care information such as how much water, sunlight, and fertilizer it needs
# The database on a particular plant should include the plant's harvest information such as when to harvest, how to harvest, and how to store
# The database on a particular plant should include the plant's pests and diseases information such as what pests and diseases to look out for and how to treat them
# The database on a particular plant should include the plant's companion planting information such as what plants to plant near it and what plants to avoid planting near it
# The database on a particular plant should include the plant's hardiness information such as what zones it grows in and what temperatures it can tolerate
# The database on a particular plant should include the plant's propagation information such as how to propagate it from seed, cuttings, or division
# The database on a particular plant should include the plant's uses such as culinary, medicinal, or ornamental
# The database on a particular plant should include links to reputable sources for more information on the plant
# The database on a particular plant should include a photo of the plant, but provide for multiple photo options
# When adding new items, it should include a timestamp of when the item was added or updated
# The database should be searchable by plant name or type
# The database should be able to display all information on a particular plant
# The database should be able to display all plants of a particular type

import sqlite3
import pandas as pd
import os
import datetime

from sql_setup import SQL_SETUP_DICT, PLANT_TYPES

DB_PATH = 'gardening.db'

def create_table_from_str(conn, table_str):
    """
    Create a table in the database using the provided SQL string.

    Args:
        conn: The SQLite database connection object.
        table_str: The SQL string to create the table.

    Returns:
        None
    """
    try:
        c = conn.cursor()
        c.execute(table_str)
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

def insert_into_plants_table(conn, plant_data):
    """
    Insert plant data into the plants table.

    Args:
        conn: The SQLite database connection object.
        plant_data: A tuple containing the plant data.

    Returns:
        None
    """
    # check if the plant scientific name already exists in the database
    c = conn.cursor()
    c.execute("SELECT scientific_name FROM plants WHERE scientific_name=?", (plant_data[1],))
    existing_plant = c.fetchone()
    if existing_plant:
        print(f"Plant with scientific name '{plant_data[1]}' already exists in the database.")
    else:
        c = conn.cursor()
        c.execute('''INSERT INTO plants (
                  plant_type_id, 
                  scientific_name, 
                  common_name, 
                  description, 
                  germination_days_start, 
                  germination_days_end, 
                  germination_temp_start, 
                  germination_temp_end, 
                  hardiness_zone_start, 
                  hardiness_zone_end, 
                  days_to_harvest, 
                  days_to_maturation, 
                  created_on, 
                  created_by
                  ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                  plant_data
                )
        conn.commit()

# Function to show all tables in the database
def get_table_names(conn):
    """
    Show all tables in the database.

    Args:
        conn: The SQLite database connection object.

    Returns:
        None
    """
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    table_names = [table[0] for table in tables]
    return table_names

# Create a database
def create_database(path_to_db: str):
    """
    Creates a new SQLite database named 'gardening.db',
    connects to the SQLite database, creates the 
    required tables for the gardening app, and commits
    the changes before closing the connection.
    """
    conn = sqlite3.connect(path_to_db)

    # Check if expected tables are already created and make them if not
    table_names = get_table_names(conn)
    if table_names == []:
        if 'plant_types' not in table_names:
            create_table_from_str(conn, SQL_SETUP_DICT['plant_types'])
            conn.executemany('INSERT INTO plant_types (type, created_on, created_by) VALUES (?, ?, ?)', PLANT_TYPES)
        if 'plant_urls' not in table_names:
            create_table_from_str(conn, SQL_SETUP_DICT['plant_urls'])
        if 'plants' not in table_names:
            create_table_from_str(conn, SQL_SETUP_DICT['plants'])
    
        conn.commit()
        print("Database created successfully.")
    # conn.close()
    return conn

# Function that shows all data in tables using pandas
def show_table_data(conn):
    """
    Show all data in the tables in the database using pandas.

    Args:
        conn: The SQLite database connection object.

    Returns:
        None
    """
    table_names = get_table_names(conn)
    for table_name in table_names:
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        print(f"Table: {table_name}")
        print(df)
        print("\n")

def main(path_to_db: str):
    conn = create_database(path_to_db)
    # print(get_table_names(conn))
    insert_into_plants_table(conn, (1, 'Rosa chinensis', 'China Rose', 'A beautiful rose with red petals.', 7, 14, 70, 75, 5, 9, 60, 90, datetime.datetime.now(), 'ProsperousHeart'))
    show_table_data(conn)
    conn.close()

if __name__ == "__main__":
    main(DB_PATH)