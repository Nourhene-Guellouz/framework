import psycopg2
import json
import sys

args = sys.argv
full_path = "C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Test_Framework\\Front_Test_Framework_NG\\db\\results.json"

try:
    connection = psycopg2.connect(
        dbname="db",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )
    print("Connected to the database")
except psycopg2.Error as e:
    print("Unable to connect to the database:", e)

cursor = connection.cursor()

try:
    if(args[1]=='0'):
        var="results"
    elif(args[1]=='1'):
        var="results2"

    # Create the table if it doesn't exist
    create_table_query = f'''
    CREATE TABLE IF NOT EXISTS {var} (
        id SERIAL PRIMARY KEY,
        test VARCHAR(100) UNIQUE,
        status INTEGER
    );
    '''
    cursor.execute(create_table_query)
    print("Table created successfully")
    
    # Empty the table before inserting new data
    empty_table_query = f'''TRUNCATE TABLE {var};'''
    cursor.execute(empty_table_query)
    print("Table emptied successfully")
    
    # Insert data into the table
    insert_query = f'''
    INSERT INTO {var} (test, status) VALUES (%s, %s);
    '''
    with open(full_path, "r") as file:
        data = json.load(file)
        for test, status in data.items():
            cursor.execute(insert_query, (test, status))
   
    print("Data added successfully")

    # Commit the transaction
    connection.commit()

except psycopg2.Error as e:
    # Rollback the transaction if an error occurs
    print("Error:", e)
    connection.rollback()

finally:
    cursor.close()
    connection.close()
