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
from sklearn.feature_extraction.text import CountVectorizer

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
        ratings_data = pd.read_csv("sample-data.csv")
        #print(ratings_data)
        # list of text documents
        text = ["The quick brown fox jumped over the lazy bikash dog.",'This is the first document.']
        # create the transform
        vectorizer = CountVectorizer()
        # tokenize and build vocab
        vectorizer.fit(text)
        # summarize
        print(vectorizer.vocabulary_)
        # encode document
        vector = vectorizer.transform(text)
        # summarize encoded vector
        print(vector.shape)
        print(type(vector))
        print(vector.toarray())
        
    except Exception as e:
        log.error(colored(str(e),"red"))

#---main function called---
if __name__=="__main__":
    try:
        main()
    except Exception as e:
        log.error(colored(str(e),"red"))

