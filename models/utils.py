import pickle
import numpy as np
import pandas as pd
import json
import config

class FlatPrediction():

    def __init__(self,total_sqft,bath,area_type,bhk,location):
        self.total_sqft=total_sqft
        self.bath=bath
        self.area_type	="area_type_"+ area_type
        self.bhk=bhk
        self.location="location_"+ location 


    def load_model(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)

    def get_predicted_price(self):

        self.load_model()  # Calling load_model method to get model and json_data

        area_type_index = self.json_data['columns'].index(self.area_type)
        location_index=self.json_data['columns'].index(self.location)
 
        array = np.zeros(len(self.json_data['columns']))

        array[0] = self.total_sqft
        array[1] = self.bath
        array[2] = self.bhk
       
        array[area_type_index] = 1
        array[location_index] = 1

        print("Test Array -->\n",array)
        predicted_charges = self.model.predict([array])[0]
        print("predicted_charges",predicted_charges)
        return np.around(predicted_charges, 2)


if __name__ == "__main__":
    total_sqft = 1011
    bath = 2
    area_type ="Built-up  Area"
    bhk = 2
    location = "Whitefield"
    

    flat = FlatPrediction(total_sqft,bath,area_type,bhk,location)
    charges = flat.get_predicted_price()
    print()
    print(f"Predicted Charges for Medical Insurance is {charges}/- Rs. Only")

        	
        