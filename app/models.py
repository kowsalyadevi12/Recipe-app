from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    recipes = db.relationship('Recipe', backref='author', lazy='dynamic')
    
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    description = db.Column(db.String(256))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments = db.relationship('Comment', backref='recipe', lazy='dynamic')

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(256))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
