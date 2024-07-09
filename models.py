from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(45), nullable=False)
    task = db.Column(db.String(300), nullable=False)
    status = db.Column(db.String(50), nullable=False)
