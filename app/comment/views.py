from datetime import datetime
from flask import render_template,session,redirect,url_for
from . import comment
from .forms import CommentFrom
from .. import *
from ..models import *


@comment.route('/Comment',methods = ['GET','POST'])
def Comment_to():
    return render_template("comment/comment.html")

