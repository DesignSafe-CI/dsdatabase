# Establishes connection to NGL database from MySQL Workbench
import pymysql
import pandas as pd

def connect():
    try:
        print('We will be phasing out the ngl_db.connect() command in favor of the ngl_db.read_sql(sql, output) command in the future. Please see https://ngl-tools.readthedocs.io/en/latest/ for details. If you use cnx = ngl_db.connect(), please close your connection [cnx.close()] when you are finished querying data. Open connections will be manually closed each night to facilitate database replication.')
        return(pymysql.connect(user='dspublic', password='R3ad0nlY', host='129.114.52.174', port=3306, db='sjbrande_ngl_db', read_timeout=600.0))
    except:
        pass
    
def read_sql(**kwargs):
    if('sql' not in kwargs):
        print('You must specify sql= in your argument list')
        return
    try:
        cnx = pymysql.connect(user='dspublic', password='R3ad0nlY', host='129.114.52.174', port=3306, db='sjbrande_ngl_db')
    except:
        print('db connection failed')
        pass
    if('output' in kwargs):
        output = kwargs['output']
    else:
        output = 'DataFrame'
    if(output=='DataFrame'):
        try:
            data = pd.read_sql(sql, cnx)
            cnx.close()
            return(data)
        except:
            print('pd.read_sql(sql, cnx) failed')
            pass
    elif(output=='dict'):
        try:
            cur = cnx.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            data = cur.fetchall()
            cnx.close()
            return(data)
        except:
            print('cur.fetchall() failed')
            pass
    else:
        print('In ngl_db.read_sql(sql, output), output must be either "DataFrame" or "dict", not "' + output + '"')
        return
