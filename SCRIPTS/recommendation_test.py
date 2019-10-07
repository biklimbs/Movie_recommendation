"""
This program recommends movie based on previous rating.
"""
#---Importing packages---
#---standard library---
import sys
import re
sys.path.append('/usr/local/lib/python3.5/dist-packages')
import time as t
from datetime import datetime,date,timedelta
import warnings
warnings.filterwarnings("ignore")

#---Third party library---
import pandas as pd
import numpy as np
from termcolor import colored
import json

#---Local library---
from logger_config import *
import logger_config

#---Configuring log filename---
log_file=os.path.splitext(os.path.basename(__file__))[0]+".log"
log = logger_config.configure_logger('default', ""+DIR+""+LOG_DIR+"/"+log_file+"")

#---Developer details---
__author__="Bikash Limboo"
__maintainer__="Bikash Limboo"


#---main function---
def main():
    try:
        #---Reading users file:
        u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
        users = pd.read_csv('ml-100k/u.user', sep='|', names=u_cols,encoding='latin-1')
        print(users.head())
        #---Reading ratings file:
        r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
        ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols,encoding='latin-1')
        
        #Reading items file:
        i_cols = ['movie id', 'movie title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
        'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
        'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
        items = pd.read_csv('ml-100k/u.item', sep='|', names=i_cols,encoding='latin-1')
        print(items.head())
    except Exception as e:
        log.error(colored(str(e),"red"))

#---main function called---
if __name__=="__main__":
    try:
        main()
    except Exception as e:
        log.error(colored(str(e),"red"))

