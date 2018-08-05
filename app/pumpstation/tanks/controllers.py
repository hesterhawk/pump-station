from flask import Blueprint, request, current_app, render_template, flash, redirect, url_for
from flask_login import current_user
from flask_paginate import Pagination, get_page_parameter
from datetime import datetime

from .forms.create_tank import CreateTankForm
from .forms.update_tank import UpdateTankForm

tanks = Blueprint('tanks', __name__, template_folder="views")

from app import db
from app.models.tank import Tank

# For pagination
PER_PAGE = 10

@tanks.route('/tanks', methods=['GET'])
def all():    

    page = request.args.get(get_page_parameter(), type=int, default=1)
    tanks = Tank.query.order_by(Tank.created_date).paginate(page, PER_PAGE, False).items

    pagination = Pagination(per_page=PER_PAGE, page=page, total=Tank.query.count(), record_name='tanks', css_framework='bootstrap4')

    return render_template('all_tanks.html', tanks=tanks, pagination=pagination)

@tanks.route('/tank/create', methods=['GET', 'POST'])
def create():
    form = CreateTankForm()
    if form.validate_on_submit():
        tank = Tank(state=1, state_update_date=datetime.now(), created_date=datetime.now(), fullname=form.fullname.data, location=form.location.data, token=form.token.data)
        db.session.add(tank)
        db.session.commit()

        flash("Water tank created successfully!")
        return redirect(url_for('tanks.all'))

    return render_template('create_tank.html', form=form)

@tanks.route('/tank/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    tank = Tank.query.get(id)
    form = UpdateTankForm()
    form.set_tank_id(id)

    if form.validate_on_submit():
        tank.fullname=form.fullname.data
        tank.location=form.location.data
        tank.token=form.token.data
        db.session.commit()
        
        flash("Water tank updated successfully!")
        return redirect(url_for('tanks.all'))        

    return render_template('update_tank.html', tank=tank, form=form)

@tanks.route('/tank/destroy/<int:id>', methods=['GET', 'POST'])
def destroy(id):
    tank = Tank.query.get(id)

    if "POST" == request.method:
        db.session.delete(tank)
        db.session.commit()

        flash("Water tank destroyed successfully!")
        return redirect(url_for('tanks.all'))      

    return render_template('destroy_tank.html', tank=tank)  