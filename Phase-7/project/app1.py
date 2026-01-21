from flask_sqlalchemy import sqlalchemy

db=sqlalchemy()

db.init_app(app)