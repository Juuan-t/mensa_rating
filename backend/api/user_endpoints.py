from flask import Blueprint, request
from backend.db.dao import UserDao

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/register', methods=['POST'])
def registerUser():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')

        if not email or not password or not name:
            return "error", 400
        
        if not UserDao().password_complexity(password):
            return "Passwort unsicher", 400
        
        if UserDao().get_user(email):
            return "Nutzer existiert bereits", 400

        UserDao().insert_user(email, name, password)

    return "Method not allowed", 400

@user_bp.route('/login', methods=['POST'])
def login():
    pass
    # TODO login user

@user_bp.route('/suggest_dish', methods=['POST'])
def suggestDish():
    pass
    # TODO login user
