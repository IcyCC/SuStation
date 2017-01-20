# -*- coding:utf-8 -*-  
#存放表单
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import Required

class CommentFrom(Form):
    Name = StringField('Name',validators=[Required()])
    Text = TextAreaField('Comment',validators=[Required()])
    SubButton = SubmitField('Submit')

