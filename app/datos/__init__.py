from flask import Blueprint

datos = Blueprint('datos',__name__, template_folder='templates')

from . import routes