from datetime import datetime
from flask import render_template,session,redirect,url_for,request
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
    page = request.args.get('page',1,type = int)
    form = CommentFrom()
    if form.validate_on_submit() :
        comment = Comment(name = form.Name.data,ctext = form.Text.data)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main.Self_introduction'))
    pagination = Comment.query.order_by(Comment.timestamp.desc()).paginate(\
        page,per_page=2,error_out=False)
    comments = pagination.items

    return render_template("self.html",form = form,comments = comments,pagination = pagination)
