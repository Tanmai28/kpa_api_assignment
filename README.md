<<<<<<< HEAD
# KPA API Assignment – [Your Name]
---

## Project Overview

This project implements two backend APIs as per the KPA assignment requirements:
- **POST /login**: User authentication using phone number and password.
- **GET /formdata**: Fetches all form data entries from the database.

The project uses FastAPI for the backend, PostgreSQL for the database, and SQLAlchemy as the ORM.  
All endpoints are fully documented and tested using Postman.

---

## Tech Stack

- **Backend Framework:** FastAPI (Python)
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Validation:** Pydantic
- **Environment Management:** python-dotenv
- **API Testing:** Postman

---

## Project Structure

```
kpa_api_assignment/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── crud.py
│   └── routes/
│        ├── __init__.py
│        ├── auth.py
│        └── formdata.py
├── .env
├── requirements.txt
├── README.md
└── yourname_postman_collection.json
```

---

## Setup Instructions

1. **Clone or unzip the project folder.**
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Database Setup

1. **Install PostgreSQL** if not already installed.
2. **Create a database and user:**
   - Open pgAdmin or psql and run:
     ```sql
     CREATE DATABASE kpa_db;
     CREATE USER kpa_user WITH PASSWORD 'yourpassword';
     GRANT ALL PRIVILEGES ON DATABASE kpa_db TO kpa_user;
     GRANT ALL PRIVILEGES ON SCHEMA public TO kpa_user;
     ```
3. **(Optional) Insert test data:**
   - Insert a user for login:
     ```sql
     INSERT INTO users (phone, password) VALUES ('7760873976', 'to_share@123');
     ```
   - Insert form data:
     ```sql
     INSERT INTO formdata (name, value) VALUES
     ('First Field', 'First Value'),
     ('Second Field', 'Second Value');
     ```

---

## Environment Variables

Create a `.env` file in the project root with:
```
DATABASE_URL=postgresql://kpa_user:yourpassword@localhost:5432/kpa_db
SECRET_KEY=your_secret_key
```
- Replace `yourpassword` and `your_secret_key` with your actual values.

---

## How to Run the Project

1. **Start the FastAPI server:**
   ```bash
   uvicorn app.main:app --reload
   ```
2. **Open the API docs:**  
   [http://localhost:8000/docs](http://localhost:8000/docs)

---

## API Documentation

### **POST /login**
- **Description:** Authenticates a user by phone and password.
- **Request Body:**
  ```json
  {
    "phone": "7760873976",
    "password": "to_share@123"
  }
  ```
- **Response:**
  - `200 OK`:
    ```json
    {
      "message": "Login successful"
    }
    ```
  - `401 Unauthorized`:
    ```json
    {
      "detail": "Invalid credentials"
    }
    ```

### **GET /formdata**
- **Description:** Returns all form data entries.
- **Response:**
  - `200 OK`:
    ```json
    [
      {
        "id": 1,
        "name": "First Field",
        "value": "First Value"
      },
      ...
    ]
    ```

---

## Testing with Postman

1. **Import the provided Postman collection (`yourname_postman_collection.json`).**
2. **Update the `baseUrl` variable to `http://localhost:8000` if needed.**
3. **Test `/login` and `/formdata` endpoints.**
 http://localhost:8000/login    - POST
 http://localhost:8000/formdata - GET

4. **Save and export the collection for submission.**

---

## Features Implemented

- User authentication with phone and password.
- Fetching all form data from the database.
- Input validation using Pydantic.
- Environment-based configuration using `.env`.
- API documentation via FastAPI’s Swagger UI.
- Postman collection for easy testing.

---

## Assumptions & Limitations

- Passwords are stored in plain text (for demo only).
- No JWT or session management implemented.
- No advanced error handling or input sanitization.
- Only two endpoints implemented as per assignment.

---

## How to Contribute / Contact

For any questions or suggestions, please contact:  
**[Your Name]**  
**Email:** [your.email@example.com]

---

**Video walkthrough and Postman collection links are included in the submission email.**

---

**Feel free to copy, edit, and personalize this documentation for your project!  
If you want me to review your final README or have any other questions, just let me know!**
SCRIPT FOR VIDEO AND README FILE

Absolutely! Here’s everything you need for a **complete, professional submission**:

---

## 1. **README Template**

Copy and fill in your details:

```markdown
# KPA API Assignment

## Setup Instructions

1. **Clone or unzip the project folder.**
2. **Create and activate a virtual environment:**
   - `python -m venv venv`
   - On Windows: `venv\Scripts\activate`
   - On Mac/Linux: `source venv/bin/activate`
3. **Install dependencies:**
   - `pip install -r requirements.txt`
4. **Set up PostgreSQL:**
   - Create a database named `kpa_db`
   - Create a user `kpa_user` with a password and grant all privileges on `kpa_db`
5. **Create a `.env` file in the project root:**
   ```
   DATABASE_URL=postgresql://kpa_user:yourpassword@localhost:5432/kpa_db
   SECRET_KEY=your_secret_key
   ```
6. **Run the app:**
   - `uvicorn app.main:app --reload`
7. **Access the API docs:**  
   [http://localhost:8000/docs](http://localhost:8000/docs)

## Tech Stack

- Python 3.x
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic

## Implemented APIs

- **POST /login**: User authentication (returns success message if credentials are correct)
- **GET /formdata**: Returns all form data entries from the database

## Limitations / Assumptions

- Passwords are stored in plain text (for demo purposes only)
- No JWT or session management implemented
- No advanced validation or error handling beyond basic checks

=======
# kpa_api_assignment
Backend assignment: FastAPI implementation of two APIs from the KPA_form data collection.
>>>>>>> 63d412e45e9a7b45db4a408f41ef1099d5c9080f
