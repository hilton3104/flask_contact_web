## Simple contact website using Flask + Mysql:
- View all contacts
- Add new contact
- Delete contact
- Edit contact

1. Use venv
   ```
   python -m venv venv
   source venv/bin/activate
   ```
2. Install flask and pymysql
   ```
   pip install -r requirements.txt
   ```
3. Create Database
   ```
   mysql -u root -p
   # password
   CREATE DATABASE contact_db;
   USE contact_db;
   SOURCE database_structure.sql;
   exit;
   ```
4. Change password in app.py to your mysql password

5. Run app
   ```
   python app.py
   ```
