import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv()
class Contact:
    def __init__(self, id:int, first_name:str, last_name:str, phone_number:str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def convert_contact_to_dictionary(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number
        }

    def __repr__(self):
        return (
            f"(id={self.id}, "
            f"first_name={self.first_name}, "
            f"last_name={self.last_name}, "
            f"phone_number={self.phone_number})"

        )
def get_connection():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        return conn
    except Exception as e :
        print(f"Error connecting to database:{e}")
        return None

def create_contact(first_name, last_name, phone_number) -> int:
    conn=get_connection()
    if conn is None:
        return None
    cursor = conn.cursor()
    query = "INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s,%s,%s)"
    cursor.execute(query,(first_name, last_name, phone_number))
    conn.commit()
    contact_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return contact_id

def get_all_contacts() -> list:
    conn = get_connection()
    if conn is None:
        return []
    cursor = conn.cursor()
    query = "SELECT id, first_name, last_name, phone_number FROM contacts"
    cursor.execute(query)
    rows = cursor.fetchall()
    contacts = []

    for row in rows:
        contact = Contact(
            id=row[0],
            first_name=row[1],
            last_name=row[2],
            phone_number=row[3]
        )
        contacts.append(contact)
    cursor.close()
    conn.close()
    return contacts

def update_contact(contact_id:int, first_name:str, last_name:str, phone_number:str) -> bool:
    conn = get_connection()
    if conn is None:
        return False
    cursor = conn.cursor()
    query = "UPDATE contacts SET first_name=%s, last_name=%s, phone_number=%s WHERE id=%s"
    cursor.execute(query,(first_name, last_name, phone_number, contact_id))
    conn.commit()
    rows_affected = cursor.rowcount
    cursor.close()
    conn.close()
    return rows_affected > 0

def delete_contact(id) -> bool:
    conn = get_connection()
    if conn is None:
        return False
    cursor = conn.cursor()
    query = "DELETE FROM contacts WHERE id=%s"
    cursor.execute(query,(id,))
    conn.commit()
    rows_affected = cursor.rowcount
    cursor.close()
    conn.close()
    return rows_affected > 0















