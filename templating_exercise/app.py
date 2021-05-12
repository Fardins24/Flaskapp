from flask import Flask, render_template

app = Flask(__name__)

@app.route('/list')
def _list():
    list_1 = ["ben", "harry", "bob", "jay", "matt", "bill"]
    return render_template('list.html', user=list_1)

if __name__ == "__main__":
    app.run(debug=True)

