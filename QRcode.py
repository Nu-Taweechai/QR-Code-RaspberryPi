from io import BytesIO
from time import sleep
from PIL import Image
from picamera import PiCamera
from zbarlight import scan_codes

stream = BytesIO()
codes = None


with PiCamera() as camera:
  camera.start_preview()
  sleep(2)
  while codes is None:
    stream.seek(0)
    camera.capture(stream, 'jpeg')
    stream.seek(0)
    codes = scan_codes(['qrcode'], Image.open(stream))
    camera.stop_preview()
    print(codes)

