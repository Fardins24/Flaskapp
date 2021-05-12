from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@34.105.225.78:3306/flask_external"

db = SQLAlchemy(app)

class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(50), nullable=False)
    complete = db.Column(db.Boolean, default=False)

@app.route('/')
def index():
    all_todos = Todos.query.all()
    todos_string = ""
    for todo in all_todos:
        todos_string += "<br>" + str(todo_id) + todo.task + str(todo.complete)
    return todos_string 

@app.route("/add")
def add():
    new_todo = Todos(task="New Todo")
    db.session.add(new_todo)
    db.session.commit()
    return new_todo.task

@app.route("/complete/<int:todo_id>")
def complete(todo_id):
    todo = Todos.query.get(todo_id)
    todo.complete = True
    db.session.commit()
    return "completed Todo"

@app.route("/incomplete/<int:todo_id>")
def incomplete(todo_id):
    todo = Todos.query.get(todo_id)
    todo.complete = False
    db.session.commit()
    return "Incompleted Todo"





if __name__ == "__main__":
    app.run(debug=True,)