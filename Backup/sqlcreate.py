import sqlite3
# Connect to the database. If it doesn't exist, it will be created in the local directory.

def get_code_for_category(category):
    # Connect to the SQLite database
    conn = sqlite3.connect('../categories.db')
    cursor = conn.cursor()

    # Prepare the SQL query to retrieve the code for the given category
    query = "SELECT code FROM category_codes WHERE category=?"

    # Execute the SQL query
    cursor.execute(query, (category,))

    # Fetch one record from the query result
    result = cursor.fetchone()

    # Close the database connection
    conn.close()

    # Return the code if a result was found, or None if not
    return result[0] if result else None

conn = sqlite3.connect('../categories.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Create table with two columns: category and code
cursor.execute('''
CREATE TABLE IF NOT EXISTS category_codes (
    category TEXT PRIMARY KEY,
    code TEXT NOT NULL
)
''')

# Insert data into the table
categories = {
    "JETSON": "JN_MO_3",
    "OAK": "OAK_MO_3",
    "YOLONAS": "YN_MO_3",
    "INFLUENCER": "INF_MO_3",
    "AGRICULTURE": "AGRI_MO_3",
    "TRADING": "AIT_MO_3",
    "Self Driving Car": "SDC_MO_3"
}

# Inserting or updating the data
for category, code in categories.items():
    cursor.execute('''
    INSERT INTO category_codes (category, code) VALUES (?, ?)
    ON CONFLICT(category) DO UPDATE SET code=excluded.code;
    ''', (category, code))

# Commit the changes to the database
conn.commit()

# Close the connection to the database
conn.close()