import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate
from sqlalchemy import update
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Vuelos


@app.route('/')
def Index():
    try:
        data = Vuelos.query.all()
        return render_template('index.html', vuelos = data)
    except Exception as e:
        return(str(e))
    
    

@app.route('/agregar', methods=['POST'])
def agregar():
    if request.method == 'POST':
        new_vuelo = Vuelos(vuelo=request.form['vuelo'], compañia = request.form['compañia'],
        hora = request.form['hora'])
        db.session.add(new_vuelo)
        db.session.commit()
        flash('Vuelo agregado correctamente')
    return redirect(url_for('Index'))
        

@app.route('/editar/<id>')
def obtener_vuelo(id):
    data=Vuelos.query.filter_by(id=int(id)).first()
    return render_template('editar-vuelo.html', vuelo = data)


@app.route('/modificar/<id>', methods = ['POST'])
def modificar(id):
    if request.method == 'POST':
        data=Vuelos.query.filter_by(id=int(id)).first()
        data.vuelo = request.form['vuelo']
        data.compañia = request.form['compañia']
        data.hora = request.form['hora']
        db.session.commit()
        flash('Vuelo modificado correctamente')
        return redirect(url_for('Index'))


@app.route('/borrar/<string:id>')
def borrar(id):
    Vuelos.query.filter_by(id=int(id)).delete()
    db.session.commit()
    flash('Vuelo eliminado correctamente')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port = 5000, debug = True)
