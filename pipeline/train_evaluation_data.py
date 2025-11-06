#%%
import os
from keras.models import Model
from keras.layers import Dense,Input
import logging
import pandas as pd
from keras.models import load_model
import numpy as np
# %%
#%%
import logging
import pandas as pd
from keras.models import Model, load_model
from keras.layers import Dense, Input

class Training_Evaluation:
    def __init__(self, model_path=r"model_disk\Blood_cancer_prediction_model.h5"):
        """
        Initialize training or load existing model.
        """
        try:
            self.model_path = model_path
            try:
                self.model_path = os.path.join(os.path.dirname(__file__), "model_disk", "Blood_cancer_prediction_model.h5")
                self.model = load_model(model_path)
                logging.info(f"✅ Loaded trained model from: {model_path}")
            except Exception:
                logging.warning(f"⚠️ Model file not found at {model_path}. You need to train the model first.")
                self.model = None
        except Exception as e:
            raise RuntimeError(f"Error in Training_Evaluation __init__: {e}")

    # -------------------------------------------------------------------------
    def train_data(self, x_train, y_train_Diagnosis, y_train_stage):
        """
        Train a multi-output classification model.
        """
        try:
            self.model_path = os.path.join(os.path.dirname(__file__), "model_disk", "Blood_cancer_prediction_model.h5")
            inputs = Input(shape=(x_train.shape[1],))
            x = Dense(64, activation='relu')(inputs)
            x = Dense(32, activation='relu')(x)

            Diagnosis_output = Dense(4, activation='softmax', name='Diagnosis_output')(x)
            Stage_output = Dense(5, activation='softmax', name='Stage_output')(x)

            self.model = Model(inputs=inputs, outputs=[Diagnosis_output, Stage_output])
            self.model.compile(
                optimizer='adam',
                loss={
                    'Diagnosis_output': 'categorical_crossentropy',
                    'Stage_output': 'categorical_crossentropy'
                },
               metrics={
                    'Diagnosis_output': ['accuracy'],
                    'Stage_output': ['accuracy']
               }
            )

            logging.info("🚀 Training started...")

            self.model.fit(
                x_train,
                {'Diagnosis_output': y_train_Diagnosis, 'Stage_output': y_train_stage},
                epochs=10,
                batch_size=64,
                verbose=1
            )
            self.model_path = "model_disk/Blood_cancer_prediction_model.h5"

# ✅ Create folder if not exists
            os.makedirs("model_disk", exist_ok=True)

            # Save the trained model
            model_save_path = "model_disk/Blood_cancer_prediction_model.h5"
            
            self.model.save(model_save_path)  # saves in HDF5 format
            print(f"Model saved at {model_save_path}")

            return "✅ Model training completed successfully."

        except Exception as e:
            raise RuntimeError(f"Error in train_data: {e}")

    # -------------------------------------------------------------------------
    def model_predict(self, features: dict):
        try:
            if self.model is None:
                self.model = load_model(self.model_path)

            input_df = pd.DataFrame([features])
            predictions = self.model.predict(input_df)

            # Get the index of the max probability
            diagnosis_index = int(np.argmax(predictions[0], axis=1)[0])
            stage_index = int(np.argmax(predictions[1], axis=1)[0])

            # Map index back to actual class labels (must match your training)
            diagnosis_labels = ['Leukemia', 'Lymphoma', 'Myeloma', 'Other']  # adjust as per your dataset
            stage_labels = ['Stage I', 'Stage II', 'Stage III', 'Stage IV', 'Stage V', 'Stage VI']  # adjust

            result = {
                "Diagnosis": diagnosis_labels[diagnosis_index],
                "Stage": stage_labels[stage_index],
                "Diagnosis_Probabilities": predictions[0].tolist(),
                "Stage_Probabilities": predictions[1].tolist()
            }
            return result

        except Exception as e:
            raise RuntimeError(f"Error in model_predict: {e}")



