from flask import Blueprint

ratings_bp = Blueprint('rating', __name__, url_prefix='/rating')

@ratings_bp.route('/vote_suggstion', methods=['POST'])
def voteSuggestion():
    pass
    # TODO register user

@ratings_bp.route('/vote_suggstion', methods=['POST'])
def rateDish():
    pass
    # TODO register user