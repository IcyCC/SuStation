from datetime import datetime
from flask import render_template,session,redirect,url_for
from . import main
from .forms import*
from .. import *
from ..models import Comment
from ..auth.forms import CommentFrom

@main.route('/',methods = ['GET','POST'])
def index():
    return render_template("index.html")

@main.route('/Self',methods = ['GET','POST'])
def Self_introduction():
    form = CommentFrom()
    if form.validate_on_submit() :
        comment = Comment(name = form.Name.data,ctext = form.Text.data)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main.Self_introduction'))
    
    comments = Comment.query.order_by(Comment.timestamp.desc()).all()    
    return render_template("self.html",form = form,comments = comments)
