from flask_wtf import FlaskForm
from wtforms.validators import Length, DataRequired
from wtforms.fields import StringField,IntegerField, SubmitField

class NewTournamentForm(FlaskForm):
    name = StringField('Tournament name', validators=[DataRequired(), Length(max=100)])
    max_teams = StringField('Max # teams')
    max_players_team = StringField('Max # team members')
    submit = SubmitField("Create!")

class NewTeamForm(FlaskForm):
    name = StringField('Team name', validators=[DataRequired(), Length(max=100)])
    submit = SubmitField("Create!")
