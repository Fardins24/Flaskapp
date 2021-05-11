from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@34.105.225.78:3306/flask_external"

db = SQLAlchemy(app)



if __name__ == "__main__":
    app.run(debug=True)

''' need to finish the many to many relationship'''