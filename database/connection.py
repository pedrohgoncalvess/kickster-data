from sqlalchemy.orm import sessionmaker
from env_var import getVar
from sqlalchemy import create_engine


class DatabaseConnection:
    def __init__(self):
        self.host = getVar('DB_HOST')
        self.port = getVar('DB_PORT')
        self.dbName = getVar('DB_NAME')
        self.user = getVar('DB_USER')
        self.password = getVar('DB_PASSWORD')
        self.__engine__ = create_engine(
            f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbName}"
        )

    def insert_object(self, new_object):
        Session = sessionmaker(self.__engine__)
        session = Session()
        try:
            session.add(new_object)
            session.commit()
            session.close()
            return True
        except Exception as error:
            print(error)
            session.rollback()
            session.close()
            return False


    def query_objects(self, statement):
        Session = sessionmaker(self.__engine__)
        session = Session()
        try:
            results = session.execute(statement)
            return results.fetchall()
        except Exception as error:
            print(error)

        finally:
            session.close()

    def update_objects(self, statement):
        Session = sessionmaker(self.__engine__)
        session = Session()
        try:
            session.execute(statement)
            session.commit()
            return True
        except Exception as error:
            print(error)
            session.close()
            return False



db_connection = DatabaseConnection()
