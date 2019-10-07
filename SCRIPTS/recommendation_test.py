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
        ratings_data = pd.read_csv("ml-latest-small/ratings.csv")
        #print(ratings_data.head())
        movie_names = pd.read_csv("ml-latest-small/movies.csv")
        #print(movie_names.head())
        movie_data = pd.merge(ratings_data, movie_names, on='movieId')
        #print(movie_data.groupby("rating").groups.keys())
        print(movie_data.groupby('title')['rating'].mean())
    except Exception as e:
        log.error(colored(str(e),"red"))

#---main function called---
if __name__=="__main__":
    try:
        main()
    except Exception as e:
        log.error(colored(str(e),"red"))

