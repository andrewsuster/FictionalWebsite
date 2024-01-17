from flask import Flask, render_template

app = Flask(__name__)





# the homepage for your site will be at the route below

@app.route('/')
def signup():
    return render_template("home.html")


@app.route('/realhome')
def home():
    return render_template("realhome.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/products')
def products():
    return render_template("products.html")



if __name__ == '__main__':
    app.run(debug=True)