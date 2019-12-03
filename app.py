from flask import Flask
from flask_restful import Resource, Api, reqparse
from base64 import b64decode
from werkzeug.datastructures import FileStorage
from extract_date import find_date


app = Flask(__name__)
api = Api(app)

class SendB64Image(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('base_64_image_content', type=str)
        args = parse.parse_args()
        b64_img = args['base_64_image_content']
        with open('./static/uploaded_images/img.jpeg', 'wb') as f:
            f.write(b64decode(b64_img)) 
        return {"upload":"success"}

class UploadImage(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('image', type=FileStorage, location='files')
        args = parse.parse_args()
        img = args['image']
        img.save("./static/uploaded_images/img.jpg")

api.add_resource(SendB64Image, '/extract_date')
api.add_resource(UploadImage, '/extract_date_from_image')
