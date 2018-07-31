from flask import Blueprint, current_app, render_template, flash, redirect, url_for
from flask_login import current_user
from datetime import datetime

from .forms.create_pump import CreatePumpForm

pumps = Blueprint('pumps', __name__, template_folder="views")

from app import db
from app.models.pump import Pump

@pumps.route('/pumps', methods=['GET'])
def all():    
    return render_template('all_pumps.html')

@pumps.route('/pump/create', methods=['GET', 'POST'])
def create():
    form = CreatePumpForm()
    if form.validate_on_submit():
        pump = Pump(state=1, state_update_date=datetime.now(), created_date=datetime.now(), fullname=form.fullname.data, location=form.location.data, token=form.token.data)
        db.session.add(pump)
        db.session.commit()

        flash("Water Pump created successfully!")
        return redirect(url_for('pumps.all'))

    return render_template('create_pump.html', form=form)