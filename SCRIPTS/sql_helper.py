"""
This script has all function related to Mysql database operation.
"""

#---standard library---
import sys,os
sys.path.append('/usr/local/lib/python3.5/dist-packages')
#---Third party library---
import pymysql.cursors
import pandas as pd
from termcolor import colored
#---Local library---
from logger_config import *
import logger_config
from constants import *

#---Connection to "DATABASE_Exception"---
def connect_to_db(database_name):
	connection = pymysql.connect(host=HOST,
                                     user=USER,
                                     password=PASSWORD,
                                     db=database_name,
                                     charset='utf8mb4',
                                     port=PORT,
                                     cursorclass=pymysql.cursors.DictCursor)
	return connection

#---Read the data from  table in the db---
def read_data_from_db(connection,sql_query):
    '''
    Returns data in dataframe from table based on given query.
    '''
    with connection.cursor() as cursor:
        try:
            sql=sql_query
            cursor.execute(sql)
            if cursor.rowcount > 0:
                df=pd.DataFrame(cursor.fetchall())
            else:
                df=pd.DataFrame()	
        except Exception as e:
            log.error(e)
    connection.close()
    return df

