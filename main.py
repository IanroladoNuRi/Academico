from flask import Flask, request, jsonify

from Resources.Titulo import *
from models import *
#from models import db, PERSONA, ESTUDIANTE, DOCENTE, TITULO, DOCENTETITULO, PERIODO, MATERIA, MATRICULA, NOTAS, PAGOS
#from models import PERSONASchema, ESTUDIANTESchema, DOCENTESchema, TITULOSchema, DOCENTETITULOSchema, PERIODOSchema, MATERIASchema, MATRICULASchema, NOTASSchema, PAGOSSchema

from config import DevelopmentConfig


#init main
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/Prueba'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False


#Init Esquema
persona_schema=PERSONASchema()
estudiante_schema=ESTUDIANTESchema()
titulo_schema=TITULOSchema()
docente_schema=DOCENTESchema()
docentetitulo_schema=DOCENTETITULOSchema()
periodo_schema=PERIODOSchema()
materia_schema=MATERIASchema()
matricula_schema=MATRICULASchema()
nota_schema=NOTASSchema()
pago_schema=PAGOSSchema()
personas_schema=PERSONASchema(many = True)
estudiantes_schema=ESTUDIANTESchema(many = True)
titulos_schema=TITULOSchema(many = True)
docentes_schema=DOCENTESchema(many = True)
docentetitulos_schema=DOCENTETITULOSchema(many = True)
periodos_schema=PERIODOSchema(many = True)
materias_schema=MATERIASchema(many = True)
matriculas_schema=MATRICULASchema(many = True)
notas_schema=NOTASSchema(many = True)
pagos_schema=PAGOSSchema(many = True)

