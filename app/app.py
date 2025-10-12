from flask import Flask, render_template

# Create Flask instance named 'app'
app = Flask(__name__)

# 1️⃣ Default route
@app.route("/")
def index():
    return "Hello CPS3500!"

# 2️⃣ New page route
@app.route("/new_page")
def new_page():
    return "This is a New Page!"

# 3️⃣ Dynamic route that uses a template
@app.route("/user/<username>")
def user(username):
    return render_template("greet.html", name=username)

# Run the app locally
if __name__ == "__main__":
    app.run(debug=True)
