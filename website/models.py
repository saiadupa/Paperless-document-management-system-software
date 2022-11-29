from enum import unique
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    author = db.Column(db.String(100))
    department_teacher = db.Column(db.String(100))
    journal = db.Column(db.String(100))
    publication_year = db.Column(db.String(10))
    link = db.Column(db.String(200))
    h_index = db.Column(db.String(100))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))




class Workshops(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Academic_Year = db.Column(db.String(30))
    Workshop_Name = db.Column(db.String(100))
    Proposal_Date = db.Column(db.String(100))
    Conductin_Date = db.Column(db.String(100))
    Instituion_Approval = db.Column(db.String(10))
    Report = db.Column(db.String(200))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))





class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Event_Name = db.Column(db.String(30))
    Proposal_Date = db.Column(db.String(100))
    Conductin_Date = db.Column(db.String(100))
    Instituion_Approval = db.Column(db.String(10))
    Report = db.Column(db.String(10))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))




class publications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    JournalName_Conference = db.Column(db.String(30))
    ISSN_ISBN_Number_Progress = db.Column(db.String(100))
    Month_and_Year  = db.Column(db.String(100))
    Title = db.Column(db.String(10))
    Link = db.Column(db.String(10))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))




class FDP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Proposal_Name = db.Column(db.String(30))
    Organization_Name = db.Column(db.String(100))
    Start_Date = db.Column(db.String(100))
    Completion_Date = db.Column(db.String(100))
    Status_Preparation = db.Column(db.String(10))
    Proposal_Copy = db.Column(db.String(200))
    Final_Report = db.Column(db.String(100))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class CP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Proposal_Name = db.Column(db.String(30))
    Organization_Name = db.Column(db.String(100))
    Start_Date = db.Column(db.String(100))
    Completion_Date = db.Column(db.String(100))
    Status_Preparation = db.Column(db.String(10))
    Proposal_Copy = db.Column(db.String(200))
    Final_Report = db.Column(db.String(100))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))   

class JOURNAL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    JournalName = db.Column(db.String(30))
    ISSN_Number = db.Column(db.String(100))
    month_and_years  = db.Column(db.String(100))
    Title = db.Column(db.String(100))
    Paper_Link = db.Column(db.String(10))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))   




class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    Workshop = db.relationship('Workshops')
    Events = db.relationship("Events")
    publication = db.relationship('publications')
    fdp = db.relationship('FDP')
    cp=db.relationship('CP')
    journal=db.relationship('JOURNAL')

    

