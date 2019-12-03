from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')

# Set database parameters
db_name, ip, user_name, password = 'usaspending', 'dopelytics.site:5432','team', 'ZAQ!@#zaq123'

# Connect to database
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://{}:{}@{}/{}'.format(user_name,password,ip,db_name)
SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy(app)

# Create model (table schema)
class test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contract_value = db.Column(db.String(50), unique=False, nullable=True)
    portfolio_group = db.Column(db.String(50), unique=False, nullable=True)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

# On /input request query db and return an array of contracts. Used for dropdowns.  
@app.route("/input")
def input():
    contracts = test.query.filter_by(portfolio_group='Construction Services').all()
    return render_template("input.html", contracts=contracts)

@app.route("/charts")
def charts():
    return render_template("charts.html")

@app.route("/handleData", methods=['POST'])
def handleData():
    projectpath = request.form['contractType']
    return render_template("running.html")
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='8090', threaded=True)