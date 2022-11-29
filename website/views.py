import mimetypes
import os
from re import X
from unicodedata import name
from flask import Blueprint, appcontext_popped, redirect, render_template, request, flash, jsonify, url_for
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from .models import FDP, Note,Events,Workshops,publications,CP,JOURNAL
from . import db
import json
views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        teacher = request.form['teacher']
        journal = request.form['journal']
        year = request.form['year']
        link = request.form['link']
        index = request.form['index']
       

        new_note = Note(title=title, author=author, department_teacher=teacher,journal=journal,publication_year=year,link=link,h_index=index, user_id=current_user.id)

        db.session.add(new_note)
        db.session.commit()
        flash('added!', category='success')  


    return render_template("home.html", user=current_user)




  
@views.route('/Workshops', methods=['GET', 'POST'])
@login_required
def workshops():
    if request.method == 'POST':
        Academic_Year = request.form['Academic_Year']
        Workshop_Name = request.form['Workshop_Name']
        Proposal_Date = request.form['Proposal_Date']
        Conductin_Date = request.form['Conductin_Date']
        Instituion_Approval = request.form['Instituion_Approval']
        Report = request.form['Report']
       

        new_Workshops = Workshops(Academic_Year=Academic_Year, Workshop_Name=Workshop_Name, Proposal_Date=Proposal_Date,Conductin_Date=Conductin_Date,Instituion_Approval=Instituion_Approval,Report=Report, user_id=current_user.id)

        db.session.add(new_Workshops)
        db.session.commit()
        flash('Workshops added!', category='success')
    return render_template("workshops.html",user=current_user)



@views.route('/Events', methods=['GET', 'POST'])
@login_required
def events():
    if request.method == 'POST':
        Event_Name = request.form['Event_Name']
        Proposal_Date = request.form['Proposal_Date']
        Conductin_Date = request.form['Conductin_Date']
        Instituion_Approval = request.form['Instituion_Approval']
        Report = request.form['Report']
       

        new_events = Events(Event_Name=Event_Name, Proposal_Date=Proposal_Date,Conductin_Date=Conductin_Date,Instituion_Approval=Instituion_Approval,Report=Report, user_id=current_user.id)

        db.session.add(new_events)
        db.session.commit()
        flash('Events added!', category='success')
    return render_template("events.html",user=current_user)


@views.route('/Publications', methods=['GET', 'POST'])
@login_required
def publication():
    if request.method == 'POST':
        JournalName_Conference = request.form['JournalName_Conference']
        ISSN_ISBN_Number_Progress = request.form['ISSN_ISBN_Number_Progress']
        Month_and_Year = request.form['Month_and_Year']
        Title = request.form['Title']
        Link = request.form['Link']
       

        new_publications = publications(JournalName_Conference=JournalName_Conference, ISSN_ISBN_Number_Progress=ISSN_ISBN_Number_Progress,Month_and_Year=Month_and_Year,Title=Title,Link=Link, user_id=current_user.id)

        db.session.add(new_publications)
        db.session.commit()
        flash('publications added!', category='success')
    return render_template("publications.html",user=current_user)




@views.route('/FDP', methods=['GET', 'POST'])
@login_required
def fdp():
    if request.method == 'POST':
        Proposal_Name = request.form['Proposal_Name']
        Organization_Name = request.form['Organization_Name']
        Start_Date = request.form['Start_Date']
        Completion_Date = request.form['Completion_Date']
        Status_Preparation = request.form['Status_Preparation']
        Proposal_Copy = request.form['Proposal_Copy']
        Final_Report = request.form['Final_Report']
       

        new_FDP = FDP(Proposal_Name=Proposal_Name, Organization_Name=Organization_Name, Start_Date=Start_Date,Completion_Date=Completion_Date,Status_Preparation=Status_Preparation,Proposal_Copy=Proposal_Copy,Final_Report=Final_Report, user_id=current_user.id)

        db.session.add(new_FDP)
        db.session.commit()
        flash('FDP added!', category='success')
    return render_template("FDP.html", user=current_user)


@views.route('/CP', methods=['GET', 'POST'])
@login_required
def cp():
    if request.method == 'POST':
        Proposal_Name = request.form['Proposal_Name']
        Organization_Name = request.form['Organization_Name']
        Start_Date = request.form['Start_Date']
        Completion_Date = request.form['Completion_Date']
        Status_Preparation = request.form['Status_Preparation']
        Proposal_Copy = request.form['Proposal_Copy']
        Final_Report = request.form['Final_Report']
       

        new_FDP = CP(Proposal_Name=Proposal_Name, Organization_Name=Organization_Name, Start_Date=Start_Date,Completion_Date=Completion_Date,Status_Preparation=Status_Preparation,Proposal_Copy=Proposal_Copy,Final_Report=Final_Report, user_id=current_user.id)

        db.session.add(new_FDP)
        db.session.commit()
        flash('FDP added!', category='success')
    return render_template("cp.html", user=current_user)

@views.route('/JOURNAL', methods=['GET', 'POST'])
@login_required
def journal():
    if request.method == 'POST':
        JournalName = request.form['JournalName']
        ISSN_Number = request.form['ISSN_Number']
        month_and_years = request.form['month_and_years']
        Title = request.form['Title']
        Paper_Link = request.form['Paper_Link']
       

        new_FDP = JOURNAL(JournalName=JournalName, ISSN_Number=ISSN_Number, month_and_years=month_and_years,Title=Title,Paper_Link=Paper_Link,user_id=current_user.id)

        db.session.add(new_FDP)
        db.session.commit()
        flash('FDP added!', category='success')
    return render_template("journal.html", user=current_user)











@views.route('/download')
@login_required
def download():
    
    all_data= Note.query.filter_by(user_id=current_user.id).all()

    with open(f'website/static/data/{current_user.id}.csv',"w+") as f:
        for data in all_data:
            row = f"{data.title}, {data.author},{data.department_teacher},{data.journal},{data.publication_year},{data.link},{data.h_index}"
            f.write(row)  
            f.write("\n")
    
    return render_template("download.html", link=f'/static/data/{current_user.id}.csv')





@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
        return jsonify({})






@views.route('/delete-events', methods=['POST'])
def delete_Events():
    Events = json.loads(request.data)
    EventsId = Events['EventsId']
    Events = Events.query.get(EventsId)
    if Events:
        if events.user_id == current_user.id:
            db.session.delete(Events)
            db.session.commit()
        return jsonify({})



