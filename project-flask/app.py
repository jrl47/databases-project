from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config.from_object('config')
db = SQLAlchemy(app, session_options={'autocommit': False})
import models
import forms

@app.route('/')
def all_players():
    players = db.session.query(models.Player).all()
    return render_template('all-players.html', players=players)


@app.route('/player/<player_id>')
def player(player_id):
    player = db.session.query(models.Player)\
        .filter(models.Player.player_id == player_id).one()
    team = db.session.query(models.Team)\
        .filter(models.Team.team_id == player.team_id).one()
    return render_template('player.html', player=player,team=team)


@app.route('/search', methods=['GET', 'POST'])
def search():
#   player = db.session.query(models.Drinker)\
#       .filter(models.Drinker.name == name).one()
#   beers = db.session.query(models.Beer).all()
#   bars = db.session.query(models.Bar).all()
#   form = forms.DrinkerEditFormFactory.form(drinker, beers, bars)
    form = forms.PlayerSearchFormFactory.form()
    if form.validate_on_submit():
        try:
            form.errors.pop('database', None)
#           models.Drinker.edit(name, form.name.data, form.address.data,
#                               form.get_beers_liked(), form.get_bars_frequented())
            player = db.session.query(models.Player)\
                .filter(models.Player.from_year == 2010).all()
            return render_template('all-players.html', players=player)
        except BaseException as e:
            form.errors['database'] = str(e)
            return render_template('find-player.html', form=form)
    else:
        return render_template('find-player.html', form=form)

@app.route('/query', methods=['GET', 'POST'])
#def search():
 
#stats is an array of length 5, with entries for points, assists, rebounds, blocks, and steals (in that order)

def query():
#   player = db.session.query(models.Drinker)\
#       .filter(models.Drinker.name == name).one()
#   beers = db.session.query(models.Beer).all()
#   bars = db.session.query(models.Bar).all()
#   form = forms.DrinkerEditFormFactory.form(drinker, beers, bars)
    form = forms.StatSearchFormFactory.form()
    if form.validate_on_submit():
        try:
            form.errors.pop('database', None)
#           models.Drinker.edit(name, form.name.data, form.address.data,
#                               form.get_beers_liked(), form.get_bars_frequented())
#            player = db.session.query(models.Game)\
#                .filter(models.Game.pts >= stats[0] and models.Game.ast >= stats[1] and models.Game.reb >= stats[2] and models.Game.blk >= stats[3] and models.Game.stl >= stats[4]).all()
            game = db.session.query(models.Game,models.Player)\
                .join(models.Player)\
                .filter(models.Game.pts >= form.pts.data).filter(models.Game.player_id == models.Player.player_id).all()
            print game
	    #game = db.session.query(models.Game)\
            #    .filter(models.Game.pts >= form.pts.data).all()
            return render_template('search-results.html', players=game)
        except BaseException as e:
            form.errors['database'] = str(e)
            return render_template('search-stats.html', form=form)
    else:
        return render_template('search-stats.html', form=form)


@app.template_filter('pluralize')
def pluralize(number, singular='', plural='s'):
    return singular if number in (0, 1) else plural

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
