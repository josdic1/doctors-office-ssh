# Import the 'app' object from our app package
from app import app
# Import the models so Flask-Migrate can see them
from app.models import Doctor, Patient, Appointment 

@app.route('/')
def index():
    return "<h1>Doctor's Office App</h1>"

if __name__ == '__main__':
    app.run(port=5555, debug=True)