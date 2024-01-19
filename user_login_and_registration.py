import sqlite3
from getpass import getpass

# Connect to SQLite and create a database (if not exists)
conn = sqlite3.connect('proj.db')
cursor = conn.cursor()

# Create a users table (if not exists)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
''')

# Commit the changes
conn.commit()

# Function to register a new user
def register_user():
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    try:
        # Insert the user into the users table with default role 'normal_user'
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, 'normal_user'))
        
        # Commit the changes
        conn.commit()

        print("User registration successful! Role: normal_user")
    except sqlite3.IntegrityError as e:
        # Handle unique constraint violation (username already exists)
        print(f"Error: {e}\nUser registration failed. The username '{username}' already exists.")
    except Exception as e:
        # Handle other exceptions
        print(f"Error: {e}\nUser registration failed.")

# Function to register a new admin
def register_admin():
    admin_username = input("Enter admin username: ")
    admin_password = getpass("Enter admin password: ")

    try:
        # Insert the admin into the users table with role 'iam_admin'
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (admin_username, admin_password, 'iam_admin'))
        
        # Commit the changes
        conn.commit()

        print("Admin registration successful! Role: iam_admin")
    except sqlite3.IntegrityError as e:
        # Handle unique constraint violation (username already exists)
        print(f"Error: {e}\nAdmin registration failed. The username '{admin_username}' already exists.")
    except Exception as e:
        # Handle other exceptions
        print(f"Error: {e}\nAdmin registration failed.")

# Function for admin login and CRUD operations
def admin_login():
    admin_username = input("Enter admin username: ")
    admin_password = getpass("Enter admin password: ")

    # Check if the admin exists and has the correct role
    cursor.execute("SELECT * FROM users WHERE username=? AND password=? AND role=?", (admin_username, admin_password, 'iam_admin'))
    admin = cursor.fetchone()

    if admin:
        print("Admin login successful!")

        # Perform CRUD operations
        while True:
            print("\n1. Create Record")
            print("2. Read Records")
            print("3. Update Record")
            print("4. Delete Record")
            print("5. Back")

            operation = input("Select an operation (1/2/3/4/5): ")

            if operation == '1':
                create_record()
            elif operation == '2':
                read_records()
            elif operation == '3':
                update_record()
            elif operation == '4':
                delete_record()
            elif operation == '5':
                break
            else:
                print("Invalid operation. Please enter 1, 2, 3, 4, or 5.")
    else:
        print("Invalid admin username or password.")



# Function to authenticate a normal user
def normal_user_login():
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    # Check if the user exists and has the correct role
    cursor.execute("SELECT * FROM users WHERE username=? AND password=? AND role=?", (username, password, 'normal_user'))
    user = cursor.fetchone()

    if user:
        print(f"Login successful! Role: {user[3]}")  # Assuming 'role' is the fourth column (index 3)
    else:
        print("Invalid username or password.")

# CRUD operations on tcs table
def create_record():
    # Assume you want to add a new record to data_table
    date = input("Enter Date: ")
    prev_close = float(input("Enter Prev_Close: "))
    open_value = float(input("Enter Open: "))
    high = float(input("Enter High: "))
    low = float(input("Enter Low: "))
    close = float(input("Enter Close: "))
    vwap = float(input("Enter VWAP: "))
    volume = int(input("Enter Volume: "))
    turnover = float(input("Enter Turnover: "))
    deliverable_volume = int(input("Enter Deliverable_Volume: "))
    perc_deliverable = float(input("Enter Perc_Deliverable: "))
    year_n = int(input("Enter Year_N: "))

# id,Date,      Prev_Close,Open,High,   Low, Close,  VWAP,   Volume, Turnover, Deliverable_Volume,Perc_Deliverable,Year_N
#   ,30-04-2021,3115.25,   3099,3132.05,3020,3035.65,3063.19,3072305,9.41E+14, 1942473,           0.6323,          18
    try:
        # Insert the record into data_table
        cursor.execute("INSERT INTO tcs (Date, Prev_Close, Open, High, Low, Close, VWAP, Volume, Turnover, Deliverable_Volume, Perc_Deliverable, Year_N) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (date, prev_close, open_value, high, low, close, vwap, volume, turnover, deliverable_volume, perc_deliverable, year_n))
        
        # Commit the changes
        conn.commit()

        print("Record added successfully!")
    except Exception as e:
        print(f"Error: {e}\nRecord creation failed.")

def read_records():
    # Read all records from data_table
    cursor.execute("SELECT * FROM tcs")
    records = cursor.fetchall()

    # Display records
    for record in records:
        print(record)

def update_record():
    record_id = int(input("Enter the ID of the record to update: "))
    new_prev_close = float(input("Enter the new Prev_Close: "))
    new_open = float(input("Enter the new Open: "))
    new_high = float(input("Enter the new High: "))
    new_low = float(input("Enter the new Low: "))
    new_close = float(input("Enter the new Close: "))
    new_vwap = float(input("Enter the new VWAP: "))
    new_volume = int(input("Enter the new Volume: "))
    new_turnover = float(input("Enter the new Turnover: "))
    new_deliverable_volume = int(input("Enter the new Deliverable_Volume: "))
    new_perc_deliverable = float(input("Enter the new Perc_Deliverable: "))
    new_year_n = int(input("Enter the new Year_N: "))

# id,Date,      Prev_Close,Open,High,   Low, Close,  VWAP,   Volume, Turnover, Deliverable_Volume,Perc_Deliverable,Year_N
#   ,30-04-2021,3115.25,   3099,3132.05,3020,3035.65,3063.19,3072305,9.41E+14, 1942473,           0.6323,          18

    try:
        # Update the record in data_table
        cursor.execute("UPDATE tcs SET Prev_Close=?, Open=?, High=?, Low=?, Close=?, VWAP=?, Volume=?, Turnover=?, Deliverable_Volume=?, Perc_Deliverable=?, Year_N=? WHERE id=?", 
                       (new_prev_close, new_open, new_high, new_low, new_close, new_vwap, new_volume, new_turnover, new_deliverable_volume, new_perc_deliverable, new_year_n, record_id))
        conn.commit()

        print("Record updated successfully!")
    except Exception as e:
        print(f"Error: {e}\nRecord update failed.")

def delete_record():
    record_id = int(input("Enter the ID of the record to delete: "))

    try:
        # Delete the record from data_table
        cursor.execute("DELETE FROM tcs WHERE id=?", (record_id,))
        conn.commit()

        print("Record deleted successfully!")
    except Exception as e:
        print(f"Error: {e}\nRecord deletion failed.")


# Main program
while True:
    print("\n1. Register User")
    print("2. register admin")
    print("3. Admin Login")
    print("4. Normal User Login")
    print("5. Exit")

    choice = input("Select an option (1/2/3/4/5): ")

    if choice == '1':
        register_user()
    elif choice == '2':
        register_admin()
    elif choice == '3':
        admin_login()
    elif choice == '4':
        normal_user_login()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, 5.")

# Close the cursor and connection
cursor.close()
conn.close()
