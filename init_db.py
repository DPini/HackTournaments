from models import db
from hacktournaments import app

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
