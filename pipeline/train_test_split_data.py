#%%
import logging
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import pandas as pd
from sklearn.model_selection import train_test_split
from typing import Tuple
from keras.utils import to_categorical
import numpy as np

class Train_test_split:
    
    def __init__(self,df:pd.DataFrame):
        self.df = df
    
    def split_func(self)->Tuple[pd.DataFrame,np.ndarray,np.ndarray]:
    
        try:
            x = self.df.iloc[:,:-2]
            y = self.df.iloc[:,-2:]
            
            x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=49)
            
            y_train_Digonasis = to_categorical(y_train['Diagnosis'].factorize()[0],num_classes=4)
            y_train_stage = to_categorical(y_train['Disease Stage'].factorize()[0],num_classes=5)
            
            y_train_Digonasis,y_train_stage
            
            logging.info("spliting data task completed")
            return (x_train),y_train_Digonasis,y_train_stage
    
        except Exception as e:
            
            raise RuntimeError(f'Error occured in Train_test_split class split_func {e}')
    


    
# %%
