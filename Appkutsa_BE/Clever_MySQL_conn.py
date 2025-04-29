import mysql
import mysql.connector


#Connect to the database
mysqlConn = mysql.connector.Connect(
    host = 'localhost', #'bmn0p7ohukcq6xxuqudp-mysql.services.clever-cloud.com',
    user = 'root', #upfp89sjo0fd79v0',
    #password = 'myJotaSQL1+',#'HGByo9urELWdufYqUvsG',
    database = 'kutsadb',#'bmn0p7ohukcq6xxuqudp',
    port = 3306
)

#Create a cursor object
cleverCursor = mysqlConn.cursor()
