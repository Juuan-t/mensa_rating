from flask import Blueprint

analytics_bp = Blueprint('analytics', __name__, url_prefix='/analytics')

@analytics_bp.route('/dish_ratings')
def getDishRatingsSuggestion():
    pass
    # TODO Ratings der Gerichte geordnet nach Beliebtheit

@analytics_bp.route('/suggestion_votes')
def getSuggestionVotes():
    pass
    # TODO Vorschläge geordnet nach Zeitstempel und Anzahl Votes

@analytics_bp.route('/heavy_users')
def getHeavyUsers():
    pass
    # TODO Nutzer geordnet nach Anzahl ihrer Vorschläge.