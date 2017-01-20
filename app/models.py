# -*- coding:utf-8 -*-  
from . import db
from datetime import datetime
from markdown import markdown
import bleach
class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(64))
    ctext = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index = True,default = datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.ctext

class Essay(db.Model):
    __tablename__ = 'essays'

    id = db.Column(db.Integer,primary_key = True)
    tittle = db.Column(db.String(300),index=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime,default=datetime.utcnow,index=True)
    kind_id = db.Column(db.Integer, db.ForeignKey('kinds.id'))
    body_html = db.Column(db.Text)

    def __repr__(self):
        return '<Essay %r>' % self.tittle

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                            'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
                            'h1', 'h2', 'h3', 'p']
        target.body_html = bleach.linkify(bleach.clean(\
                markdown(value, output_format='html'),\
                tags=allowed_tags, strip=True))

db.event.listen(Essay.body, 'set', Essay.on_changed_body)



class Kind(db.Model):
    __tablename__ = 'kinds'

    id = db.Column(db.Integer, primary_key = True,index= True)
    name = db.Column(db.String(200))

    essays = db.relationship('Essay', backref='kind')

    def __repr__(self):
        return '<Kind %r >' % self.name



