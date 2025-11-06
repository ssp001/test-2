#%%
import logging
import pandas as pd
#%%
class Data_ingeaiton:
    def __init__(self,data):
        self.data:str = data
    def ingest_data(self,df)->pd.DataFrame:
        try:
            df = pd.read_csv(self.data)
            logging.info("Data ingestaion task done")
            return(df)
        except Exception as e:
            raise RuntimeError("Error ouccured in Data_ingeation ingest-Data {e}")



