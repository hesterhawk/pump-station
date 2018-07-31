from app import db
from datetime import datetime

class Pump(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.Integer)
    state_update_date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    fullname = db.Column(db.String(12), index=True, unique=True)
    location = db.Column(db.String(128))
    token = db.Column(db.String(24))

    def __repr__(self):
        return '<Pump {}>'.format(self.fullname)