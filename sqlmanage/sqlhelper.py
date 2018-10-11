from flaskext.mysql import MySQL
from sqlmanage.sqlconfig import SqlConfig
from sqlmanage.sqlquery import SqlQuery

class SqlHelper:
    def __init__(self, app):
        sql_config = SqlConfig()
        self.my_sql = MySQL()
        self.sql_query = SqlQuery()
        app.config['MYSQL_DATABASE_USER'] = sql_config.mysql_database_user
        app.config['MYSQL_DATABASE_PASSWORD'] = sql_config.mysql_database_password
        app.config['MYSQL_DATABASE_HOST'] = sql_config.mysql_database_host
        self.my_sql.init_app(app)

    def connect_mysql(self):
        connect = self.my_sql.connect()
        cursor = connect.cursor()
        return cursor

    # def query_all(self):
    #     cursor = self.connect_mysql()
    #     cursor.execute(self.sql_query.query_all())
    #     return cursor.fetchall()

    def query_by_id(self, msisdn, part):
        cursor = self.connect_mysql()
        cursor.execute(self.sql_query.query_by(msisdn, part))
        return cursor.fetchall()
