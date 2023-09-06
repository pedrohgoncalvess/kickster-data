import psycopg2
from env_var import getVar
from typing import NoReturn, Any


class DatabaseConnection:
    def __init__(self):
        self.host = getVar('DB_HOST')
        self.port = getVar('DB_PORT')
        self.dbName = getVar('DB_NAME')
        self.user = getVar('DB_USER')
        self.password = getVar('DB_PASSWORD')

    def connection(self):
        return psycopg2.connect(
            dbname=self.dbName,
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password
        )

    def __perform_insert_query__(self, statement: str) -> NoReturn:

        connection = self.connection()
        cursor = connection.cursor()

        try:
            cursor.execute(statement)
            connection.commit()

        except Exception as error:
            print(error)
            connection.rollback()

        finally:
            connection.close()

    def __perform_consult_query__(self, statement: str) -> Any:
        global resultQuery
        connection = self.connection()
        cursor = connection.cursor()

        try:
            cursor.execute(statement)
            resultQuery = cursor.fetchall()
        except:
            connection.rollback()
            resultQuery = None
        finally:
            connection.close()
            return resultQuery

    def __create_database__(self) -> NoReturn:
        with open(r'../build.sql') as buildDb:
            script: str = buildDb.read()
            self.connection.cursor().execute(script)
            self.connection.commit()
            self.connection.close()

# DatabaseConnection().__create_database__()
