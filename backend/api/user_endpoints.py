from flask import Blueprint
from backend.db.dao import UserDao

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/register', methods=['POST'])
def registerUser():
    pass
    # TODO register user

@user_bp.route('/login', methods=['POST'])
def login():
    pass
    # TODO login user

@user_bp.route('/suggest_dish', methods=['POST'])
def suggestDish():
    pass
    # TODO login user
