from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# 1. App and Database Configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# 2. Import Models
from app.models import Doctor, Patient, Appointment 


# 3. Routes
@app.route('/')
def index():
    return "<h1>Doctor's Office App</h1>"

# 4. Main Execution Block
if __name__ == '__main__':
    app.run(port=5555, debug=True)