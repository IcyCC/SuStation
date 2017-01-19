# -*- coding:utf-8 -*-  
from . import db
from datetime import datetime

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(64))
    ctext = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index = True,default = datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.ctext
