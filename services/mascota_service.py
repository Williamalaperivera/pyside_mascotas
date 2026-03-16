from database import Session
from models.mascota import Mascota
from sqlalchemy import func


class MascotaService:

    @staticmethod
    def obtener_todos():
        session = Session()
        try:
            mascotas = session.query(Mascota).all()
            return mascotas
        finally:
            session.close()

    @staticmethod
    def obtener_por_id(mascota_id):
        session = Session()
        try:
            mascota = session.query(Mascota).filter(Mascota.id == mascota_id).first()
            return mascota
        finally:
            session.close()

    @staticmethod
    def crear(nombre, especie, peso):
        session = Session()

        try:
            nueva = Mascota(
                nombre=nombre,
                especie=especie,
                peso=peso
            )

            session.add(nueva)
            session.commit()

            return True

        except Exception as e:
            print(e)
            session.rollback()
            return False

        finally:
            session.close()

    @staticmethod
    def actualizar(mascota_id, nombre, especie, peso):

        session = Session()

        try:

            mascota = session.query(Mascota).filter(Mascota.id == mascota_id).first()

            if mascota:

                mascota.nombre = nombre
                mascota.especie = especie
                mascota.peso = peso

                session.commit()
                return True

            return False

        except Exception as e:

            print(e)
            session.rollback()
            return False

        finally:
            session.close()

    @staticmethod
    def eliminar(mascota_id):

        session = Session()

        try:

            mascota = session.query(Mascota).filter(Mascota.id == mascota_id).first()

            if mascota:
                session.delete(mascota)
                session.commit()
                return True

            return False

        except Exception as e:

            print(e)
            session.rollback()
            return False

        finally:
            session.close()

    @staticmethod
    def obtener_estadisticas():

        session = Session()

        try:

            total = session.query(func.count(Mascota.id)).scalar()

            promedio = session.query(func.avg(Mascota.peso)).scalar()

            especies = session.query(
                func.count(func.distinct(Mascota.especie))
            ).scalar()

            if promedio is None:
                promedio = 0

            return {
                "total": total,
                "promedio_peso": round(promedio, 2),
                "especies": especies
            }

        finally:
            session.close()

    @staticmethod
    def obtener_especies():

        session = Session()

        try:

            datos = session.query(
                Mascota.especie,
                func.count(Mascota.id)
            ).group_by(Mascota.especie).all()

            return datos

        finally:
            session.close()