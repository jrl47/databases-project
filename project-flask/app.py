from flask import Flask, render_template, redirect, url_for
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
    if form.validate_on_submit():
        try:
            form.errors.pop('database', None)
            if form.predicate.data=='greater':
                player = db.session.query(models.Game,models.Player)\
                    .join(models.Player)\
                    .filter(getattr(models.Game, form.attribute.data) >= form.value.data).filter(models.Game.player_id == models.Player.player_id)
            elif form.predicate.data=='less':
                player = db.session.query(models.Game,models.Player)\
                    .join(models.Player)\
                    .filter(getattr(models.Game, form.attribute.data) <= form.value.data).filter(models.Game.player_id == models.Player.player_id)
            elif form.predicate.data=='equal':
                player = db.session.query(models.Game,models.Player)\
                    .join(models.Player)\
                    .filter(getattr(models.Game, form.attribute.data) == form.value.data).filter(models.Game.player_id == models.Player.player_id)
            if form.predicate2.data=='greater':
                player = player.filter(getattr(models.Game, form.attribute2.data) >= form.value2.data)
            elif form.predicate2.data=='less':
                player = player.filter(getattr(models.Game, form.attribute2.data) <= form.value2.data)
            elif form.predicate2.data=='equal':
                player = player.filter(getattr(models.Game, form.attribute2.data) == form.value2.data)
            if form.predicate3.data=='greater':
                player = player.filter(getattr(models.Game, form.attribute3.data) >= form.value3.data)
            elif form.predicate3.data=='less':
                player = player.filter(getattr(models.Game, form.attribute3.data) <= form.value3.data)
            elif form.predicate3.data=='equal':
                player = player.filter(getattr(models.Game, form.attribute3.data) == form.value3.data)
            if form.predicate4.data=='greater':
                player = player.filter(getattr(models.Game, form.attribute4.data) >= form.value4.data)
            elif form.predicate4.data=='less':
                player = player.filter(getattr(models.Game, form.attribute4.data) <= form.value4.data)
            elif form.predicate4.data=='equal':
                player = player.filter(getattr(models.Game, form.attribute4.data) == form.value4.data)
            if form.predicate5.data=='greater':
                player = player.filter(getattr(models.Game, form.attribute5.data) >= form.value5.data)
            elif form.predicate5.data=='less':
                player = player.filter(getattr(models.Game, form.attribute5.data) <= form.value5.data)
            elif form.predicate5.data=='equal':
                player = player.filter(getattr(models.Game, form.attribute5.data) == form.value5.data)
            player = player.order_by(getattr(models.Game, form.orderby.data).desc()).limit(100).all()
            return render_template('result-list.html',results=player)
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

@app.route('/game/<game_id>/<player_id>/<matchup>')
def game(game_id,player_id,matchup):
    game = db.session.query(models.Game)\
        .filter(models.Game.game_id == game_id)\
        .filter(models.Game.player_id == player_id)\
        .filter(models.Game.matchup == matchup).one()
    player = db.session.query(models.Player)\
        .filter(models.Player.player_id == player_id).one()
    return render_template('game.html',game=game,player=player)

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
