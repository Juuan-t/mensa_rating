from flask import Blueprint, request
from backend.db.dao import UserDao

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/register', methods=['POST'])
def registerUser():

    pass
    # TODO register user

@user_bp.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            return "Email and password are required", 400
        
        if UserDao().check_password(email, password):
            return "Login successful", 200
        else:
            return "Invalid email or password", 401
        
    return "Method not allowed", 405

@user_bp.route('/suggest_dish', methods=['POST'])
def suggestDish():
    pass
    # TODO login user
