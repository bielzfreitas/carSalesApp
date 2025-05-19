from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    cars = [
        {'modelo': 'Civic', 'marca': 'Honda', 'ano': 2018, 'preco': 'R$ 60.000'},
        {'modelo': 'Corolla', 'marca': 'Toyota', 'ano': 2019, 'preco': 'R$ 70.000'},
        {'modelo': 'Gol', 'marca': 'Volkswagen', 'ano': 2017, 'preco': 'R$ 45.000'}
    ]
    return render_template('carSales.html', cars=cars)