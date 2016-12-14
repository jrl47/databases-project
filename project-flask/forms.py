from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired

class PlayerSearchFormFactory:
    @staticmethod
    def form():
        class F(FlaskForm):
            first_last = StringField(default="")
            attribute = SelectField('Attribute', choices=[('pts', 'Points'), ('ast', 'Assists'), ('reb', 'Rebounds'), ('blk', 'Blocks'), ('stl', 'Steals')])
            predicate = SelectField('Predicate', choices=[('greater', '>='), ('less', '<='), ('equal', '=')])
            value = IntegerField(default=0)
            attribute2 = SelectField('Attribute', choices=[('pts', 'Points'), ('ast', 'Assists'), ('reb', 'Rebounds'), ('blk', 'Blocks'), ('stl', 'Steals')])
            predicate2 = SelectField('Predicate', choices=[('greater', '>='), ('less', '<='), ('equal', '=')])
            value2 = IntegerField(default=0)
            attribute3 = SelectField('Attribute', choices=[('pts', 'Points'), ('ast', 'Assists'), ('reb', 'Rebounds'), ('blk', 'Blocks'), ('stl', 'Steals')])
            predicate3 = SelectField('Predicate', choices=[('greater', '>='), ('less', '<='), ('equal', '=')])
            value3 = IntegerField(default=0)
            attribute4 = SelectField('Attribute', choices=[('pts', 'Points'), ('ast', 'Assists'), ('reb', 'Rebounds'), ('blk', 'Blocks'), ('stl', 'Steals')])
            predicate4 = SelectField('Predicate', choices=[('greater', '>='), ('less', '<='), ('equal', '=')])
            value4 = IntegerField(default=0)
            attribute5 = SelectField('Attribute', choices=[('pts', 'Points'), ('ast', 'Assists'), ('reb', 'Rebounds'), ('blk', 'Blocks'), ('stl', 'Steals')])
            predicate5 = SelectField('Predicate', choices=[('greater', '>='), ('less', '<='), ('equal', '=')])
            value5 = IntegerField(default=0)
            orderby = SelectField('Attribute', choices=[('pts', 'Points'), ('ast', 'Assists'), ('reb', 'Rebounds'), ('blk', 'Blocks'), ('stl', 'Steals')])
        return F()

class StatSearchFormFactory:
    @staticmethod
    def form():
        class F(FlaskForm):
            pts = IntegerField(default=0)
            ast = IntegerField(default=0)
            reb = IntegerField(default=0)
            blk = IntegerField(default=0)
            stl = IntegerField(default=0)
        return F()
