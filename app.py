from cs50 import SQL
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

db = SQL("sqlite:///todo.db")

@app.route("/")
def index():
    rows = db.execute("SELECT * FROM todos")
    return render_template("index.html", rows=rows)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        task = request.form.get("task")
        db.execute("INSERT INTO todos (task) VALUES (:task)", task=task)
        return redirect("/")

if __name__ == '__main__':
    app.run()