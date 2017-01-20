from .. import db
from datetime import datetime
from flask import render_template,session,redirect,url_for
from ..models import Essay,Kind
from .forms import Compose,KindForm
from . import write


@write.route('/kind',methods = ['GET','POST'])
def Write_addKind():
    form = KindForm()

    if form.validate_on_submit() :
        kind = Kind(name = form.name.data)
        db.session.add(kind)
        db.session.commit()
        return redirect(url_for('write.addKind'))
    return render_template('write/kindadd.html',form = form)

@write.route('/',methods = ['GET','POST'])
def Write_compose():
    form = Compose()
    if form.validate_on_submit() :
        essay = Essay(tittle = form.tittle.data,body = form.body.data,kind_id = form.kind.data )
        db.session.add(essay)
        db.session.commit()
        return redirect(url_for('write.Write_compose'))
    return render_template('write/write.html',form = form)
