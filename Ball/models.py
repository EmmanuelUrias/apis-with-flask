from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Reptiles(db.Model):
    __tablename__ = 'reptiles'

    id = db.Column(db.Integer, primary_key = True)
    reptile_name = db.Column(db.String(250))
    reptile_age = db.Column(db.Integer)
    reptile_weight = db.Column(db.Integer)