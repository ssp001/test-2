#%%
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = "0"



from data_ingeation import Data_ingeaiton
from process_data import Process_Data,Encoding_Func
from train_test_split_data import Train_test_split
from train_evaluation_data import Training_Evaluation

if __name__ == "__main__":


    # ✅ Load and process dataset
    data_path = r"C:\Users\shova\Desktop\project\test-2\Data-set\Blood_Cancer_Realistic_Dataset.csv"
    Data_set = Data_ingeaiton(data=data_path)
    df = Data_set.ingest_data(None)

    Processed_data = Process_Data(df=df)
    Processed_data.drop_func()

    encoder = Encoding_Func(Processed_data.df)
    encoder_df = encoder.OneHotEndoer()
    encoder.lable_eoncder()
    encoder.ordinal_encoder()

    splitter = Train_test_split(df=encoder_df)
    x_train, y_train_Digonasis, y_train_stage = splitter.split_func()

    # ✅ Train and save
    trainer = Training_Evaluation()
    trainer.train_data(x_train, y_train_Digonasis, y_train_stage)



    # This is all functions and the main function 💩.
    





# %%
