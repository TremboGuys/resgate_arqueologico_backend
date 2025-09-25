
import os
import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv
from .helpers import image_to_base64
from rest_framework.exceptions import APIException

load_dotenv()

class UploadCloudinary():
    cloudinary.config(
        cloud_name=os.environ.get("CLOUD_NAME"),
        api_key=os.environ.get("API_KEY"),
        api_secret=os.environ.get("API_SECRET"),
        secure=True
    )
    
    def upload_image(self, file):
        file = image_to_base64(file)

        try:
            response = cloudinary.uploader.upload(file, transformation=[{"width": 100, "heigth": 100}])
        except Exception as error:
            raise APIException(f"Error in upload image: {error}")
        
        return response