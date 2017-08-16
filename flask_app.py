from flask import Flask, request, jsonify, send_file
from flask_restful import Resource, Api
#from sqlalchemy import create_engine
from json import dumps
from PIL import Image

from learn_dict import *

from matplotlib import pyplot as plt

app = Flask(__name__)


#This controller listens "POST" -request in address "localhost:5000/"
#One can use e.g. command line tool 'curl' to make 
#POST request, e.g. '$ curl -F "file=@kiiski.jpg" http://localhost:5000/ > testi.png'
@app.route("/", methods=["POST"])
def home():
    
    #The request parameter name is 'file'
    img = Image.open(request.files['file'])
    img.save('temp', img.format)

    # Save the dictionary plot to file named 'dict.png'
    save_dict_img('temp', 'dict')

    #return 'Success!'
    return send_file('dict.png') #send_file(img)


if __name__ == "__main__":
    app.run()
