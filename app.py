from flask import Flask
from flask_restful import Resource, Api, reqparse
from base64 import b64decode


app = Flask(__name__)
api = Api(app)

class UploadImage(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('base_64_image_content', type=bytes)
        args = parse.parse_args()
        b64_img = args['base_64_image_content']
        with open('img.jpeg', 'wb') as f:
            f.write(b64decode(b64_img)) 
        return {"upload":"success"}

api.add_resource(UploadImage, '/extract_date')
