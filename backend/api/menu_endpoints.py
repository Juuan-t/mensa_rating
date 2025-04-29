from flask import Blueprint

menu_bp = Blueprint('menu', __name__, url_prefix='/menu')

@menu_bp.route('/add_menu_item')
def registerUser():
    pass
    # TODO register user

@menu_bp.route('/login', methods=('POST'))
def login():
    pass
    # TODO login user