import cloudinary
import cloudinary.uploader as uploader


cloudinary.config( 
  cloud_name = "", 
  api_key = "", 
  api_secret = "" 
)


def get_uploader():
    return uploader