from flask import Blueprint, current_app, render_template, redirect, url_for
from flask_login import current_user

pumps = Blueprint('pumps', __name__, template_folder="views")

@pumps.route('/pumps', methods=['GET'])
def all():    
    return render_template('all_pumps.html')