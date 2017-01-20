from .. import db
from datetime import datetime
from flask import render_template,session,redirect,url_for
from . import auth
from .forms import CommentFrom
from ..models import Comment

@auth.route('/Comment',methods = ['GET','POST'])
def Comment_to():
    form = CommentFrom()
    if form.validate_on_submit() :
        comment = Comment(name = form.Name.data,ctext = form.Text.data)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('auth.Comment_to'))
    comments = Comment.query.order_by(Comment.timestamp.desc()).all()    

    return render_template("comment/comment.html",form = form,comments = comments)

