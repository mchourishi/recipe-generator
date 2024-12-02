from flask import Blueprint, jsonify
from models import Recipe
from sqlalchemy import func

bp = Blueprint('random', __name__)

@bp.route('/random', methods=['GET'])
def get_random_recipe():
    recipe = Recipe.query.order_by(func.random()).first()  # SQLAlchemy random query
    if recipe:
        return jsonify(
            {
                "name": recipe.name,
                "ingredients": recipe.ingredients,
                "instructions": recipe.instructions,
                "cuisine": recipe.cuisine,
                "meal_type": recipe.meal_type,
                "id": recipe.id,
            }
        )
    return jsonify({"error": "No Recipes Found"}), 404
