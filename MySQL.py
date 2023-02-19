import mysql.connector

mydb= mysql.connector.connect(host = 'localhost', user = 'root', password = 'Pwd4DBM$')
#initiallising a variable connected with MySQL server
cur= mydb.cursor()
#Cursor allocates memory for databases in the server
cur.execute('create table st(name varchar(20), roll int')
#any commands that can be run on MySQL are to be passed through execute method
#alltables is the database in MySQL which I created to place all the tables
#use "use alltables;" command to use it to manipulate tables
