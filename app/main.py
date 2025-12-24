from fastapi import FastAPI, HTTPException
import mysql.connector
from pydantic import BaseModel

from data_interactor import get_all_contacts, create_contact, Contact

app = FastAPI()

class ContactCreate(BaseModel):
    first_name: str
    last_name: str
    phone_number: str



@app.get("/contacts")
def read_contacts():
    try:
        contacts = get_all_contacts()
        result = []

        for contact in contacts:
            contact_dict = contact.convert_contact_to_dictionary()
            result.append(contact_dict)

        return result

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="database error"
        )


@app.post("/contacts")
def create_new_contact(contact: ContactCreate):
    try:
        contact_id = create_contact(
            contact.first_name,
            contact.last_name,
            contact.phone_number
        )
        return {
            "message": "Contact created successfully",
            "id": contact_id
        }

    except mysql.connector.IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Phone number already exists"
        )

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Database error while creating contact"
        )



