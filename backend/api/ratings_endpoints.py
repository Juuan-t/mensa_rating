from flask import Blueprint, request
from backend.db.user_dao import UserDao
from backend.db.rating_dao import RatingDAO

ratings_bp = Blueprint('rating', __name__, url_prefix='/rating')

@ratings_bp.route('/vote_suggstion', methods=['POST'])
def voteSuggestion():
    pass
    # TODO register user

@ratings_bp.route('/rate_dish', methods=['POST'])
def rateDish():
    if request.method == 'POST':
        email = request.form.get('email')
        dish_id = request.form.get('dish_id')
        stars = request.form.get('stars')
        comment = request.form.get('comment')
        if not email or not dish_id or not stars:
            return "error", 400
        if not stars.isnumeric() or int(stars) < 1 or int(stars) > 5:
            return "You can only assign Stars between 1 and 5", 400
        
        if RatingDAO().get_rating(dish_id, email):
            RatingDAO().alter_rating(dish_id, email, stars, comment)
        else:
            RatingDAO().insert_rating(email, stars, comment, dish_id)
        return "Rating successful", 200
    return "Method not allowed", 405
