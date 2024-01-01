from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'salary': '$100k-$200k',
        'location': 'USA'
    },
    {
        'id': 2,
        'title': 'Engineer',
        'salary': '$100k-$300k',
        'location': 'Deutschland'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'salary': '$200k',
        'location': 'India'
    },
    {
        'id': 4,
        'title': 'Janitor',
        'salary': '$100k',
        'location': 'London'
    },
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
