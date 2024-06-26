from werkzeug.security import generate_password_hash
from app import db
from flask import request, jsonify
from ..models.users import Users, user_schema, users_schema

def post_user():
    try:
        username = request.json.get('username')
        password = request.json.get('password')
        name = request.json.get('name')
        email = request.json.get('email')

        if not all([username, password, name, email]):
            return jsonify({'message': 'Missing required fields', 'data': {}}), 400

        pass_hash = generate_password_hash(password)
        user = Users(username=username, password=pass_hash, name=name, email=email)

        db.session.add(user)
        db.session.commit()

        result = user_schema.dump(user)
        return jsonify({'message': 'User successfully registered', 'data': result}), 201
    except Exception as e:
        return jsonify({'message': 'Unable to create user', 'error': str(e)}), 500

def update_user(id):
    username = request.json.get('username')
    password = request.json.get('password')
    name = request.json.get('name')
    email = request.json.get('email')

    user = Users.query.get(id)
    if not user:
        return jsonify({'message': "User doesn't exist", 'data': {}}), 404

    pass_hash = generate_password_hash(password)

    try:
        user.username = username
        user.password = pass_hash
        user.name = name
        user.email = email
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'message': 'User successfully updated', 'data': result}), 200
    except Exception as e:
        return jsonify({'message': 'Unable to update user', 'error': str(e)}), 500
    
def get_users():
    users = Users.query.all()

    if users:
        result = users_schema.dump(users)
        return jsonify({'message': 'successfully fetched', 'data': result}), 201

    return jsonify({'message': 'nothing found', 'data': {}}), 404

def get_user(id):
    user = Users.query.get(id)

    if user:
        result = user_schema.dump(user)
        return jsonify({'message': 'successfully fetched', 'data': result}), 201

    return jsonify({'message': 'nothing found', 'data': {}}), 404

def delete_user(id):
    user = Users.query.get(id)
    if not user:
        return jsonify({'message': "User doesn't exist", 'data': {}}), 404

    if user:
        try:
            db.session.delete(user)
            db.session.commit()
            result = user_schema.dump(user)
            return jsonify({'message': 'Successfully deleted', 'data': result}), 200
        except Exception as e:
            return jsonify({'message': 'Unable to delete', 'error': str(e)}), 500
        
def user_by_username(username):
    try:
        return Users.query.filter(Users.username == username).one()
    except:
        return None