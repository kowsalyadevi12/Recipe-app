from flask import jsonify, request
from flask_jwt_extended import jwt_required, create_access_token,get_jwt_identity

from app import app, db
from app.models import User, Recipe, Comment

# User registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'Missing username or password'}), 400
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists'}), 400
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    app.logger.debug("Message")
    return jsonify({'user_id': user.id}), 201


# User login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({'error': 'Invalid username or password'}), 401
    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token}), 200


#create new recipe
@app.route('/recipes', methods=['POST'])
@jwt_required()
def create_recipe():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    user_id = get_jwt_identity()
    recipe = Recipe(title=title, description=description, author_id=user_id)
    db.session.add(recipe)
    db.session.commit()
    return jsonify({'recipe_id': recipe.id}), 201


#Update a recipe
@app.route('/update_recipes/int:recipe_id', methods=['PUT'])
@jwt_required()
def update_recipe(recipe_id):
    data = request.get_json()
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return jsonify({'error': 'Recipe not found'}), 404
    recipe.title = data.get('title', recipe.title)
    recipe.description = data.get('description', recipe.description)
    db.session.commit()
    return jsonify({'message': 'Recipe updated successfully'}), 200


#Delete a recipe
@app.route('/recipes/int:recipe_id', methods=['DELETE'])
@jwt_required()
def delete_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return jsonify({'error': 'Recipe not found'}), 404
    db.session.delete(recipe)
    db.session.commit()
    return jsonify({'message': 'Recipe deleted successfully'}), 200


#Get all recipes
@app.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    recipe_list = []
    for recipe in recipes:
        recipe_list.append({
            'id': recipe.id,
            'title': recipe.title,
            'description': recipe.description,
            'author': recipe.author.username})
    return jsonify({'recipes': recipe_list}), 200


#Add a comment to a recipe
@app.route('/recipes/int:recipe_id/comments', methods=['POST'])
@jwt_required()
def add_comment(recipe_id):
    data = request.get_json()
    text = data.get('text')
    user_id = get_jwt_identity()
    comment = Comment(text=text, user_id=user_id, recipe_id=recipe_id)
    db.session.add(comment)
    db.session.commit()
    return jsonify({'comment_id': comment.id}), 201


