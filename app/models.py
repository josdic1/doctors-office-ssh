from sqlalchemy_serializer import SerializerMixin
from flask_sqlalchemy import SQLAlchemy

from app import db

class Doctor(db.Model, SerializerMixin):
    __tablename__ = 'doctors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    # Relationship to appointments
    appointments = db.relationship('Appointment', back_populates='doctor')

class Patient(db.Model, SerializerMixin):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    # Relationship to appointments
    appointments = db.relationship('Appointment', back_populates='patient')

class Appointment(db.Model, SerializerMixin):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    reason = db.Column(db.String)

    # Foreign keys to link doctors and patients
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))

    # Relationships to access the Doctor and Patient objects
    doctor = db.relationship('Doctor', back_populates='appointments')
    patient = db.relationship('Patient', back_populates='appointments')