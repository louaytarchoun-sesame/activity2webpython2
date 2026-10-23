from extensions import db

class User(db.Model):
    username = db.Column(db.String(20), primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(255))

    def __repr__(self):
        return f'<User {self.username} : {self.email}>'