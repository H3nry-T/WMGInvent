
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from services.ElectronicsService import ElectronicsService
from repositories.ElectronicsRepository import ElectronicsRepository
from global_db_object import db

import numpy as np
import json

analytics_routes = Blueprint('analytics', __name__)

@analytics_routes.route('/analytics')
@login_required
def show_analytics():
    electronics = ElectronicsService(ElectronicsRepository(db)).get_all_electronics()

    
    prices = [float(e.price) for e in electronics if e.price is not None]
    if not prices:
    
        prices = [0, 10, 20]

    bins = 10
    min_price = min(prices)
    max_price = max(prices)
    if min_price == max_price:
        max_price = min_price + 1 

    counts, bin_edges = np.histogram(prices, bins=bins, range=(min_price, max_price))
    labels_hist = [f'${int(edge)}' for edge in bin_edges[:-1]]

    chart_data_hist = {
        'labels': labels_hist,
        'datasets': [{
            'label': 'Number of Products',
            'data': counts.tolist(),
            'backgroundColor': 'rgba(75, 192, 192, 0.2)',
            'borderColor': 'rgba(75, 192, 192, 1)',
            'borderWidth': 1
        }]
    }

   
    from collections import defaultdict
    stock_by_manuf = defaultdict(int)
    for e in electronics:
        if e.manufacturer:
            stock_by_manuf[e.manufacturer] += e.stock or 0

    bar_labels = list(stock_by_manuf.keys())
    bar_values = list(stock_by_manuf.values())
    chart_data_bar = {
        'labels': bar_labels,
        'datasets': [{
            'label': 'Stock by Manufacturer',
            'data': bar_values,
            'backgroundColor': 'rgba(54, 162, 235, 0.2)',
            'borderColor': 'rgba(54, 162, 235, 1)',
            'borderWidth': 1
        }]
    }

   
    sorted_electronics = sorted(electronics, key=lambda x: x.name)
    line_labels = [e.name for e in sorted_electronics]
    line_prices = [float(e.price) for e in sorted_electronics]
    chart_data_line = {
        'labels': line_labels,
        'datasets': [{
            'label': 'Price (Line)',
            'data': line_prices,
            'fill': False,
            'borderColor': 'rgba(255,99,132,1)',
            'tension': 0.1
        }]
    }

 
    total_stock = sum(e.stock or 0 for e in electronics)

    pie_labels = bar_labels
    pie_values = [stock_by_manuf[m] for m in pie_labels]
    chart_data_pie = {
        'labels': pie_labels,
        'datasets': [{
            'data': pie_values,
            'backgroundColor': [
                'rgba(255, 99, 132, 0.6)',
                'rgba(54, 162, 235, 0.6)',
                'rgba(255, 206, 86, 0.6)',
                'rgba(75, 192, 192, 0.6)',
                'rgba(153, 102, 255, 0.6)',
                'rgba(255, 159, 64, 0.6)'
            ]
        }]
    }

 
    scatter_labels = [e.name for e in electronics]
    scatter_data = []
    for e in electronics:
        scatter_data.append({
            'x': float(e.price or 0),
            'y': e.stock or 0
        })
    chart_data_scatter = {
        'datasets': [{
            'label': 'Price vs Stock',
            'data': scatter_data,
            'backgroundColor': 'rgba(153, 102, 255, 0.6)'
        }]
    }


    return render_template(
        'analytics.html',
        user=current_user,
        chart_data_hist=json.dumps(chart_data_hist),
        chart_data_bar=json.dumps(chart_data_bar),
        chart_data_line=json.dumps(chart_data_line),
        chart_data_pie=json.dumps(chart_data_pie),
        chart_data_scatter=json.dumps(chart_data_scatter),
    )
