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
    return "This is a TODO list!"

if __name__ == "__main__":
    app.run(debug=True,)