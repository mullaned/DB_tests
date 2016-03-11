from database.mysql import MySQLDatabase

my_db = MySQLDatabase('juanexp','root','ihi8Neru')

#results1 = my_db.get_available_tables()

#results2 = my_db.get_columns_for_table('employees')

kwrgs = {'where': "employees.first_name='Gino'",
         'order by': "employees.last_name",
         'limit': "2"}

results3 = my_db.select('employees', columns=['first_name', 'last_name'], named_tuples=True,**kwrgs)

#print results1

#print results2

print results3

































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