'''
#Crear estudiante
@app.route('/ESTUDIANTE', methods=['POST'])
def add_ESTUDIANTE():
    IdCedula = request.json['IdCedula']
    apellidos = request.json['apellidos']
    nombre = request.json['nombre']
    usuario = request.json['usuario']
    contraseña = request.json['contraseña']
    email = request.json['email']

    IdCedula_ref = IdCedula

    nuevo_persona = PERSONA(IdCedula, apellidos, nombre, usuario, contraseña, email)
    nuevo_estudiante= ESTUDIANTE(IdCedula_ref)
    db.session.add(nuevo_persona)
    db.session.commit()
    db.session.add(nuevo_estudiante)
    db.session.commit()

    return estudiante_schema.jsonify(nuevo_estudiante)



#GET all estudiantes
@app.route('/ESTUDIANTE', methods=['GET'])
def get_ESTUDIANTES():
    all_estudiantes = ESTUDIANTE.query.all()
    estudiantes_serializados = estudiantes_schema.dump(all_estudiantes)
    lista_estudiantes = []
    for x in estudiantes_serializados:
        persona = PERSONA.query.get(x["IdCedula_ref"])
        persona_serializada = persona_schema.dump(persona)
        estudiante = {
            "IdCedula" : persona_serializada["IdCedula"],
            "apellidos" : persona_serializada["apellidos"],
            "nombre" : persona_serializada["nombre"],
            "usuario" : persona_serializada["usuario"],
            "contraseña": persona_serializada["contraseña"],
            "email": persona_serializada["email"],
            "estudiante" : {
                "IdCodigoEstudiante" : x["IdCodigoEstudiante"]
            }
        }
        lista_estudiantes.append(estudiante)


    return jsonify(lista_estudiantes)



#GET single estudiante
@app.route('/ESTUDIANTE/<id>', methods=['GET'])
def get_ESTUDIANTE(id):
    estudiante_query = ESTUDIANTE.query.get(id)
    estudiante_serializado = estudiante_schema.dump(estudiante_query)
    persona_query = PERSONA.query.get(estudiante_serializado["IdCedula_ref"])
    persona_serializada = persona_schema.dump(persona_query)
    persona = {
        "IdCedula": persona_serializada["IdCedula"],
        "apellidos": persona_serializada["apellidos"],
        "nombre": persona_serializada["nombre"],
        "usuario": persona_serializada["usuario"],
        "contraseña": persona_serializada["contraseña"],
        "email": persona_serializada["email"],
        "estudiante": {
            "IdCodigoEstudiante": estudiante_serializado["IdCodigoEstudiante"]
        }
    }
    return jsonify(persona)



#Update estudiante
@app.route('/ESTUDIANTE/<id>', methods=['PUT'])
def update_ESTUDIANTE(id):
    estuditante_query = ESTUDIANTE.query.get(id)

    IdCedula = request.json['IdCedula']
    apellidos = request.json['apellidos']
    nombre = request.json['nombre']
    usuario = request.json['usuario']
    contraseña = request.json['contraseña']
    email = request.json['email']

    persona_query = PERSONA.query.get(IdCedula)

    persona_query.IdCedula = IdCedula
    persona_query.apellidos = apellidos
    persona_query.nombre = nombre
    persona_query.usuario = usuario
    persona_query.contraseña = contraseña
    persona_query.email = email

    db.session.commit()

    return persona_schema.jsonify(persona_query)



#DELETE estudiante
@app.route('/ESTUDIANTE/<id>', methods=['DELETE'])
def delete_ESTUDIANTE(id):
    estudiante_query = ESTUDIANTE.query.get(id)
    estudiante_serializado = estudiante_schema.dump(estudiante_query)
    persona_query = PERSONA.query.get(estudiante_serializado["IdCedula_ref"])

    db.session.delete(estudiante_query)
    db.session.commit()
    db.session.delete(persona_query)
    db.session.commit()


    return persona_schema.jsonify(persona_query)



#Crear docente
@app.route('/DOCENTE', methods=['POST'])
def add_DOCENTE():
    IdCedula = request.json['IdCedula']
    apellidos = request.json['apellidos']
    nombre = request.json['nombre']
    usuario = request.json['usuario']
    contraseña = request.json['contraseña']
    email = request.json['email']

    IdCedula_ref = IdCedula

    titulo = request.json['titulos']

    nuevo_persona = PERSONA(IdCedula, apellidos, nombre, usuario, contraseña, email)
    nuevo_docente= DOCENTE(IdCedula_ref)
    db.session.add(nuevo_persona)
    db.session.commit()
    db.session.add(nuevo_docente)
    db.session.commit()
    for x in titulo:
        nuevo_docente_titulo = DOCENTETITULO(nuevo_docente.IdDocente,x["IdTitulo"])
        db.session.add(nuevo_docente_titulo)
        db.session.commit()

    return docente_schema.jsonify(nuevo_docente)



#GET all docentes
@app.route('/DOCENTE', methods=['GET'])
def get_DOCENTES():
    all_docentes = DOCENTE.query.all()
    docentes_serializados = docentes_schema.dump(all_docentes)
    lista_docentes = []
    for x in docentes_serializados:
        persona_query = PERSONA.query.get(x["IdCedula_ref"])
        persona_serializada = persona_schema.dump(persona_query)
        persona = {
            'IdCedula' : persona_serializada["IdCedula"],
            'apellidos' : persona_serializada["apellidos"],
            'nombre' : persona_serializada["nombre"],
            'usuario' : persona_serializada["usuario"],
            'contraseña': persona_serializada["contraseña"],
            'email': persona_serializada["email"],
            'docente' : {
                "IdDocente" : x["IdDocente"]
            },
            'titulos' : []
        }
        titulos_consulta = DOCENTETITULO.query.filter_by(IdDocente_ref=x["IdDocente"]).all()
        titulos_consulta_serializado = docentetitulos_schema.dump(titulos_consulta)
        for y in titulos_consulta_serializado:
            persona['titulos'].append({"IdTitulo":y["IdTitulo_ref"]})

        lista_docentes.append(persona)


    return jsonify(lista_docentes)



#GET single docente
@app.route('/DOCENTE/<id>', methods=['GET'])
def get_DOCENTE(id):
    docente_query = DOCENTE.query.get(id)
    docente_serializado = docente_schema.dump(docente_query)
    persona_query = PERSONA.query.get(docente_serializado["IdCedula_ref"])
    persona_serializada = persona_schema.dump(persona_query)
    persona = {
        "IdCedula": persona_serializada["IdCedula"],
        "apellidos": persona_serializada["apellidos"],
        "nombre": persona_serializada["nombre"],
        "usuario": persona_serializada["usuario"],
        "contraseña": persona_serializada["contraseña"],
        "email": persona_serializada["email"],
        'DOCENTE' : {
                "IdDocente" : docente_serializado["IdDocente"]
            },
            'titulos' : []
        }

    titulos_consulta = DOCENTETITULO.query.filter_by(IdDocente_ref=docente_serializado["IdDocente"]).all()
    titulos_consulta_serializado = docentetitulos_schema.dump(titulos_consulta)
    for y in titulos_consulta_serializado:
        persona['titulos'].append({"IdTitulo": y["IdTitulo_ref"]})

    return jsonify(persona)



#Update docente
@app.route('/DOCENTE/<id>', methods=['PUT'])
def update_DOCENTE(id):
    docente_query = DOCENTE.query.get(id)
    docente_serializado = docente_schema.dump(docente_query)

    persona_query = PERSONA.query.get(docente_serializado["IdCedula_ref"])

    IdCedula = request.json['IdCedula']
    apellidos = request.json['apellidos']
    nombre = request.json['nombre']
    usuario = request.json['usuario']
    contraseña = request.json['contraseña']
    email = request.json['email']
    IdCedula_ref = IdCedula

    persona_query.IdCedula = IdCedula
    persona_query.apellidos = apellidos
    persona_query.nombre = nombre
    persona_query.usuario = usuario
    persona_query.contraseña = contraseña
    persona_query.email = email

    db.session.commit()

    return docente_schema.jsonify(persona_query)



#DELETE docente
@app.route('/DOCENTE/<id>', methods=['DELETE'])
def delete_DOCENTE(id):
    docente_query = DOCENTE.query.get(id)
    docente_serializado = docente_schema.dump(docente_query)
    persona_query = PERSONA.query.get(docente_serializado["IdCedula_ref"])

    db.session.delete(docente_query)
    db.session.commit()
    db.session.delete(persona_query)
    db.session.commit()


    return persona_schema.jsonify(persona_query)



#Update docentetitulo
@app.route('/DOCENTETITULO/<id>', methods=['PUT'])
def update_DOCENTETITULO(id):
    docentetitulo_query = DOCENTETITULO.query.get(id)

    IdTitulo_ref = request.json['IdTitulo_ref']

    docentetitulo_query.IdTitulo_ref =IdTitulo_ref

    db.session.commit()

    return docentetitulo_schema.jsonify(docentetitulo_query)



#DELETE docentetitulo
@app.route('/DOCENTETITULO/<id>', methods=['DELETE'])
def delete_DOCENTETITULO(id):
    docentetitulo_query = DOCENTETITULO.query.get(id)

    db.session.delete(docentetitulo_query)
    db.session.commit()

    return docentetitulo_schema.jsonify(docentetitulo_query)



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



#Crear periodo
@app.route('/PERIODO', methods=['POST'])
def add_PERIODO():
    fechaInicio = request.json['fechaInicio']
    fechaFin = request.json['fechaFin']
    detalle = request.json['detalle']

    nuevo_periodo= PERIODO(fechaInicio,fechaFin,detalle)
    db.session.add(nuevo_periodo)
    db.session.commit()

    return periodo_schema.jsonify(nuevo_periodo)



#GET all periodos
@app.route('/PERIODO', methods=['GET'])
def get_PERIODOS():
    all_periodos = PERIODO.query.all()
    result = periodos_schema.dump(all_periodos)
    return jsonify(result)



#GET single periodo
@app.route('/PERIODO/<id>', methods=['GET'])
def get_PERIODO(id):
    periodo_query = PERIODO.query.get(id)
    return periodo_schema.jsonify(periodo_query)



#Update periodo
@app.route('/PERIODO/<id>', methods=['PUT'])
def update_PERIODO(id):
    periodo_query = PERIODO.query.get(id)

    fechaInicio = request.json['fechaInicio']
    fechaFin = request.json['fechaFin']
    detalle = request.json['detalle']

    periodo_query.fechaInicio =fechaInicio
    periodo_query.fechaFin = fechaFin
    periodo_query.detalle = detalle


    db.session.commit()

    return periodo_schema.jsonify(periodo_query)



#DELTE periodo
@app.route('/PERIODO/<id>', methods=['DELETE'])
def delete_PERIODO(id):
    periodo_query = PERIODO.query.get(id)
    db.session.delete(periodo_query)
    db.session.commit()

    return periodo_schema.jsonify(periodo_query)



#crear materia
@app.route('/MATERIA', methods=['POST'])
def add_MATERIA():
    prerrequisito = request.json['prerrequisito']
    correquisito = request.json['correquisito']
    detalle = request.json['detalle']

    nuevo_materia= MATERIA(prerrequisito,correquisito,detalle)
    db.session.add(nuevo_materia)
    db.session.commit()

    return materia_schema.jsonify(nuevo_materia)



#GET all materia
@app.route('/MATERIA', methods=['GET'])
def get_MATERIAS():
    all_materias = MATERIA.query.all()
    result = materias_schema.dump(all_materias)
    return jsonify(result)



#GET single materia
@app.route('/MATERIA/<id>', methods=['GET'])
def get_MATERIA(id):
    materia_query = MATERIA.query.get(id)
    return materia_schema.jsonify(materia_query)



#Update materia
@app.route('/MATERIA/<id>', methods=['PUT'])
def update_MATERIA(id):
    materia_query = MATERIA.query.get(id)

    prerrequisito = request.json['prerrequisito']
    correquisito = request.json['correquisito']
    detalle = request.json['detalle']

    materia_query.prerrequisito = prerrequisito
    materia_query.correquisito = correquisito
    materia_query.detalle = detalle

    db.session.commit()

    return materia_schema.jsonify(materia_query)



#DELETE materia
@app.route('/MATERIA/<id>', methods=['DELETE'])
def delete_MATERIA(id):
    materia_query = MATERIA.query.get(id)
    db.session.delete(materia_query)
    db.session.commit()
    return materia_schema.jsonify(materia_query)



#crear matricula
@app.route('/MATRICULA', methods=['POST'])
def add_MATRICULA():
    estado = request.json['estado']
    tipoMatricula = request.json['tipoMatricula']
    IdCodigoEstudiante_ref = request.json['IdCodigoEstudiante_ref']
    IdMateria_ref = request.json['IdMateria_ref']
    IdPeriodo_ref = request.json['IdPeriodo_ref']
    IdDocente_ref = request.json['IdDocente_ref']

    nuevo_matricula= MATRICULA(estado,tipoMatricula,IdCodigoEstudiante_ref,IdMateria_ref,IdPeriodo_ref,IdDocente_ref)
    db.session.add(nuevo_matricula)
    db.session.commit()

    return matricula_schema.jsonify(nuevo_matricula)



#GET all matricula
@app.route('/MATRICULA', methods=['GET'])
def get_MATRICULAS():
    all_matriculas = MATRICULA.query.all()
    result = matriculas_schema.dump(all_matriculas)
    return jsonify(result)



#GET single matricula
@app.route('/MATRICULA/<id>', methods=['GET'])
def get_MATRICULA(id):
    matricula_query = MATRICULA.query.get(id)
    return matricula_schema.jsonify(matricula_query)



#UPDATE matricula
@app.route('/MATRICULA/<id>', methods=['PUT'])
def update_MATRICULA(id):
    matricula_query = MATRICULA.query.get(id)

    estado = request.json['estado']
    tipoMatricula = request.json['tipoMatricula']

    matricula_query.estado = estado
    matricula_query.tipoMatricula = tipoMatricula

    db.session.commit()

    return matricula_schema.jsonify(matricula_query)



# DELETE matricula
@app.route('/MATRICULA/<id>', methods=['DELETE'])
def delete_MATRICULA(id):
    matricula_query = MATRICULA.query.get(id)
    db.session.delete(matricula_query)
    db.session.commit()

    return matricula_schema.jsonify(matricula_query)



#crear nota
@app.route('/NOTA', methods=['POST'])
def add_NOTA():
    detalle = request.json['detalle']
    calificacion = request.json['calificacion']
    IdMatricula_ref = request.json['IdMatricula_ref']

    nuevo_nota= NOTAS(detalle,calificacion,IdMatricula_ref)
    db.session.add(nuevo_nota)
    db.session.commit()

    return nota_schema.jsonify(nuevo_nota)



#GET all notas
@app.route('/NOTA', methods=['GET'])
def get_NOTAS():
    all_notas = NOTAS.query.all()
    result = notas_schema.dump(all_notas)
    return jsonify(result)



#GET single nota
@app.route('/NOTA/<id>', methods=['GET'])
def get_NOTA(id):
    nota_query = NOTAS.query.get(id)
    return nota_schema.jsonify(nota_query)



#Update nota
@app.route('/NOTA/<id>', methods=['PUT'])
def update_NOTA(id):
    nota_query = NOTAS.query.get(id)

    detalle = request.json['detalle']
    calificacion = request.json['calificacion']
    IdMatricula_ref = request.json['IdMatricula_ref']

    nota_query.detalle = detalle
    nota_query.calificacion = calificacion
    nota_query.IdMatricula_ref = IdMatricula_ref

    db.session.commit()

    return nota_schema.jsonify(nota_query)



#DELETE nota
@app.route('/NOTA/<id>', methods=['DELETE'])
def delete_NOTA(id):
    nota_query = NOTAS.query.get(id)
    db.session.delete(nota_query)
    db.session.commit()

    return nota_schema.jsonify(nota_query)



#crear pago
@app.route('/PAGO', methods=['POST'])
def add_PAGO():
    detalle = request.json['detalle']
    monto = request.json['monto']
    IdMatricula_ref = request.json['IdMatricula_ref']

    nuevo_pago= PAGOS(detalle,monto,IdMatricula_ref)
    db.session.add(nuevo_pago)
    db.session.commit()

    return pago_schema.jsonify(nuevo_pago)



#GET all pagos
@app.route('/PAGO', methods=['GET'])
def get_PAGOS():
    all_pagos = PAGOS.query.all()
    result = pagos_schema.dump(all_pagos)
    return jsonify(result)



#GET single pago
@app.route('/PAGO/<id>', methods=['GET'])
def get_PAGO(id):
    pago_query = PAGOS.query.get(id)
    return pago_schema.jsonify(pago_query)



#Update pago
@app.route('/PAGO/<id>', methods=['PUT'])
def update_PAGO(id):
    pago_query = PAGOS.query.get(id)

    detalle = request.json['detalle']
    monto = request.json['monto']
    IdMatricula_ref = request.json['IdMatricula_ref']

    pago_query.detalle = detalle
    pago_query.monto = monto
    pago_query.IdMatricula_ref = IdMatricula_ref

    db.session.commit()

    return pago_schema.jsonify(pago_query)



#GET single pago
@app.route('/PAGO/<id>', methods=['DELETE'])
def delete_PAGO(id):
    pago_query = PAGOS.query.get(id)
    db.session.delete(pago_query)
    db.session.commit()

    return pago_schema.jsonify(pago_query)


'''
#rest.add_resource(Titulo,"/venv/Resources/Titulo")
#Run Server
if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)
