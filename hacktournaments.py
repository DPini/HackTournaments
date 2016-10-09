from flask import Flask,render_template, request, flash, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import *
from forms import *
from flask_oauthlib.client import OAuth


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY']="usfhduihsduighifduhgighsfihgwihgiusfdgihsdi"

oauth = OAuth(app)

slack = oauth.remote_app(
    'slack',
    consumer_key='88963600400.88997176354',
    consumer_secret='secret',
    request_token_params={'scope': 'identity.basic,identity.avatar'},
    base_url='https://slack.com/',
    request_token_url=None,
    access_token_method='GET',
    access_token_url='https://slack.com/api/oauth.access',
    authorize_url='https://slack.com/oauth/authorize'
)


### API ###

@app.route('/oauth_debug')
def oauth_debug():
    if 'github_token' in session:
        me = github.get('user')
        return jsonify(me.data)
    return redirect(url_for('login'))


@app.route('/login')
def login():
    return slack.authorize(callback=url_for('authorized', _external=True))


@app.route('/logout')
def logout():
    session.pop('slack_token', None)
    return redirect(url_for('index'))


@app.route('/login/authorized')
def authorized():
    resp = slack.authorized_response()
    if resp is None or resp.get('access_token') is None:
        return 'Access denied: reason=%s error=%s resp=%s' % (
            request.args['error'],
            request.args['error_description'],
            resp
        )
    session['slack_token'] = (resp['access_token'], '')
    me = slack.get('user')
    return jsonify(me.data)


@slack.tokengetter
def get_slack_oauth_token():
    return session.get('slack_token')



@app.context_processor
def inject_tournaments():
    return dict( tournaments=Tournament.query.all() )



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/tournament/new', methods=['GET','POST'])
def new_tournament():
    print(request.headers)
    form = NewTournamentForm()
    if request.method == 'POST' and form.validate_on_submit():
        t = Tournament( name=form.name.data, max_teams=form.max_teams.data, max_players_team = form.max_players_team.data )
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('tournament', id=t.id))
    return render_template("tournaments/new_tournament.html",form=form)

@app.route('/tournament/<id>')
def tournament(id):
    return render_template("tournaments/tournament.html", teams = Team.get_teams_by_tournament(id)
    , tment = Tournament.query.get(id))

@app.route('/tournament/<t_id>/team/new', methods=['GET','POST'])
def new_team(t_id):
    form = NewTeamForm()
    if request.method == 'POST' and form.validate_on_submit():
        print("t_id:",t_id)
        t = Team( name=form.name.data, tournament = t_id )
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('team',t_id=t_id, team_id=t.id))
    return render_template("tournaments/teams/new_team.html",form=form)

@app.route('/tournament/<t_id>/team/<team_id>')
def team(t_id,team_id):
    return "test"


if __name__ == "__main__":
    db.init_app(app)
    #with app.app_context():
    #    db.create_all()
    app.run(debug=True)
