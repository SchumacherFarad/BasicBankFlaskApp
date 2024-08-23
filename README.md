
# BasicBank Flask App

A bank simulation that stores user data in a CSV file, uses Python classes, and interacts with a web app integrated with Flask.


## Related Project

[BasicBank](https://github.com/SchumacherFarad/BasicBank)

  
## Features

- Money Transfer

- Display last transactions

- Creating new accounts

- Profile page with password change

  
## Roadmap

- Deposit, Withdraw

  
## Run the app on your computer

Clone the repository

```bash
  git clone https://github.com/SchumacherFarad/BasicBankFlaskApp
```

Navigate to the project directory

```bash
  cd BasicBankFlaskApp
```

Install necessary packages

```bash
  pip install -r requirements.txt
```

You should edit the host parameter in the 81st row of app.py with your local ip or you can delete it with the port parameter 
```python
    app.run(host='<your local ip>',port=5000,  debug=True)
```
OR
```python
    app.run(debug=True)
```


Run the app

```bash
  python app.py
```

If you chose deleting the parameters, go to http://127.0.0.1:5000/ in your browser.

If you chose editing the host parameter with your local ip, go to http://(your local ip):5000/
  
## Ekran Görüntüleri

![Login Page](https://github.com/SchumacherFarad/SchumacherFarad/blob/main/RepoImages/BasicBankFlaskAppLogin.png?raw=true)

![Login Page](https://github.com/SchumacherFarad/SchumacherFarad/blob/main/RepoImages/BasicBankFlaskAppHome.png?raw=true)

![Login Page](https://github.com/SchumacherFarad/SchumacherFarad/blob/main/RepoImages/BasicBankFlaskAppMoneyTransfer.png?raw=true)

![Login Page](https://github.com/SchumacherFarad/SchumacherFarad/blob/main/RepoImages/BasicBankFlaskAppTransactions.png?raw=true)


  
## Feedback

If you have any feedback, please contact me at ferhatkunduraci03@gmail.com.

  
## Thanks to

- [Ali Emre Kaya](https://github.com/aliemre2023) for reporting bugs and suggesting solutions

  
