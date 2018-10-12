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

    def user_data_query_by(self, msisdn, gender, locations, age, limit, part):
        cursor = self.connect_mysql()
        cursor.execute(self.sql_query.user_data_query_by(msisdn, gender, locations, age, limit, part))
        cursor.close()
        return cursor.fetchall()

    def location_query(self):
        cursor = self.connect_mysql()
        cursor.execute(self.sql_query.location_query())
        cursor.close()
        return cursor.fetchall()

    def msisdn_query_by(self, fb_ids, part):
        cursor = self.connect_mysql()
        cursor.execute(self.sql_query.msisdn_query_by(fb_ids, part))
        cursor.close()
        return cursor.fetchall()
