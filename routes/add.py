from flask import Blueprint, jsonify, request
from models import Recipe,db

bp = Blueprint('add', __name__)

@bp.route('/add', methods = ['POST'])
def add_recipe():
    data = request.get_json()
    
    # Check if all necessary fields are provided
    if not data or not all(key in data for key in ['name', 'ingredients', 'instructions', 'cuisine', 'meal_type']):
        return jsonify({"error": "Missing required fields"}), 400
    
     # Create a new Recipe object
    new_recipe = Recipe(
        name=data['name'],
        ingredients=data['ingredients'],
        instructions=data['instructions'],
        cuisine=data['cuisine'],
        meal_type=data['meal_type']
    )
    
    # Add the new recipe to the database
    db.session.add(new_recipe)
    
    try:
        # Commit the transaction to save the recipe
        db.session.commit()
        return jsonify({
            "message": "Recipe added successfully",
            "id": new_recipe.id,
            "name": new_recipe.name
        }), 201  # HTTP 201: Created
    except Exception as e:
        # Rollback the session in case of an error
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        # Close the session (optional but recommended)
        db.session.remove()