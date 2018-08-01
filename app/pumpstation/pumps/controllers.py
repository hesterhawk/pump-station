from flask import Blueprint, request, current_app, render_template, flash, redirect, url_for
from flask_login import current_user
from flask_paginate import Pagination, get_page_parameter
from datetime import datetime

from .forms.create_pump import CreatePumpForm

pumps = Blueprint('pumps', __name__, template_folder="views")

from app import db
from app.models.pump import Pump

# For pagination
PER_PAGE = 10

@pumps.route('/pumps', methods=['GET'])
def all():    

    page = request.args.get(get_page_parameter(), type=int, default=1)
    pumps = Pump.query.order_by(Pump.created_date).paginate(page, PER_PAGE, False).items

    pagination = Pagination(per_page=PER_PAGE, page=page, total=Pump.query.count(), record_name='pumps', css_framework='bootstrap4')

    return render_template('all_pumps.html', pumps=pumps, pagination=pagination)

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