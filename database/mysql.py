import MySQLdb as _mysql


class MySQLDatabase:
    def __init__(self, database_name, username, password, host='localhost'):
        try:
            self.db = _mysql.connect(db=database_name,
                                     host=host,
                                     user=username,
                                     passwd=password)

            self.database_name = database_name

            print "Connected to MySQL!"

        except _mysql.Error, e:
            print e

    def __del__(self):
        if hasattr(self, 'db'):
            self.db.close()
            print "MYSQL Connection closed"

    def get_available_tables(self):
        cursor = self.db.cursor()
        cursor.execute("SHOW TABLES;")
        self.tables = cursor.fetchall()
        cursor.close()
        return self.tables

    def get_columns_for_table(self, table_name):
        cursor = self.db.cursor()
        cursor.execute("SHOW COLUMNS FROM %s " % table_name)
        columns = cursor.fetchall()
        cursor.close()
        return columns
