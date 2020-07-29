import os
from flask import Flask
'''
#Crear titulo
@app.route('/TITULO', methods=['POST'])
def add_TITULO():
    titulo = request.json['titulo']
    detalletitulo = request.json['detalletitulo']

    nuevo_titulo= TITULO(titulo,detalletitulo)
    db.session.add(nuevo_titulo)
    db.session.commit()

    return titulo_schema.jsonify(nuevo_titulo)



#GET all titulos
@app.route('/TITULO', methods=['GET'])
def get_TITULOS():
    all_titulos = TITULO.query.all()
    result = titulos_schema.dump(all_titulos)
    return jsonify(result)



#GET single titulo
@app.route('/TITULO/<id>', methods=['GET'])
def get_TITULO(id):
    titulo = TITULO.query.get(id)
    return titulo_schema.jsonify(titulo)



#Update titulo
@app.route('/TITULO/<id>', methods=['PUT'])
def update_TITULO(id):
    titulo_query = TITULO.query.get(id)


    titulo = request.json['titulo']
    detalletitulo = request.json['detalletitulo']

    titulo_query.titulo = titulo
    titulo_query.detalletitulo = detalletitulo

    db.session.commit()

    return titulo_schema.jsonify(titulo_query)



#DELETE titulo
@app.route('/TITULO/<id>', methods=['DELETE'])
def delete_TITULO(id):
    titulo_query = TITULO.query.get(id)
    db.session.delete(titulo_query)
    db.session.commit()

    return titulo_schema.jsonify(titulo_query)

'''