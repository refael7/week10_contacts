from fastapi import FastAPI, HTTPException
import mysql.connector
from pydantic import BaseModel

from data_interactor import get_all_contacts, create_contact, Contact, update_contact, delete_contact

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

@app.put("/contacts/{id}")
def update_existing_contact(contact_id: int, contact: ContactCreate):
    if (
        contact.first_name is None and
        contact.last_name is None and
        contact.phone_number is None
    ):
        raise HTTPException(
            status_code=400,
            detail="At least one field must be provided for update"
        )

    try:
        updated = update_contact(
            contact_id=contact_id,
            first_name=contact.first_name,
            last_name=contact.last_name,
            phone_number=contact.phone_number
        )


        if not updated:
            raise HTTPException(
                status_code=404,
                detail="Contact not found"
            )

        return {
            "message": "Contact updated successfully"
        }

    except mysql.connector.IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Phone number already exists"
        )

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Database error while updating contact"
        )

@app.delete("/contacts/{id}")
def delete_contact_endpoint(id: int):
    try:
        deleted = delete_contact(id)

        if not deleted:
            raise HTTPException(
                status_code=404,
                detail="Contact not found"
            )

        return {
            "message": "Contact deleted successfully"
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Database error while deleting contact"
        )



