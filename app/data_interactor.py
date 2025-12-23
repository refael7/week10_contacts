import os
import psycopg2
class Contact:
    def __init__(self, id, first_name, last_name, phone_number):
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

def get_connection():
    conn = psycopg2.connect(
    db_password = os.getenv("DB_PASSWORD"),
    db_host = os.getenv("DB_HOST"),
    db_port = os.getenv("DB_PORT"),
    db_user = os.getenv("DB_USER"),
    db_name = os.getenv("DB_NAME"))
    return conn





