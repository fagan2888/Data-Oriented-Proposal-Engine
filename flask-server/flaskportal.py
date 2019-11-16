from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/input")
def input():
    return render_template("input.html")

@app.route("/charts")
def charts():
    return render_template("charts.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')