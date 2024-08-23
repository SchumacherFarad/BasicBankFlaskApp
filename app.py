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
    if "userinfo" in session:
        return redirect(url_for("index"))
    else:
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
    if "userinfo" in session:
        if request.method == "POST":
            ibantotransact = request.form["ibantr"]
            moneytotransact = request.form["money"]
            basicbank.transferMoney(session["userinfo"][1], ibantotransact, float(moneytotransact))
            basicbank.writePeople("./People.csv")
        return render_template("money_transfer.html")
    else:
        return redirect(url_for("login"))

@app.route('/index', methods = ["GET" , "POST"])
def index():
    if "userinfo" in session:
        if request.method == "POST":
            del session["userinfo"]
            return redirect(url_for("login"))
        else:
            basicbank.writePeople("./People.csv")
            basicbank.customers[basicbank.findiban(session["userinfo"][1])].transactions.clear()
            basicbank.customers[basicbank.findiban(session["userinfo"][1])].readTransactions()
            session["userinfo"][4] = basicbank.customers[basicbank.findiban(session["userinfo"][1])].balance
            session["userinfo"][6] = basicbank.customers[basicbank.findiban(session["userinfo"][1])].transactions
            userinforms = session["userinfo"]
            return render_template("index.html", userinfo = userinforms)
    else:
        return redirect(url_for("login"))

@app.route('/transactions')
def transactions():
    if "userinfo" in session:
        basicbank.customers[basicbank.findiban(session["userinfo"][1])].transactions.clear()
        basicbank.customers[basicbank.findiban(session["userinfo"][1])].readTransactions()
        session["userinfo"][6] = basicbank.customers[basicbank.findiban(session["userinfo"][1])].transactions
        userinforms = session["userinfo"]
        return render_template("transactions.html", userinfo = userinforms)
    else:
        return redirect(url_for("login"))

@app.route('/account', methods=["GET","POST"])
def account():
    if "userinfo" in session:
        if request.method == "POST":
            newpass = int(request.form["passw"])
            basicbank.customers[basicbank.findiban(session["userinfo"][1])].password = newpass
            session["userinfo"][5] = newpass
            session["userinfo"] = session["userinfo"]
            basicbank.writePeople("./People.csv")
            userinforms = session["userinfo"]
            return render_template("account.html", userinfo = userinforms)
        else:
            userinforms = session["userinfo"]
            return render_template("account.html", userinfo = userinforms)
    else:
        return redirect(url_for("login"))

@app.route("/signup", methods = ["GET","POST"])
def signup():
    if request.method == "POST":
        basicbank.addPerson({request.form.get("isworker") == "1"},request.form["nm"],request.form["snm"], request.form["passw"],float(request.form["balance"]), float(1000) if request.form.get("isworker")=="1" else None)
        new = basicbank.customers[basicbank.findiban(f"TR{(24-len(str(basicbank.lastiban)))*'0'}{basicbank.lastiban-1}")]
        if isinstance(new,Worker):
            userinfos = ["Worker",new.iban,new.name,new.surname,new.balance,new.password,new.transactions, new.salary]
            session["userinfo"] = userinfos
        elif isinstance(new,Customer):
            userinfos = ["Customer",new.iban,new.name,new.surname,new.balance,new.password,new.transactions]
            session["userinfo"] = userinfos
        return redirect(url_for("index"))
    else:
        return render_template("signup.html")

if __name__ == "__main__":
    app.run(host='192.168.1.22',port=5000,  debug=True)