from flask import Blueprint

site = Blueprint('site', __name__)

from prices.site import views