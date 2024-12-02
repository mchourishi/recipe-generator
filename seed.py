from app import create_app, db
from models import Recipe

# Sample data to seed into the database
sample_recipes = [
    {"name": "Spaghetti Carbonara", "ingredients": "spaghetti, egg, cheese, pancetta", "instructions": "Boil pasta, mix with eggs, cheese, pancetta", "cuisine": "Italian", "meal_type": "Main"},
    {"name": "Chicken Curry", "ingredients": "chicken, curry powder, onions, garlic", "instructions": "Cook chicken with spices, add onions and garlic", "cuisine": "Indian", "meal_type": "Main"},
    {"name": "Caesar Salad", "ingredients": "lettuce, croutons, parmesan, caesar dressing", "instructions": "Toss lettuce and croutons with dressing", "cuisine": "American", "meal_type": "Side"}
]

def seed_data():
    app = create_app()
    
    # Use the app context to interact with the database
    with app.app_context():
        # Clear any existing data
        # db.drop_all()  # Optional: Drop existing tables if you want to reset the DB
        db.create_all()  # Create tables if they don't exist
        
        # Insert sample data
        for recipe in sample_recipes:
            new_recipe = Recipe(
                name=recipe["name"],
                ingredients=recipe["ingredients"],
                instructions=recipe["instructions"],
                cuisine=recipe["cuisine"],
                meal_type=recipe["meal_type"]
            )
            db.session.add(new_recipe)
        
        # Commit the session to save data to the database
        db.session.commit()

    print("Data seeded successfully!")

if __name__ == "__main__":
    seed_data()
