from flask import Flask
from flask_restful import Resource, Api, reqparse
from base64 import b64decode
from werkzeug.datastructures import FileStorage
import os

from extract_date import pipeline
from utils import random_string


app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return "Go to https://github.com/techytushar/ocr-date-extractor for more information"

class SendB64Image(Resource):
    def post(self):
        # Route to receive base64 encoded images 
        parse = reqparse.RequestParser()
        parse.add_argument('base_64_image_content', type=str)
        args = parse.parse_args()
        b64_img = args['base_64_image_content']
        file_name = random_string()
        with open(f'./static/uploaded_images/{file_name}.jpeg', 'wb') as f:
            f.write(b64decode(b64_img))
        date = pipeline(file_name)
        os.remove(f'./static/uploaded_images/{file_name}.jpeg')
        if date is ValueError:
            return {"Error": "Only bytes data of Base64 encoded image accepted"}, 415
        return {"date": date}

class UploadImage(Resource):
    def post(self):
        # Route to receive image files
        parse = reqparse.RequestParser()
        parse.add_argument('image', type=FileStorage, location='files')
        args = parse.parse_args()
        img = args['image']
        file_name = random_string()
        img.save(f"./static/uploaded_images/{file_name}.jpeg")
        date = pipeline(file_name)
        os.remove(f'./static/uploaded_images/{file_name}.jpeg')
        if date is ValueError:
            return {"Error": "Only bytes data of Base64 encoded image accepted"}, 415
        return {"date": date}

if __name__ == "app":
    path = './static/uploaded_images'
    if not os.path.exists(path):
        os.makedirs(path)
    api.add_resource(SendB64Image, '/extract_date')
    api.add_resource(UploadImage, '/extract_date_from_image')
