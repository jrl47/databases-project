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


@app.route('/player/<id>')
def player(id):
    player = db.session.query(models.Player)\
        .filter(models.Player.id == id).one()
    return render_template('player.html', player=player)


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
                .filter(models.Player.last_name == form.last_name.data).one()
            return redirect(url_for('player', id = player.id))
        except BaseException as e:
            form.errors['database'] = str(e)
            return render_template('find-player.html', form=form)
    else:
        return render_template('find-player.html', form=form)


@app.template_filter('pluralize')
def pluralize(number, singular='', plural='s'):
    return singular if number in (0, 1) else plural

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
