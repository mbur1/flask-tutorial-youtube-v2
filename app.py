from flask import Flask, render_template, jsonify
from database import load_artikel_from_db, load_singleart_from_db

app = Flask(__name__)


@app.route("/")
def hello_world():
  artikel = load_artikel_from_db()
  return render_template('home.html', artikel=artikel)


@app.route("/artikel/<id>")
def show_artikel(id):
  art = load_singleart_from_db(id)
  if not art:
    return "Not found", 404
    
  return render_template('artikelpage.html', art=art)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
