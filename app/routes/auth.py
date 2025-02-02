from flask import Flask, session, abort, url_for, redirect


app = Flask("Google login")
app.secret_key = "clajuropajuema"

def  login_is_requiered(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401) # Unauthorized
        else:
            return function(*args, **kwargs)       

    return wrapper

@app.route("/login")
def login():
    pass

@app.route("/callback")
def callback():
    pass

@app.route("/logout")
def logout():
    pass

@app.route("/")
def index():
    return  "Hello, World!"

@app.route("/proctected_page")
@login_is_requiered
def protected_page():
    return "This is a protected page"

if __name__ == "__main__":
    app.run(debug=True)



