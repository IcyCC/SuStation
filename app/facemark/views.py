from .. import db
from datetime import datetime
from flask import render_template,session,redirect,url_for
from . import facemark
from .forms import MarkComment
import InDate

@facemark.route('/mark',methods = ['GET','POST'])
def facemarking():
    id = InDate.getID()
    img_url = InDate.getItem()[id]['image_urls'][0]
    form = MarkComment()
    if form.validate_on_submit():
        InDate.setID(id+1)
        if form.score.data == 0 :
            return redirect(url_for("facemark.facemarking"))
        else:
            score = form.score.data
            InDate.outItem(id=id, url=img_url, score=score)
            return redirect(url_for("facemark.facemarking"))
    return  render_template("facemarking/index.html", img_url=img_url, form=form, id=id)
