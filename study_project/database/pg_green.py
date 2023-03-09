import dotenv
from psycopg2 import OperationalError, connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os

def create_connection(db_name, db_user, db_password, db_host, db_port, prnt=False):
    """
    Службова функція для відкриття доступу до БД
    :param db_name: назва БД
    :param db_user: зареєстроване ім'я користувача
    :param db_password: пароль
    :param db_host: ім'я хоста
    :param db_port: порт СУБД (5432)
    :param prnt: виведення логу
    :return: psycopg2.connection або None
    """
    try:
        if prnt:print(
                f"Try connection to db_name={db_name} user={db_user} pass={db_password} host={db_host} port={db_port} ...")
        if db_name == "":
            connection = connect(user=db_user, password=db_password, host=db_host, port=db_port)
            if (prnt):
                print("Connection to PostgreSQL DB successful")
        else:
            print(f"Connection to Database {db_name}...")
            connection = connect(user=db_user, password=db_password, host=db_host, port=db_port,
                                          database=db_name)
            if (prnt):
                print(f"Connection to Database {db_name} successful")
    except OperationalError as e:
        if (prnt):
            print(f"The error '{e}' occurred")
        connection = None
    return connection


class PDatabaseConnect:
    """
    Class for DataBase access
    Конструктор считує дані для ідентифікації з файлу .env
    Якщо файлу немає, формуються параметри за замовчуванням і створюється файл .env
    """
    def __init__(self):
        if dotenv.load_dotenv():
            self.__port = os.environ["DB_PORT"]
            self.__db_name = os.environ["DB_NAME"]
            self.__host = os.environ["PG_HOST"]
            self.__user = os.environ["PG_USER"]
            try:
                self.__password = os.environ["PG_PASSWORD"]
            except:
                self.__password = "postgres"
            try:
                self.__server = os.environ["PG_SERVER"]
            except:
                self.__server = "postgres"
        else:
            self.setting(db_name='postgres', password='postgres')

    def setting(self, user='postgres', host='localhost', port='5432', password="", server='postgres', db_name=""):
        self.__host = host
        self.__port = port
        self.__server = server
        self.__user = user
        self.__password = password
        self.__db_name = db_name

        dotenv_path = ".env"
        dotenv.set_key(dotenv_path, "DB_HOST", self.__host)
        dotenv.set_key(dotenv_path, "DB_PORT", self.__port)
        dotenv.set_key(dotenv_path, "PG_SERVER", self.__server)
        dotenv.set_key(dotenv_path, "PG_USER", self.__user)
        dotenv.set_key(dotenv_path, "PG_PASSWORD", self.__password)
        dotenv.set_key(dotenv_path, "DB_NAME", self.__db_name)

    def get_connection(self):
        return create_connection(self.__server, self.__user, self.__password, self.__host, self.__port, True)

    def create_database(self, prnt) -> bool:
        conn = create_connection("", self.__user, self.__password, self.__host, self.__port, prnt)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        if conn == None: return False

        conn.autocommit = True
        cursor = conn.cursor()
        name_db = os.environ["DB_NAME"]

        # команда для створення бази даних
        sql = "CREATE DATABASE " + self.__db_name
        # виконання коду sql
        ret = True
        try:
            cursor.execute(sql)
            if prnt:
                print(f"Database {name_db} is created successful")
        except OperationalError:
            if prnt:
                print(f"The database {name_db} have already existed")
        except:
            print(f"Error creating the database {name_db}")
            ret = False

        cursor.close()
        conn.close()

        return ret

    def _execute_query(self, conn, query, prnt=False):
        """
        Doing sql-query
        conn - DataBase connection -> psycopg2.connection
        """
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            conn.commit()
            if prnt:
                print(f"Query {query} is executed successfully")
        except OperationalError as e:
            if prnt:
                print(f"The error '{e}' occurred")
            else:
                raise OperationalError

    def create_database_tables(self, lst_table, prnt = False) -> bool:
        """
        Create tables
        lst_table - list of sql-queries for creating tables
        prnt - print log
        """
        conn = create_connection(self.__db_name, self.__user, self.__password, self.__host, self.__port, prnt)
        if conn == None: return False
        if prnt: print("Connect to Database")

        for query in lst_table:
            self._execute_query(conn, query, prnt)

        conn.close()

    def __str__(self):
        return f"Parameters: Server name: {self.__server}\nDatabase name: {self.__db_name}\n" + \
            f"User: {self.__user}\nPassword: {self.__password}\nHost: {self.__host}\nPort: {self.__port}\n"

