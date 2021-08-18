from flask import render_template
from prices.site import site

@site.route('/')
@site.route('/index')
def index():
    return render_template('index.html')