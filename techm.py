import sqlite3
 
# Connect to SQLite and create a database
conn = sqlite3.connect("proj.db")
cursor = conn.cursor() #cursor is like pointer or object for the database
 

# Create a table named "airtel" write every query in excute method
cursor.execute('''
    CREATE TABLE IF NOT EXISTS techm (
            id INTEGER PRIMARY KEY AUTOINCREMENT ,
            Date DATETIME,
            Prev_Close DOUBLE,
            Open DOUBLE,
            High DOUBLE,
            Low DOUBLE,
            Close DOUBLE,
            VWAP DOUBLE,
            Volume INTEGER,
            Turnover DOUBLE,
            Deliverable_Volume INTEGER,
            Perc_Deliverable DOUBLE
            
    )
''')
 
 
 

import csv
 
# Read data from the CSV file
with open('TECHM.csv') as f:
    reader = csv.DictReader(f)
    data = list(reader)
 
# Insert data into the table
for row in data:
    cursor.execute("INSERT INTO techm(Date, Prev_Close, Open, High,Low,Close,VWAP,Volume,Turnover,Deliverable_Volume,Perc_Deliverable)VALUES (?, ?, ?, ?,?,?,?,?,?,?,?)",
                   ( row['Date'], row['Prev_Close'], row['Open'], row['High'],row['Low'], row['Close'], row['VWAP'], row['Volume'], row['Turnover'],
                    row['Deliverable_Volume'], row['Perc_Deliverable']))
 
# Commit the changes
conn.commit()
 
# Close the database connection
conn.close()
 

import sqlite3
 
# Connect to the database
conn = sqlite3.connect('proj.db')  
cursor = conn.cursor()
 
# Execute a SELECT query on the "airtel" table
cursor.execute('SELECT * FROM airtel')


# Fetch all rows
rows = cursor.fetchall()
 
# Display the data
for row in rows:
    print(row)
 
# Close the database connection
conn.close()

# ----------------------------------------------
