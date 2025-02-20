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
    min_price = request.args.get("min_price", None)
    max_price = request.args.get("max_price", None)
    stock_status = request.args.get("stock_status", None)
    sort_by = request.args.get("sort_by", None)

    if min_price: 
        min_price = float(min_price)
    else: 
        min_price = None
        
    if max_price: 
        max_price = float(max_price)
    else: 
        max_price = None

    electronics = electronics_service.search_electronics(
        search_term, 
        min_price, 
        max_price,
        stock_status,
        sort_by
    )
    return render_template(
        "index.html", 
        user=current_user, 
        electronics=electronics,
        current_sort=sort_by
    )
