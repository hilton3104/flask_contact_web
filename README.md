# Contact Management System
A simple full-stack web application for managing personal contacts with **CRUD** (Create, Read, Update, Delete) operations and real-time search functionality.

## Features
- **View all contacts** – Display contacts
- **Add new contact** – Name and phone number
- **Edit existing contact** – Update name or phone number
- **Delete contact** – With confirmation dialog
- **Search contacts** – Real-time search by name or phone number

## Run the app

### 1. Prerequisites
- Python 3.8+
- MySQL Server (running locally)

### 2. Clone the repository
```bash
git clone https://github.com/hilton3104/flask_contact_web.git
cd flask_contact_web
```

### 3. Create and activate virtual environment
```bash
python -m vene venv
source venv/bin/activate    # macOS/Linux
# or
venv\Scripts\activate   # Windows
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Set up the database
```bash
# Login to MySQL
mysql -u root -p

# Create database and tables
CREATE DATABASE contact_db;
USE contact_db;
SOURCE database_structure.sql;
exit;
```

### 6. Configure database password
Edit `app.py` and change the `password` field in `get_db()` function:
```python
def get_db():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='password',  # <- change this
        database='contact_db',
        ...
    )
```

### 7. Run the application
```bash
python app.py
```

### 8. Open in browser
Visit http://127.0.0.1:5000/contact

### 9. Stop the server and deactivate virtual environment
- To stop the Flask development server, press `Ctrl + C` in the terminal.
- To deactivate the virtual environment, simply run:
```bash
deactivate
```


### Notes
- This project is for **educational purposes only**.
- MySQL must be installed and running locally before starting the app.
- The database schema is defined in `database_structure.sql`.