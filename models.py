from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, ForeignKey
from flask_marshmallow import Marshmallow

#Init DB
db=  SQLAlchemy()
#Init ma
ma = Marshmallow()

#PERSONA Clase/Model
class PERSONA(db.Model):
    IdCedula = db.Column(db.String(10), unique=True, primary_key = True, nullable=False)
    apellidos = db.Column(db.String(80), nullable=False)
    nombre = db.Column(db.String(80), nullable=False)
    usuario = db.Column(db.String(20), unique=True, nullable=False)
    contraseña =db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self,IdCedula, apellidos, nombre, usuario, contraseña, email):
        self.IdCedula=IdCedula
        self.apellidos=apellidos
        self.nombre=nombre
        self.usuario=usuario
        self.contraseña = contraseña
        self.email = email

# PERSONA Esquema
class PERSONASchema(ma.Schema):
    class Meta:
        model = PERSONA
        fields = ('IdCedula','apellidos','nombre','usuario','contraseña','email')



#ESTUDIANTE Clase/Model
class ESTUDIANTE(db.Model):
    IdCodigoEstudiante = db.Column(db.Integer, autoincrement=True, primary_key = True, nullable=False)
    IdCedula_ref = db.Column(db.String(10), ForeignKey("PERSONA.IdCedula"), nullable=False)

    def __init__(self, IdCedula_ref):
        self.IdCedula_ref = IdCedula_ref

# ESTUDIANTE Esquema
class ESTUDIANTESchema(ma.Schema):
    class Meta:
        model = ESTUDIANTE
        fields = ('IdCodigoEstudiante','IdCedula_ref')
        persona = ma.Nested(PERSONASchema)



#DOCENTE Clase/Model
class DOCENTE(db.Model):
    IdDocente = db.Column(db.Integer, autoincrement=True, primary_key = True, nullable=False)
    IdCedula_ref = db.Column(db.String(10), ForeignKey("PERSONA.IdCedula"), nullable=False)

    def __init__(self, IdCedula_ref):
        self.IdCedula_ref = IdCedula_ref

# DOCENTE Esquema
class DOCENTESchema(ma.Schema):
    class Meta:
        model = DOCENTE
        fields = ('IdDocente','IdCedula_ref')
        persona = ma.Nested(PERSONASchema)
        titulo = ma.List(ma.Nested('TITULOSchema'))



#TITULO Clase/Model
class TITULO(db.Model):
    IdTitulo = db.Column(db.Integer, autoincrement=True, primary_key = True, nullable=False)
    titulo = db.Column(db.String(40), nullable=False)
    detalletitulo = db.Column(db.String(80), nullable=False)

    def __init__(self, titulo, detalletitulo):
        self.titulo=titulo
        self.detalletitulo=detalletitulo

#TITULO Esquema
class TITULOSchema(ma.Schema):
    class Meta:
        model = TITULO
        fields = ('IdTitulo','titulo','detalletitulo')


#DOCENTETITULO Clase/Model
class DOCENTETITULO(db.Model):
    IdDocenteTitulo = db.Column(db.Integer, autoincrement=True, primary_key = True, nullable=False)
    IdDocente_ref = db.Column(db.Integer,  ForeignKey("DOCENTE.IdDocente"), nullable=False)
    IdTitulo_ref = db.Column(db.Integer, ForeignKey("TITULO.IdTitulo"), nullable=False)
    def __init__(self, IdDocente_ref, IdTitulo_ref):
        self.IdDocente_ref=IdDocente_ref
        self.IdTitulo_ref=IdTitulo_ref

# DOCENTETITULO Esquema
class DOCENTETITULOSchema(ma.Schema):
    class Meta:
        model = DOCENTETITULO
        fields = ('IdDocenteTitulo','IdDocente_ref','IdTitulo_ref')
        docente = ma.Nested(DOCENTESchema)
        titulo = ma.Nested(TITULOSchema)



#PERIODO Clase/Model
class PERIODO(db.Model):
    IdPeriodo = db.Column(db.Integer, autoincrement=True, primary_key = True, nullable=False)
    fechaInicio = db.Column(db.Date, nullable=False)
    fechaFin = db.Column(db.Date, nullable=False)
    detalle = db.Column(db.String(80), unique=True)

    def __init__(self, fechaInicio, fechaFin, detalle):
        self.fechaInicio=fechaInicio
        self.fechaFin=fechaFin
        self.detalle = detalle

