from flask import Flask, render_template

app = Flask(__name__)

ARTIKEL = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'continent': '$100k-$200k',
        'threatlevel': 'USA',
        'artikeltext': 'USA'
    },
    {
        'id': 2,
      'title': 'Data Analyst',
      'continent': '$100k-$200k',
      'threatlevel': 'USA',
      'artikeltext': 'USA'
    },
    {
        'id': 3,
      'title': 'Data Analyst',
      'continent': '$100k-$200k',
      'threatlevel': 'USA',
      'artikeltext': 'USA'
    },
    {
        'id': 4,
      'title': 'Data Analyst',
      'continent': '$100k-$200k',
      'threatlevel': 'USA',
      'artikeltext': 'USA'
    },
]



@app.route("/")
def hello_world():
  return render_template('home.html', artikel=ARTIKEL)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
