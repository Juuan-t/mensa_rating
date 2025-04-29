from flask import Blueprint

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/register', methods=['POST'])
def registerUser():
    pass
    # TODO register user

@user_bp.route('/login', methods=['POST'])
def login():
    pass
    # TODO login user

