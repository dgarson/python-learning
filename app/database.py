from app import app
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

# engine = create_engine(app.config.get("SQLALCHEMY_DATABASE_URI"), convert_unicode=True, echo=True)
# db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
engine = db.engine
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
metadata = db.metadata
# metadata = MetaData(bind=engine)

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import app.models
    # metadata.create_all(bind=engine)
    # db.create_all(bind=engine, app=app)
    db.drop_all()
    db.create_all()
    print("created tables")