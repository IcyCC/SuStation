# -*- coding:utf-8 -*-  
#存放表单
from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField, TextAreaField, validators,StringField,SubmitField,SelectField
from wtforms.validators import Required
from flask_pagedown.fields import PageDownField

class Compose(Form):
    tittle = StringField('tittle',validators=[Required()])
    body = PageDownField('Enter your idea', validators=[Required()])
    kind = SelectField('Colum',coerce=int,choices=[(1,u'Web开发'),(2,u'机器学习'),(3,u'用python娱乐'),(4,u'知乎的收获'),(5,u'随写')])
    sub = SubmitField('Submit')

class KindForm(Form):
    name = StringField('name')
    sub = SubmitField('Submit')

