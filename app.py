from flask import Flask, render_template, request, redirect, url_for
from models import db, Order

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Indicador para controlar si la inicialización ya se ha realizado
app_has_run_before = False

@app.before_request
def initialize():
    global app_has_run_before
    if not app_has_run_before:
        db.create_all()
        app_has_run_before = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/empresa')
def empresa():
    orders = Order.query.all()
    return render_template('empresa.html', orders=orders)

@app.route('/create_order', methods=['POST'])
def create_order():
    task = request.form['task']
    ip_address = request.remote_addr
    new_order = Order(task=task, ip_address=ip_address, status='Pendiente')
    db.session.add(new_order)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update_order/<int:id>', methods=['POST'])
def update_order(id):
    order = Order.query.get(id)
    order.status = request.form['status']
    db.session.commit()
    return redirect(url_for('empresa'))

if __name__ == '__main__':
    app.run(debug=True)
