from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import or_

# FORMATO: mysql+pymysql://USUARIO:CONTRASEÑA@HOST:PUERTO/NOMBRE_BD
# Template, cambia a los locales.
DB_USER = 'root'
DB_PASS = 'tu_contraseña'
DB_HOST = 'localhost' # 127.0.0.1
DB_PORT = '3306' # 3306
DB_NAME = 'biblioteca_db'

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False) # echo=True para ver el SQL generado
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Libro(Base):
    __tablename__ = 'libros'

    id = Column(Integer, primary_key=True)
    titulo = Column(String(100), nullable=False)
    autor = Column(String(100), nullable=False)
    genero = Column(String(50))
    estado = Column(String(20)) # 'Leído' o 'No leído'

    def __repr__(self):
        return f"<Libro(titulo='{self.titulo}', autor='{self.autor}')>"

class GestorBiblioteca:
    def __init__(self):
        # Crear tablas si no existen
        try:
            Base.metadata.create_all(engine)
        except Exception as e:
            print(f"Error conectando a MariaDB: {e}")
            print("Sugerencia: Revisa que el servicio esté activo y la BD creada.")

    def get_session(self):
        return Session()

    def agregar_libro(self, titulo, autor, genero, estado):
        session = self.get_session()
        nuevo_libro = Libro(titulo=titulo, autor=autor, genero=genero, estado=estado)
        try:
            session.add(nuevo_libro)
            session.commit()
            return True
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error: {e}")
            return False
        finally:
            session.close()

    def listar_libros(self):
        session = self.get_session()
        try:
            # Retorna una lista de OBJETOS Libro, no tuplas
            return session.query(Libro).all()
        finally:
            session.close()

    def buscar_libros(self, termino):
        session = self.get_session()
        try:
            search = f"%{termino}%"
            # Filtro con OR (titulo O autor O genero)
            return session.query(Libro).filter(
                or_(
                    Libro.titulo.like(search),
                    Libro.autor.like(search),
                    Libro.genero.like(search)
                )
            ).all()
        finally:
            session.close()

    def actualizar_libro(self, id_libro, **kwargs):
        session = self.get_session()
        try:
            libro = session.query(Libro).filter_by(id=id_libro).first()
            if libro:
                if kwargs.get('titulo'): libro.titulo = kwargs['titulo']
                if kwargs.get('autor'): libro.autor = kwargs['autor']
                if kwargs.get('genero'): libro.genero = kwargs['genero']
                if kwargs.get('estado'): libro.estado = kwargs['estado']
                session.commit()
                return True
            return False
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error: {e}")
            return False
        finally:
            session.close()

    def eliminar_libro(self, id_libro):
        session = self.get_session()
        try:
            libro = session.query(Libro).filter_by(id=id_libro).first()
            if libro:
                session.delete(libro)
                session.commit()
                return True
            return False
        except SQLAlchemyError:
            session.rollback()
            return False
        finally:
            session.close()