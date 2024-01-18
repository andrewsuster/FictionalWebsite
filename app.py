from flask import Flask, render_template, request

app = Flask(__name__)

# Global variable to store the default value
default_username = "Create Account"

# the homepage for your site will be at the route below
@app.route('/')
def signup():
    return render_template("home.html", page_title=default_username)

@app.route('/realhome')
def home():
    return render_template("realhome.html", page_title=default_username)

@app.route('/about')
def about():
    return render_template("about.html", page_title=default_username)

@app.route('/contact')
def contact():
    return render_template("contact.html", page_title=default_username)

@app.route('/products')
def products():
    return render_template("products.html", page_title=default_username)

@app.route('/confirmation')
def confirmation():
    global default_username  # Declare default_username as a global variable

    name = request.args.get('usrname')
    email = request.args.get('email')

    # Update the default_username if name is provided
    if name:
        default_username = name

    props = {
        "name": name,
        "email": email
    }

    return render_template("confirmation.html", data=props, page_title=default_username)

if __name__ == '__main__':
    app.run(debug=True)
