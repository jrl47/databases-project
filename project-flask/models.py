from sqlalchemy import sql, orm
from app import db

'''
class Player(db.Model):
    __tablename__ = 'player'
    id = db.Column('id', db.Integer(), primary_key=True)
    first_name = db.Column('first_name', db.String(20))
    last_name = db.Column('last_name', db.String(20))
'''

class Team(db.Model):
    __tablename__ = 'team'
    id = db.Column('id', db.Integer())
    conf_titles = db.Column('conf_titles', db.Integer())
    div_titles = db.Column('div_titles', db.Integer())
    start_year = db.Column('start_year', db.Integer())
    end_year = db.Column('end_year', db.Integer())
    games = db.Column('games', db.Integer())
    league_titles = db.Column('league_titles', db.Integer())
    wins = db.Column('wins', db.Integer())
    losses = db.Column('losses', db.Integer())
    po_appearances = db.Column('po_appearances', db.Integer())
    team_city = db.Column('team_city', db.String(25))
    team_id = db.Column('team_id', db.String(15), primary_key=True)
    team_name = db.Column('team_name', db.String(15))
    win_pct = db.Column('win_pct', db.Float())
    years = db.Column('years', db.Integer())

class Player(db.Model):
    __tablename__ = 'player'
    id = db.Column('id', db.Integer())
    first_last = db.Column('first_last', db.String(30))
    from_year = db.Column('from_year', db.Integer())
    to_year = db.Column('to_year', db.Integer())
    player_id = db.Column('player_id', db.String(10), primary_key=True)
    team_city = db.Column('team_city', db.String(25))
    team_id = db.Column('team_id', db.String(15), db.ForeignKey('team.team_id'))
    team_name = db.Column('team_name', db.String(15))

class Game(db.Model):
    __tablename__ = 'game'
    id = db.Column('id', db.Integer())
    pts = db.Column('pts', db.Float())
    ast = db.Column('ast', db.Float())
    blk = db.Column('blk', db.Float())
    stl = db.Column('stl', db.Float())
    reb = db.Column('reb', db.Float())
    oreb = db.Column('oreb', db.Float())
    dreb = db.Column('dreb', db.Float())
    tov = db.Column('tov', db.Float())
    fg3a = db.Column('fg3a', db.Float())
    fg3m = db.Column('fg3m', db.Float())
    fg3_pct = db.Column('fg3_pct', db.Float())
    fta = db.Column('fta', db.Float())
    ftm = db.Column('ftm', db.Float())
    ft_pct = db.Column('ft_pct', db.Float())
    min = db.Column('min', db.Float())
    pf = db.Column('pf', db.Float())
    plus_minus = db.Column('plus_minus', db.Float())
    game_date = db.Column('game_date', db.String(20))
    game_id = db.Column('game_id', db.String(20), primary_key=True)
    matchup = db.Column('matchup', db.String(20))
    player_id = db.Column('player_id', db.String(20), db.ForeignKey('player.player_id'), primary_key=True)
    w1 = db.Column('w1', db.String(1))
'''
    address = db.Column('address', db.String(20))
    likes = orm.relationship('Likes')
    frequents = orm.relationship('Frequents')
    @staticmethod
    def edit(old_name, name, address, beers_liked, bars_frequented):
        try:
            db.session.execute('DELETE FROM likes WHERE drinker = :name',
                               dict(name=old_name))
            db.session.execute('DELETE FROM frequents WHERE drinker = :name',
                               dict(name=old_name))
            db.session.execute('UPDATE drinker SET name = :name, address = :address'
                               ' WHERE name = :old_name',
                               dict(old_name=old_name, name=name, address=address))
            for beer in beers_liked:
                db.session.execute('INSERT INTO likes VALUES(:drinker, :beer)',
                                   dict(drinker=name, beer=beer))
            for bar, times_a_week in bars_frequented:
                db.session.execute('INSERT INTO frequents'
                                   ' VALUES(:drinker, :bar, :times_a_week)',
                                   dict(drinker=name, bar=bar,
                                        times_a_week=times_a_week))
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
class Beer(db.Model):
    __tablename__ = 'beer'
    name = db.Column('name', db.String(20), primary_key=True)
    brewer = db.Column('brewer', db.String(20))
class Bar(db.Model):
    __tablename__ = 'bar'
    name = db.Column('name', db.String(20), primary_key=True)
    address = db.Column('address', db.String(20))
    serves = orm.relationship('Serves')
class Likes(db.Model):
    __tablename__ = 'likes'
    drinker = db.Column('drinker', db.String(20),
                        db.ForeignKey('drinker.name'),
                        primary_key=True)
    beer = db.Column('beer', db.String(20),
                     db.ForeignKey('beer.name'),
                     primary_key=True)
class Serves(db.Model):
    __tablename__ = 'serves'
    bar = db.Column('bar', db.String(20),
                    db.ForeignKey('bar.name'),
                    primary_key=True)
    beer = db.Column('beer', db.String(20),
                     db.ForeignKey('beer.name'),
                     primary_key=True)
    price = db.Column('price', db.Float())
class Frequents(db.Model):
    __tablename__ = 'frequents'
    drinker = db.Column('drinker', db.String(20),
                        db.ForeignKey('drinker.name'),
                        primary_key=True)
    bar = db.Column('bar', db.String(20),
                    db.ForeignKey('bar.name'),
                    primary_key=True)
    times_a_week = db.Column('times_a_week', db.Integer())
'''
