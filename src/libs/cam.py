from io import BytesIO
from time import sleep
from picamera import PiCamera
from PIL import Image

class cam:
    def __init__(self):
        self.stream = BytesIO()
        self.camera = PiCamera()
    
    def get(self):
        self.camera.capture(self.stream, format='jpeg')
        self.stream.seek(0)
        image = Image.open(self.stream).convert('RGB') 
        return image