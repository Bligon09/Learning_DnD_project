
from flask import (Flask, render_template, request, flash, session,
                   redirect)
from dndmodel import connect_to_db, db
import dndcrud

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

@app.route('/csheet')
def show_sheet():
    #TODO: get user_id from a get or post request
    user=dndcrud.get_user_info(1)
    namefield=dndcrud.get_Cnamefield_info(1)
    #TODO: get user_id from a get or post request

    return render_template('csheet.html', user=user, namefield=namefield )

@app.route('/user', methods =['POST'] )
def register_user():
    user_name = request.form.get('user_name')
    email = request.form.get('email')
    password = request.form.get('password')
    new_user = dndcrud.create_user(user_name, email, password)
    db.session.add(new_user)
    db.session.commit()

    print(new_user)

    # check_email = dndcrud.get_user_by_email(email)

    # print(check_email)
    # if check_email is not None:
    #     flash("You can't use that email")

    # else:
    #     new_user = dndcrud.create_user(email, user_name, password)
    #     flash("Your account has been created")
        # db.session.add(new_user)
        # db.session.commit()


    return redirect('/menu')



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
