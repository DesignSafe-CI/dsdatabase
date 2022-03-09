import pymysql
import pandas as pd
import sqlalchemy

def connect():
    try:
        print('We have phased out the ngl_db.connect() command in favor of the ngl_db.read_sql(sql, output) command. Please see https://ngl-tools.readthedocs.io/en/latest/ for details.')
    except:
        pass
    
def read_sql(**kwargs):
    if('sql' not in kwargs):
        print('You must specify sql= in your argument list')
        return
    if('output' in kwargs):
        output = kwargs['output']
    else:
        output = 'DataFrame'
    if(output=='DataFrame'):
        try:
            engine = sqlalchemy.create_engine('mysql+pymysql://dspublic:R3ad0nlY@129.114.52.174:3306/sjbrande_ngl_db')
            data = pd.read_sql_query(sql, con=engine)
            engine.dispose()
            return(data)
        except:
            print('pd.read_sql_query(sql, cnx) failed')
            pass
    elif(output=='dict'):
        try:
            cnx = pymysql.connect(user='dspublic', password='R3ad0nlY', host='129.114.52.174', port=3306, db='sjbrande_ngl_db')
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
