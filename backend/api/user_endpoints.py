from flask import Blueprint, request
from backend.db.user_dao import UserDAO

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/register', methods=['POST'])
def registerUser():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')

        if not email or not password or not name:
            return "error", 400
        
        if not UserDAO().password_complexity(password):
            return "Passwort unsicher", 400
        
        if UserDAO().get_user(email):
            return "Nutzer existiert bereits", 400

        UserDAO().insert_user(email, name, password)

    return "Method not allowed", 405

@user_bp.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            return "Email and password are required", 400
        
        if UserDAO().check_password(email, password):
            return "Login successful", 200
        else:
            return "Invalid email or password", 401
        
    return "Method not allowed", 405

@user_bp.route('/suggest_dish', methods=['POST'])
def suggestDish():
    if request.method == 'POST':
        email = request.form.get('email')
        description = request.form.get('description')

        if not email or not description:
            return "email and description required", 400
        
        UserDAO().insert_suggestion(email, description)

    return "Method not allowed", 405

