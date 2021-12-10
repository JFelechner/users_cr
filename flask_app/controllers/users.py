from flask_app import app
from flask import Flask,render_template,redirect,request
from flask_app.models.user import User


@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html", users=users)





@app.route('/create_user_page')
def create_user_page():
    return render_template('create_user.html')

@app.route('/create_user', methods=["POST"])
def create_user():

    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    user = User.save(data)
    print(user)
    return redirect(f"/show/{user}")





@app.route('/show/<int:id>')
def show_user(id):

    data={
        "id":id
    }
    users = User.get_one(data)
    print(users)
    return render_template('show.html', users=users)






@app.route('/edit/<int:id>')
def edit_user(id):

    data={
        "id":id
    }
    users = User.get_one(data)
    print(users)
    return render_template('edit.html', users=users)

@app.route('/update/user', methods=["POST"])
def update_user():

    User.update_user(request.form)
    return redirect('/')





@app.route('/delete/user', methods=["POST"])
def delete_user():

    User.delete(request.form)
    return redirect('/')
