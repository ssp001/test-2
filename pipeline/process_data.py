#%%
import pandas as pd
import logging
from sklearn.preprocessing import LabelEncoder,OrdinalEncoder,OneHotEncoder

class Process_Data:

    def __init__(self,df)->pd.DataFrame:
        self.df:pd.DataFrame = df

    def drop_func(self):

        try:
            self.df.drop(columns='Patient_ID',inplace=True)
            logging.info(f"Column dropping done successfully. Current columns: {self.df.columns.tolist()}")

        except Exception as e:
            logging.info(f"Error ocurred in class process data drop func {e}")

class Encoding_Func(Process_Data):
        
        def __init__(self,df:pd.DataFrame):
             self.df = df
        
        def OneHotEndoer(self):
        
            try:
                ohe = OneHotEncoder(drop='first')
                index = ['Gender','Fever','Fatigue','Weight Loss','Bone Pain','Night Sweats','Enlarged Lymph Nodes','Smoking Habit','Alcohol Consumption','Family Cancer History','Previous Blood Disorder']
                ar = ohe.fit_transform(self.df[index])
                new = ar.toarray()
                self.df[index] = pd.DataFrame(new,columns=[index])
                Data_frame = self.df.fillna("Negative",inplace=True)
                logging.info("one hot ending task done")
                return self.df
            
            except Exception as e:
               raise RuntimeError(f'error occured in ecoding class one hot ecoding function {e}')
        
        def lable_eoncder(self):
            
            try:
                le = LabelEncoder()
                Data_frame = self.df['Blood_Group'] = le.fit_transform(self.df['Blood_Group'])
                logging.info("Label Ending task done")
                return Data_frame
            
            except Exception as e:
               raise RuntimeError(f'error occuerd in ordinal ending class lable ecoding fuction {e}')
        
        def ordinal_encoder(self):
        
            try: 
                oe = OrdinalEncoder()
                Data_frame = self.df['Physical Activity'] = oe.fit_transform(self.df[['Physical Activity']])
                logging.info("ordinal encoding task is done")
                return Data_frame
        
            except Exception as e:
                 raise RuntimeError(f'Error occured in Ending class ordinal encoding function{e}')

# %%
