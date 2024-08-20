from bank import Bank
from customer import Customer
from worker import Worker
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')
basicbank = Bank()
basicbank.readPeople("BasicBankPythonApp/People.csv")
basicbank.writePeople("BasicBankPythonApp/People.csv")