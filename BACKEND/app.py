from flask import Flask
import os
import BusinessObjects as bo
import DataObject  as do

app = Flask(__name__)

db_ip=os.getenv("db_ip") #'10.0.2.15'
ConnectionData ={}
ConnectionData ['user'] = 'postgres'
ConnectionData ['password'] = 'postgres'
ConnectionData ['host'] = str(db_ip)
ConnectionData ['port'] = '5432'
ConnectionData ['database'] = 'northwind'

@app.route("/")
def hello():
    c1=bo.Customer(1,'Alfreds Futterkiste','Maria Anders','Obere Str. 57','Berlin','12209','Germany')
    return c1.CustomerName

@app.route("/test_insert")
def test_insert():
    #ConnectionString = 'database=northwind user=postgres password =postgres host=10.0.2.15 port=5432'
    c2=do.Customer(ConnectionData)
    c1=bo.Customer(1,'Alfreds Futterkiste','Maria Anders','Obere Str. 57','Berlin','12209','Germany')
    s1=c2.insert(c1)
    return s1

if __name__ =="__main__":
    app.run(host='0.0.0.0',port=8080)