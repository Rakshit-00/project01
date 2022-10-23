from flask import Flask,jsonify,render_template,request
from models.utils import FlatPrediction
# import config

app=Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome to BANGLORE PROPERTY PREDICTION ")
    return render_template('index.html')

@app.route('/predict_charges',methods=['POST','GET'])
def get_insurance_charges():

    if request.method=='GET':
        print("We are using GET Method")

        # data = request.form
        # print("Data::",data)
        
        # total_sqft=eval(data['total_sqft'])
        # bath = eval(data['bath'])
        # area_type = data['area_type']
        # bhk = eval(data['bhk'])
        # location = data['location']
        
        total_sqft=eval(request.args.get("total_sqft"))
        bath = eval(request.args.get("bath"))
        area_type = (request.args.get("area_type"))
        bhk = eval(request.args.get("bhk"))
        location = (request.args.get("location"))
    

        flat = FlatPrediction(total_sqft,bath,area_type,bhk,location)
        charges = flat.get_predicted_price()
        print()

        return render_template('index.html',prediction= charges)

        # return jsonify({"Result":f"Predicted Charges for Medical Insurance is {charges}/- Rs. Only"})

    else:
        print("We are in POST Method")

        total_sqft=eval(request.form.get("total_sqft"))
        bath = eval(request.form.get("bath"))
        area_type = (request.form.get("area_type"))
        bhk = eval(request.form.get("bhk"))
        location = (request.form.get("location"))

        flat = FlatPrediction(total_sqft,bath,area_type,bhk,location)
        charges = flat.get_predicted_price()
        print()

        return render_template('index.html',prediction= charges)

        # return jsonify({"Result":f"Predicted Charges for Medical Insurance is {charges}/- Rs. Only"})

if __name__ == "__main__" :

    app.run(host='0.0.0.0',port=5000,debug=True)