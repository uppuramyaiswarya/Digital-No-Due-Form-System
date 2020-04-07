from flask import Blueprint

nodues = Blueprint('nodues', __name__)

from . import routes, models