from datetime import datetime
from app import app, db
from app.models import Doctor, Patient, Appointment

with app.app_context():
    print('Deleting old data...')
    Appointment.query.delete()
    Doctor.query.delete()
    Patient.query.delete()

    print('Creating new doctors...')
    d1 = Doctor(name="Dr. Hibbert")
    d2 = Doctor(name="Dr. Nick")
    doctors = [d1, d2]

    print("Creating new patients...")
    p1 = Patient(name="Homer")
    p2 = Patient(name="Marge")
    p3 = Patient(name="Bart")

    print("Creating new appointments...")
    a1 = Appointment(
        reason="Annual Checkup",
        date=datetime(2025, 9, 15, 10, 30),
        doctor=d1,
        patient=p2
    )
    a2 = Appointment(
        reason="Skateboard Accident",
        date=datetime(2025, 9, 20, 14, 0),
        doctor=d2,
        patient=p3
    )
    a3 = Appointment(
        reason="Swallowed a Crayon",
        date=datetime(2025, 10, 1, 9 , 45),
        doctor=d1,
        patient=p1
    )
