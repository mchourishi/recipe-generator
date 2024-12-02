from flask import Blueprint, jsonify, request
from models import Recipe

bp = Blueprint('search', __name__)

@bp.route('/search', methods = ['GET'])
def search_recipes():
    query = request.args.get('query')
    
    recipes = Recipe.query.filter(
        (Recipe.cuisine.ilike(f'%{query}%')) |
        (Recipe.name.ilike(f'%{query}%')) |
        (Recipe.meal_type.ilike(f'%{query}%'))
        ).all()
    
    if recipes: 
        for recipe in recipes:
            return jsonify([{
                'name': recipe.name,
                'ingredients': recipe.ingredients,
                'instructions': recipe.instructions,
                'cuisine': recipe.cuisine,
                'meal_type': recipe.meal_type,
                'id': recipe.id,
            }])
    else:
        return jsonify({"error": "No Recipes Found"}), 404

