import time

import psycopg2
from env_var import getVar
from typing import NoReturn, Any
from database.queries import Queries


class DatabaseConnection:
    def __init__(self):
        self.host = getVar('DB_HOST')
        self.port = getVar('DB_PORT')
        self.dbName = getVar('DB_NAME')
        self.user = getVar('DB_USER')
        self.password = getVar('DB_PASSWORD')
        self.queries = Queries()

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
            print(error, statement)
            connection.rollback()

        finally:
            time.sleep(0.5)
            cursor.close()
            connection.close()

    def __perform__update_query__(self, statement: str):
        connection = self.connection()
        cursor = connection.cursor()

        try:
            cursor.execute(statement)
            connection.commit()

        except:
            connection.rollback()

        finally:
            time.sleep(0.5)
            cursor.close()
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
            cursor.close()
            return resultQuery