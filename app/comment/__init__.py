from flask import Blueprint

main = Blueprint('comment',__name__)

from .import views,errors