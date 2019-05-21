from flask import Blueprint
main = Blueprint('main', __name__)
from . import views, error
# To  avoid circular dependencies we import the views
# and errors modules.