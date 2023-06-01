
from flask import (Flask, render_template, request, flash, session,
                   redirect)
# from model import connect_to_db, db
# import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
   
    return render_template('homepage.html')


@app.route('/menu')
def menu():


    return render_template('menu.html')

@app.route('/new-to-roleplaying')
def newroleplayer():


    return render_template('new-to-roleplaying.html')

@app.route('/history')
def history():


    return render_template('history.html')



if __name__ == "__main__":
    # connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
