# week10_contacts

Contact Manager API – Week 10

  

 
GET    /contacts        – קבלת כל אנשי הקשר
POST   /contacts        – יצירת איש קשר חדש
PUT    /contacts/{id}   – IDעדכון איש קשר לפי 
DELETE /contacts/{id}   – IDמחיקת איש קשר לפי 

 

 
Contact:
id (int)
first_name (string)
last_name (string)
phone_number (string, unique)




מהתיקייה הראשית של הפרויקט:

docker compose up -d --build

curl http://localhost:8000/contacts


 
db  – MySQL database  
api – FastAPI application (port 8000)



 