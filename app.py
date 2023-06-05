# imports for app
import mariadb
import dbcreds
import json
#  importing flask aND defining app variable to configure api
from flask import Flask
app = Flask(__name__)
# defining conn and cursor to use throughout
conn = mariadb.connect(**dbcreds.conn_params)
cursor = conn.cursor()
# function to close cursor and conn
def close_all():
    if(cursor != None):
        cursor.close()
    if(conn != None):
        conn.close()
# setting page /dogs to call procedure get_dogs and if results
# are in a list it converts it using Json
@app.get('/dogs')
def get_dogs():
    cursor.execute('CALL get_dogs()')
    results = cursor.fetchall()
    if(type(results) == list):
        results_json = json.dumps(results,default=str)
        close_all()
        return(results_json)
    else:
        close_all()
        return'something went wrong'
# setting page /animals to call procedure get_all_animals and if results
# are in a list it converts it using json 
@app.get('/animals')
def get_animals():
    cursor.execute('CALL get_all_animals()')
    results = cursor.fetchall()
    if(type(results) == list):
        results_json = json.dumps(results,default=str)
        close_all()
        return(results_json)
    else:
        close_all()
        return'something went wrong'
# setting page/cats to call procedure get_cats and if results are
# in a list it converts it using Json
@app.get('/cats')
def get_cats():
    cursor.execute('CALL get_cats()')
    results = cursor.fetchall()
    if(type(results) == list):
        results_json = json.dumps(results,default=str)
        close_all()
        return(results_json)
    else:
        close_all()
        return'something went wrong'
# runs app with debugger
app.run(debug=True)