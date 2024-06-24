from wtforms import StringField, validators, Form
from config import getLangs

class JsonValidateForm(Form):
    language = StringField('language', [validators.AnyOf(getLangs())])
    code = StringField('code', [validators.Length(min=5, max=25)])
