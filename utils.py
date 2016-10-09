from models import Tournament,db
from hacktournaments import app


db.init_app(app)


def add_tournament(name,max_players_team,max_teams):
    t = Tournament(name=name,max_players_team=max_players_team,max_teams=max_teams)
    db.session.add(t)


if __name__ == "__main__":
    #add_tournament(name="Test",max_players_team=16,max_teams=12)
