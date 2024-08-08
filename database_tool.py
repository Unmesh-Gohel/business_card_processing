from crewai_tools import tool
import sqlite3

@tool
def insert_into_database(data: dict) -> str:
    """
    Tool to insert data into the database.
    :param data: Dictionary containing the parsed data.
    :return: Success message or error.
    """
    try:
        conn = sqlite3.connect('business_cards.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS cards
                          (name TEXT, title TEXT, company TEXT, phone TEXT, email TEXT)''')
        cursor.execute('''INSERT INTO cards (name, title, company, phone, email)
                          VALUES (?, ?, ?, ?, ?)''', 
                          (data['name'], data['title'], data['company'], data['phone'], data['email']))
        conn.commit()
        conn.close()
        return "Data inserted successfully"
    except Exception as e:
        return str(e)
