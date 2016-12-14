from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config.from_object('config')
db = SQLAlchemy(app, session_options={'autocommit': False})
import models
import forms

@app.route('/', methods=['GET', 'POST'])
def home():
    form = forms.PlayerSearchFormFactory.form()
    if request.method == 'POST':
        try:
            form.errors.pop('database', None)
            player = db.session.query(models.Game,models.Player)\
                .join(models.Player)\
                .filter(models.Game.player_id == models.Player.player_id)

            f = request.form
            rows = (len(f) - 1) / 3
            for i in range(0, rows):
                index = str(i + 1)
                predicate = f['predicate-' + index]
                attribute = getattr(models.Game, f['attribute-' + index])
                value = f['value-' + index]
                if predicate=='greater':
                    player = player.filter(attribute >= value)
                elif predicate=='less':
                    player = player.filter(attribute <= value)
                elif predicate=='equal':
                    player = player.filter(attribute == value)

            total = player.count()
            player = player.all()
            return render_template('result-list.html', results=player)
        except BaseException as e:
            form.errors['database'] = str(e)
            return render_template('home.html', form=form)
    else:
        return render_template('home.html', form=form)


@app.route('/player/<player_id>')
def player(player_id):
    player = db.session.query(models.Player)\
        .filter(models.Player.player_id == player_id).one()
    team = db.session.query(models.Team)\
        .filter(models.Team.team_id == player.team_id).one()
    return render_template('player.html', player=player,team=team)

@app.route('/team/<team_id>')
def team(team_id):
    team = db.session.query(models.Team)\
        .filter(models.Team.team_id == team_id).one()
    return render_template('team.html',team=team)


@app.route('/query', methods=['GET', 'POST'])
def query():
    form = forms.StatSearchFormFactory.form()
    if form.validate_on_submit():
        try:
            form.errors.pop('database', None)
            game = db.session.query(models.Game,models.Player)\
                .join(models.Player)\
                .filter(models.Game.pts >= form.pts.data).filter(models.Game.player_id == models.Player.player_id).all()
            return render_template('result-list.html', results=game)
        except BaseException as e:
            form.errors['database'] = str(e)
            return render_template('home.html', form=form)
    else:
        return render_template('home.html', form=form)


@app.template_filter('pluralize')
def pluralize(number, singular='', plural='s'):
    return singular if number in (0, 1) else plural

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
