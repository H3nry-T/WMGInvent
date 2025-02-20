from flask import Blueprint, request, render_template
from services.ElectronicsService import ElectronicsService
from repositories.ElectronicsRepository import ElectronicsRepository
from global_db_object import db
from flask_login import login_required, current_user
electronics_routes = Blueprint("electronics_routes", __name__)
electronics_service = ElectronicsService(ElectronicsRepository(db))

#also acts like the default home page   
@electronics_routes.route("/electronics/browse", methods=["GET"])
@login_required
def search_electronics():
    search_term = request.args.get("search", "")
    electronics = electronics_service.search_electronics(search_term)
    return render_template("index.html", user=current_user, electronics=electronics)
