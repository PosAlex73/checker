from wtforms import StringField, validators, Form


class JsonValidateForm(Form):
    language = StringField('language', [validators.AnyOf(["php", "python", "go"])])
    code = StringField('code', [validators.Length(min=5, max=25)])
