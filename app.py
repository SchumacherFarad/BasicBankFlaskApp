from bank import Bank
from customer import Customer
from worker import Worker
from flask import Flask, render_template, request, url_for, redirect, session
basicbank = Bank()
basicbank.readPeople("./People.csv")

app = Flask(__name__)
app.secret_key ="748943448fe3fd665c0b97d37b6b0c7b15cc41ea7d8d6107186ed9f6568961e1"
@app.route('/', methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        useriban = request.form["iban"]
        userpass = request.form["passw"]
        for i in basicbank.customers:
            if useriban == i.iban:
                if userpass == i.password:
                    i.readTransactions()
                    if isinstance(i,Worker):
                        userinfos = ["Worker",i.iban,i.name,i.surname,i.balance,i.password,i.transactions,i.salary]
                        session["userinfo"] = userinfos
                    elif isinstance(i,Customer):
                        userinfos = ["Customer",i.iban,i.name,i.surname,i.balance,i.password,i.transactions]
                        session["userinfo"] = userinfos
                    return redirect(url_for("index"))
        return render_template("login.html")
    else:
        return render_template("login.html")

@app.route('/money_transfer', methods = ['GET', 'POST'])
def money_transfer():
    if request.method == "POST":
        ibantotransact = request.form["ibantr"]
        moneytotransact = request.form["money"]
        basicbank.transferMoney(session["userinfo"][1], ibantotransact, float(moneytotransact))
        basicbank.writePeople("./People.csv")
    return render_template("money_transfer.html")

@app.route('/index')
def index():
    if "userinfo" in session:
        basicbank.customers[basicbank.findiban(session["userinfo"][1])].transactions.clear()
        basicbank.customers[basicbank.findiban(session["userinfo"][1])].readTransactions()
        session["userinfo"][4] = basicbank.customers[basicbank.findiban(session["userinfo"][1])].balance
        session["userinfo"][6] = basicbank.customers[basicbank.findiban(session["userinfo"][1])].transactions
        userinforms = session["userinfo"]
        return render_template("index.html", userinfo = userinforms)
    else:
        return redirect(url_for("/"))

@app.route('/transactions')
def transactions():
    if "userinfo" in session:
        basicbank.customers[basicbank.findiban(session["userinfo"][1])].transactions.clear()
        basicbank.customers[basicbank.findiban(session["userinfo"][1])].readTransactions()
        session["userinfo"][6] = basicbank.customers[basicbank.findiban(session["userinfo"][1])].transactions
        userinforms = session["userinfo"]
        return render_template("transactions.html", userinfo = userinforms)
    else:
        return redirect(url_for("/"))

@app.route('/account')
def account():
    if "userinfo" in session:
        userinforms = session["userinfo"]
        return render_template("account.html", userinfo = userinforms)
    else:
        return redirect(url_for("/"))

if __name__ == "__main__":
    app.run(debug=True)