#Periodo Esquema
class PERIODOSchema(ma.Schema):
    class Meta:
        model = PERIODO
        fields = ('IdPeriodo','fechaInicio','fechaFin','detalle')



#MATERIA Clase/Model
class MATERIA(db.Model):
    IdMateria = db.Column(db.Integer, autoincrement=True, primary_key = True, nullable=False)
    prerrequisito = db.Column(db.String(30))
    correquisito = db.Column(db.String(30))
    detalle = db.Column(db.String(80))

    def __init__(self, prerrequisito, correquisito, detalle):
        self.prerrequisito=prerrequisito
        self.correquisito=correquisito
        self.detalle = detalle

#MATERIA Esquema
class MATERIASchema(ma.Schema):
    class Meta:
        model = PERIODO
        fields = ('IdMateria','prerrequisito','correquisito','detalle')



#MATRICULA Clase/Model
class MATRICULA(db.Model):
    IdMatricula = db.Column(db.Integer, autoincrement=True, primary_key = True, nullable=False)
    estado = db.Column(db.String(30), nullable=False)
    tipoMatricula = db.Column(db.String(30), nullable=False)
    IdCodigoEstudiante_ref = db.Column(db.Integer, ForeignKey("ESTUDIANTE.IdCodigoEstudiante"), nullable=False)
    IdMateria_ref = db.Column(db.Integer, ForeignKey("MATERIA.IdMateria"), nullable=False)
    IdPeriodo_ref = db.Column(db.Integer, ForeignKey("PERIODO.IdPeriodo"), nullable=False)
    IdDocente_ref = db.Column(db.Integer, ForeignKey("DOCENTE.IdDocente"), nullable=False)

    def __init__(self, estado, tipoMatricula, IdCodigoEstudiante_ref, IdMateria_ref, IdPeriodo_ref, IdDocente_ref):
        self.estado=estado
        self.tipoMatricula=tipoMatricula
        self.IdCodigoEstudiante_ref = IdCodigoEstudiante_ref
        self.IdMateria_ref = IdMateria_ref
        self.IdPeriodo_ref = IdPeriodo_ref
        self.IdDocente_ref = IdDocente_ref


#MATRICULA Esquema
class MATRICULASchema(ma.Schema):
    class Meta:
        model = PERIODO
        fields = ('IdMatricula','estado','tipoMatricula','IdCodigoEstudiante_ref','IdMateria_ref','IdPeriodo_ref','IdDocente_ref')
        estudiante = ma.Nested(ESTUDIANTESchema)
        materia = ma.Nested(MATERIASchema)
        periodo = ma.Nested(PERIODOSchema)
        docente = ma.Nested(DOCENTESchema)



#NOTAS Clase/Model
class NOTAS(db.Model):
    IdNotas = db.Column(db.Integer, autoincrement=True, primary_key = True, nullable=False)
    detalle = db.Column(db.String(80), nullable=False)
    calificacion = db.Column(db.Float, nullable=False)
    IdMatricula_ref = db.Column(db.Integer, ForeignKey("MATRICULA.IdMatricula"), nullable=False)

    def __init__(self, detalle, calificacion, IdMatricula_ref):
        self.detalle=detalle
        self.calificacion=calificacion
        self.IdMatricula_ref = IdMatricula_ref

#NOTAS Esquema
class NOTASSchema(ma.Schema):
    class Meta:
        model = NOTAS
        fields = ('IdNotas','detalle','calificacion','IdMatricula_ref')
        matricula = ma.Nested(MATERIASchema)



#PAGOS Clase/Model
class PAGOS(db.Model):
    IdPagos = db.Column(db.Integer, autoincrement=True, primary_key = True, nullable=False)
    detalle = db.Column(db.String(80), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    IdMatricula_ref = db.Column(db.Integer, ForeignKey("MATRICULA.IdMatricula"), nullable=False)

    def __init__(self, detalle, monto, IdMatricula_ref):
        self.detalle=detalle
        self.monto=monto
        self.IdMatricula_ref = IdMatricula_ref

#PAGOS Esquema
class PAGOSSchema(ma.Schema):
    class Meta:
        model = PAGOS
        fields = ('IdPagos','detalle','monto','IdMatricula_ref')
        matricula = ma.Nested(MATERIASchema)





