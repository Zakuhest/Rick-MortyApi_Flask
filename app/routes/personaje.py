from flask import Blueprint, render_template, redirect, url_for, request
from app.models.personajes import Personaje, api
from app.db.db import db

personajes_ruta = Blueprint('personajes', __name__)

@personajes_ruta.route('/')
def index():
    condicion = [{"$sort": {"id": -1}}]
    personajes = db.personajes.aggregate(condicion)
    return render_template('index.html', personajes=personajes)

@personajes_ruta.route('/404')
def notfound():
    return render_template('404.html')

@personajes_ruta.route('/search', methods=['POST'])
def busqueda():
    if request.form.get('id') == "" or request.form.get('id')==None: 
        id = 0 
    else:
        id = request.form.get('id')
    
    name = request.form.get('name')
    origin = request.form.get('origin')
    location = request.form.get('location')
    
    lista = [id,name,origin,location]
    contador = 0

    for n in lista:
        if n == "" or n == None or n == 0:
            contador += 1
        
    if contador == 4:
        return redirect('/')
    
    docs = db.personajes.find(
        {'$or':
        [
            {'id': int(id)},   # type: ignore
            {'name':name},
            {'origin.name':origin},
            {'location.name':location}
        ]},
        )
    contar = len(list(docs))

    search = db.personajes.find(
        {'$or':
        [
            {'id': int(id)},   # type: ignore
            {'name':name},
            {'origin.name':origin},
            {'location.name':location}
        ]},
        )
    if contar < 1:
        return redirect(url_for('personajes.notfound'))

    return render_template('index_busqueda.html', buscados=search)

@personajes_ruta.route('/profile/<int:id>', methods=['GET','POST'])
def perfil(id):
    
    perfil = db.personajes.find_one({'id':id})
    return render_template('profile.html', profile=perfil)

@personajes_ruta.route('/add/', methods=['GET','POST'])
def add_personajes():
    paginas = 42
    obj = api()
    for i in range(1,paginas+1):
        json = obj.request_api(n_page=str(i))
        for j in range(len(json['results'])):
            db.personajes.insert_one(json['results'][j])

    return redirect(url_for('personajes.index'))


