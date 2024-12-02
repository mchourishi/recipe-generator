from app import db

class Recipe(db.Model):
    __tablename__ = 'recipes'  # This defines the table name in the database

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    cuisine = db.Column(db.String(100), nullable=False)
    meal_type = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Recipe {self.name}>'
