from flask import Blueprint, current_app, render_template, redirect, url_for
from flask_login import current_user

main = Blueprint('main', __name__, template_folder="views")

@main.route('/', methods=['GET'])
def index():
    return render_template('main.html')
    
@main.route('/dashboard', methods=['GET'])
def dashboard():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))

    """
        TODO
        
        Calculate percentage of all water pumps
    """
    percent = 89

    return render_template('dashboard.html', percent=90, donut=_chartDonut(percent))

### private

def _chartDonut(percent):

    data = {
        39: "#b10c0c",  # red
        69: "#e2c912",  # yellow
        100: "#0cb120"  # green
    }

    color = list(filter(lambda x: percent < x, data))[-1]

    colors = "{'data1': '" + str(data[color]) + "','data2': '#dcdcdc'};"
    columns = "[['data1', {}],['data2', {}]];".format(percent, 100 - percent)

    return { "colors": colors, "columns": columns }
