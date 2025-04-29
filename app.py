from flask import Flask
import backend.api.analytics_endpoints as ae
import backend.api.menu_endpoints as me
import backend.api.ratings_endpoints as re
import backend.api.user_endpoints as ue

app = Flask(__name__)
app.register_blueprint(ae.analytics_bp)
app.register_blueprint(me.menu_bp)
app.register_blueprint(ue.user_bp)
app.register_blueprint(re.ratings_bp)