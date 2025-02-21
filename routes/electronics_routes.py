from flask import Blueprint, request, render_template, flash, redirect, url_for
from services.ElectronicsService import ElectronicsService
from repositories.ElectronicsRepository import ElectronicsRepository
from global_db_object import db
from flask_login import login_required, current_user
from forms.electronics_form import ElectronicForm
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

@electronics_routes.route("/electronics/<int:id>", methods=["GET"])
@login_required
def get_electronic(id):
    electronic = electronics_service.get_electronics_by_id(id)
    return render_template("product_detail.html", user=current_user, product=electronic)

@electronics_routes.route("/electronics/<int:id>/update", methods=["POST", "GET"])
@login_required
def edit_electronic(id):
    electronic = electronics_service.get_electronics_by_id(id)
    form = ElectronicForm(request.form, obj=electronic)
    
    if request.method == "GET": 
        return render_template("edit_product.html", user=current_user, product=electronic, form=form)
    
    if form.validate_on_submit():
        if electronic:
            form.populate_obj(electronic)
            electronics_service.update_electronic(electronic)
            flash("Product updated successfully", "success")
            return redirect(url_for("electronics_routes.get_electronic", id=id))
        else:
            flash("Product not found, so cannot update", "danger")

    return render_template("product_detail.html", user=current_user, product=electronic, form=form)
