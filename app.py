from flask import Flask,request, jsonify

app = Flask(__name__)

def predict_price(lotarea):
    # Load a machine learning model
    # pass the features 
    # get the prediction using the .predict Attribute return that prediction 
    # for now create a mock model
    #  y = B + B1x
    return 50000 + 200*int(lotarea)

@app.route('/getprice/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    lotarea = request.args.get("LotArea", None)

    # For debugging
    print(f"got LotArea {lotarea}")

    response = {}

    # Check if user sent a name at all
    if not lotarea:
        return "<h2> Lot Area value not found enter LotArea value </h2>"
    # Check if the user entered a number not a string
    elif not str(lotarea).isdigit():
        return "<h2> Lot Area can't be non Numeric </h2>"
    # Now the user entered a valid name
    else:
        return "<h2> Predicted price of house is {0}</h2>".format(predict_price(lotarea))


@app.route('/')
def index():
    return '<h2>Hello world welcome to python flask app and impriving it</h2>'

if __name__ == '__main__':
    app.run(threaded=True,port=5000)