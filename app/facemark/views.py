from .. import db
from datetime import datetime
from flask import render_template,session,redirect,url_for
from . import facemark
from .forms import MarkComment
import InDate

@facemark.route('/mark',methods = ['GET','POST'])
def facemarking():
    #img_url = 'a'
    img_url = InDate.getItem().next()['image_urls'][0]
    form = MarkComment()
    if form.validate_on_submit():
        if form.score.data is None:
            return redirect(url_for("facemark.facemarking"))
        else:
            score = form.score.data
            InDate.outItem(img_url,score)
        return redirect(url_for("facemark.facemarking"))
    return  render_template("facemarking/index.html",img_url = img_url,form = form)
