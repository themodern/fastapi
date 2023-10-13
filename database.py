import sqlite3

# Create or connect to the SQLite database
conn = sqlite3.connect('customer_database.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Define the SQL statement to create the "customer" table
# create 
# 1. primary key
# 2. name
# 3. tel
# 4. email

create_customer_table = """
CREATE TABLE IF NOT EXISTS customer (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL, 
    tel TEXT NOT NULL,
    email TEXT NOT NULL
);
"""

# Execute the SQL statement to create the table
cursor.execute(create_customer_table)

# Commit the changes and close the database connection
conn.commit()
conn.close()
