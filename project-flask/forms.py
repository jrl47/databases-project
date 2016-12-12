from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired

class PlayerSearchFormFactory:
    @staticmethod
    def form():
        class F(FlaskForm):
            first_last = StringField(default="")
            query_type = SelectField('Type', choices=[('players', 'Players'), ('teams', 'Teams')])
            attribute = SelectField('Attribute', choices=[('pts', 'Points'), ('ast', 'Assists'), ('reb', 'Rebounds'), ('blk', 'Blocks'), ('stl', 'Steals')])
            predicate = SelectField('Predicate', choices=[('greater', '>'), ('less', '<'), ('equal', '=')])
            value = IntegerField(default=0)
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
