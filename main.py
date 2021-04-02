from flask import Flask
from flask import render_template, request, url_for, redirect, g, session, flash
import sqlite3
from flask_sqlalchemy import SQLAlchemy
import pytest
import random, string
from decimal import Decimal

# def fileReader():
#     pdfName = "old/file.pdf"

#     pdfRead = PyPDF2.PdfFileReader(pdfName)

#     for i in range(pdfRead.getNumPages()):
#         page = pdfRead.getPage(i)
#         print("Page No: " + str(1 + pdfRead.getPageNumber(page)))
#         pageContent = page.extractText()
#         print(pageContent)



app = Flask(__name__)
app.secret_key = "123"


def genUniqueID(length):
    id = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(length)])
    return id

def genON(length):
    id = ''.join([random.choice(string.digits) for n in range(length)])
    return id

def create_connection():
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('database.db')
    return db

@app.route("/", methods=["POST", "GET"])
def index():
    
    if request.method == "POST":

        if not session['register-email']:
            session['login-email'] = request.form['login-email']
            session['login-password'] = request.form['login-password']
        elif not session['login-email']:
            session['register-email'] = request.form['register-email']
            session['register-password'] = request.form['register-password']
            session['register-password2'] = request.form['register-password2']
        
        # print(session)
        # return render_template("quotes.html", fullname = session['fullname'], address1 = session['address1'], address2 = session['address2'], state = session['state'], zipcode = session['zipcode'])
        return redirect(url_for("create_profile"))
    else:
        return render_template("index.html")


@app.route("/create_profile", methods=["POST", "GET"])
def create_profile():
    if request.method == "POST":
        session['fullname'] = request.form['fullname']
        session['address1'] = request.form['address1']
        session['address2'] = request.form['address2']
        session['state'] = request.form['state']
        session['zipcode'] = request.form['zipcode']
        # print(session)
        unique_id = genUniqueID(8)
        session['unique_id'] = unique_id
        

        conn = create_connection()
        cursor = conn.cursor()

        command = f"INSERT INTO Profile VALUES('{unique_id}', '{session['fullname']}', '{session['address1']}', '{session['address2']}', '{session['state']}', {session['zipcode']})"
        cursor.execute(command)

        # command = f"SELECT * FROM profile;"
        # cursor.execute(command)

        # print("Profile during profile ", cursor.fetchall())
        conn.commit()
        cursor.close()
        return redirect(url_for("quotes"))
    else:
        return render_template("create_profile.html")


@app.route("/quotes", methods=["POST", "GET"])
def quotes():
    conn = create_connection()
    cursor = conn.cursor()
    command = f"SELECT address1, address2 FROM Profile WHERE unique_id LIKE '%{session['unique_id']}%';"

    cursor.execute(command)
    temp = cursor.fetchall()

    address = temp[0][0] + " " + temp[0][1]
    print(address)

    if request.method == "POST":
        session['gallons_requested'] = request.form['gallons_requested']
        session['delivery_address'] = request.form['delivery_address']
        session['delivery_date'] = request.form['delivery_date']
        
        
        
        return redirect(url_for("checkout"))
    else:
        return render_template("quotes.html", fullname = session['fullname'], address = address, state = session['state'], zipcode = session['zipcode'])


@app.route("/checkout", methods=["POST", "GET"])
def checkout():
    if request.method == "POST":
        conn = create_connection()
        cursor = conn.cursor()

        order_no = int(genON(8))
        price = 0

        command = f"INSERT INTO History VALUES( {order_no}, DATE('now', 'localtime'), '{session['delivery_address']}', '{session['delivery_date']}', {session['gallons_requested']}, {price}, '{session['unique_id']}' )"
        # command = f"INSERT INTO history VALUES( 123, '10/10/2000', '7005 BELLING tx', '10/12/2000', 10, 1000, '{session['unique_id']}')"
        cursor.execute(command)

        conn.commit()
        cursor.close()
        return redirect(url_for("quotes"))
    else:
        return render_template("checkout.html", gallons_requested = session['gallons_requested'], delivery_address = session['delivery_address'], delivery_date = session['delivery_date'])

@app.route("/history", methods=["POST", "GET"])
def history():
    conn = create_connection()
    cursor = conn.cursor()

    command = f"SELECT * FROM history WHERE unique_id LIKE '%{session['unique_id']}%'"
    cursor.execute(command)

    history_list = cursor.fetchall()
    # print(history_list)

    cursor.close()
    return render_template("history.html", history_list = history_list)

@app.route("/faq", methods=["POST", "GET"])
def faq():
    return render_template("faq.html")


if __name__ == "__main__":
    app.run(debug=True)