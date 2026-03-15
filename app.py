from flask import Flask, request, render_template, redirect, url_for
import pymysql
import pymysql.cursors

app = Flask(__name__)

def get_db():
    return pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = ' PASSWORD',
        database = 'contact_db',
        charset = 'utf8mb4',
        cursorclass = pymysql.cursors.DictCursor
    )


@app.route('/add')
def show_add_form():
    return render_template('add_contact.html')

@app.route('/add_contact', methods=['GET', 'POST'])
def add_contact():
    name = request.form['name']
    phone = request.form['phone']

    conn = get_db()
    try:
        with conn.cursor() as cursor:
            sql = """
                insert into contacts (name, phone) values (%s, %s)
            """
            cursor.execute(sql, (name, phone))
            conn.commit()
    finally:
        conn.close()
    return redirect(url_for('list_contact'))

@app.route('/contact')
def list_contact():
    conn = get_db()
    try:
        with conn.cursor() as cursor:
            cursor.execute("select * from contacts order by name")
            contacts = cursor.fetchall()
    finally:
        conn.close()
    return render_template('contacts_list.html', contacts = contacts)

@app.route('/edit/<int:contact_id>')
def show_edit_form(contact_id):
    conn = get_db()
    try:
        with conn.cursor() as cursor:
            cursor.execute("select * from contacts where id=%s", (contact_id,))
            contact = cursor.fetchone()
    finally:
        conn.close()
    return render_template('edit_contact.html', contact = contact)

@app.route('/edit_contact/<int:contact_id>', methods=['POST'])
def edit_contact(contact_id):
    name = request.form['name']
    phone = request.form['phone']
    conn = get_db()
    try:
        with conn.cursor() as cursor:
            cursor.execute("update contacts set name = %s, phone = %s where id=%s", (name, phone, contact_id))
            conn.commit()
    finally:
        conn.close()
    return redirect(url_for('list_contact'))

@app.route('/delete/<int:contact_id>')
def delete_contact(contact_id):
    conn = get_db()
    try:
        with conn.cursor() as cursor:
            cursor.execute("delete from contacts where id=%s", (contact_id,))
            conn.commit()
    finally:
        conn.close()
    return redirect(url_for('list_contact'))
            

if __name__ == '__main__':
    app.run(debug=True)