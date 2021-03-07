from flask import Flask
from flask import render_template, request, url_for, redirect, g, session, flash
import sqlite3
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


def genID(length):
    id = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(length)])
    return id


@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")


@app.route("/create_profile", methods=["POST", "GET"])
def create_profile():
    if request.method == "POST":
        session['fullname'] = request.form['fullname']
        session['address1'] = request.form['address1']
        session['address2'] = request.form['address2']
        session['state'] = request.form['state']
        session['zipcode'] = request.form['zipcode']
        print(session)

        return render_template("quotes.html", fullname = session["fullname"], address1 = session["address1"], address2 = session["address2"], state = session["state"], zipcode = session["zipcode"])
    else:
        return render_template("create_profile.html")


@app.route("/quotes", methods=["POST", "GET"])
def quotes():
    if request.method == "POST":
        session['gallons_requested'] = request.form['gallons_requested']
        session['delivery_address'] = request.form['delivery_address']
        session['delivery_date'] = request.form['delivery_date']  

        return render_template("checkout.html", gallons_requested = session['gallons_requested'], delivery_address = session['delivery_address'])
    else:
        return render_template("index.html")


@app.route("/checkout", methods=["POST", "GET"])
def checkout():

    return render_template("checkout.html")
    # if request.method == "POST":
    #     session['gallons_requested'] = request.form['gallons_requested']
    #     session['delivery_address'] = request.form['delivery_address']
    #     session['delivery_date'] = request.form['delivery_date']  

    #     print(session)
    #     return redirect(url_for("checkout"))


    # else:
    #     return render_template("checkout.html")



if __name__ == "__main__":
    app.run(debug=True)