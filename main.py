from database.mysql import MySQLDatabase

my_db = MySQLDatabase('juanexp','root','ihi8Neru')

results1 = my_db.get_available_tables()

results2 = my_db.get_columns_for_table('employees')

print results1

print results2

































#cursor = db.cursor()
#
#cursor.execute("UPDATE employees SET employees.first_name = 'Dave' WHERE employees.emp_no = 10001  ")
#
#cursor.execute("SELECT * FROM employees WHERE employees.emp_no = 10001 ")
#
#db.commit()
#
#results = cursor.fetchmany(2)

#cursor.close()
#db.close()

#print results






