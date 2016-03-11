import MySQLdb as _mysql
import collections


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

    def convert_to_named_tuples(self, cursor):
        results = None

        names = " ".join(d[0] for d in cursor.description)
        klass = collections.namedtuple('Results', names)

        try:
            results = map(klass._make, cursor.fetchall()) #amount of results to return
        except _mysql.ProgrammingError:
            pass

        return results


    def select(self,table,columns=None, named_tuples=False, **kwargs):

        sql_str = "SELECT "

        #add columns or just the wildcard
        if not columns:
            sql_str += " * "
        else:
            for column in columns:
                sql_str += "%s, " % column

            #removes the last comma
            sql_str = sql_str[:-2]


            #add the table to select from
            sql_str += " FROM %s.%s" % (self.database_name, table)

            #there is a JOIN clause attached
            if kwargs.has_key('join'):
                sql_str += " INNER JOIN %s" % kwargs.get('join')

            #if there is a WHERE clause attached
            if kwargs.has_key('where'):
                sql_str += " WHERE %s" % kwargs.get('where')

            if kwargs.has_key('order by'):
                sql_str += " ORDER BY %s" % kwargs.get('order by')

            if kwargs.has_key('limit'):
                sql_str += " LIMIT %s" % kwargs.get('limit')

            sql_str += ";" #finalise our sql string

            cursor = self.db.cursor()

            cursor.execute(sql_str)

            if named_tuples:
                results = self.convert_to_named_tuples(cursor)

            else:
                results = cursor.fetchall() #the amount of records to return


            cursor.close()

            return results


    def delete(self, table, **wheres):
        sql_str = "DELETE FROM %s.%s" % (self.database_name, table)

        if wheres is not None:
            first_where_clause = True
            for where, term in wheres.iteritems():
                if first_where_clause:
                    #this is the first WHERE clause
                    sql_str += " WHERE %s.%s%s" % (table,where,term)
                    first_where_clause = False
                else:
                    #this is the additional clause so use AND
                    sql_str += " AND %s.%s%s" % (table,where,term)


        sql_str += ";"

        cursor = self.db.cursor()
        cursor.execute(sql_str)
        self.db.commit()
        cursor.close()