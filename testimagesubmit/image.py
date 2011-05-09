from google.appengine.api import images
from google.appengine.api import urlfetch
import base64

APPROVE_PNG = None

def get_approve_png():
   # if it's already loaded, don't load it again
   global APPROVE_PNG
   if APPROVE_PNG != None:
      return APPROVE_PNG

   # if reach here, we need to load it
   url = "http://chart.apis.google.com/chart?chst=d_text_outline&chld=000000|12|h|FFFFFF|_|APPROVED"
   result = urlfetch.fetch(url)
   if result.status_code == 200:
      APPROVE_PNG = result.content
   return APPROVE_PNG


def process(originalBase64PictureData):
   # return originalBase64PictureData
   scaledImage = images.resize(base64.decodestring(originalBase64PictureData),
                            160, 120)
   approvedImage = images.composite(
         [(scaledImage, 0, 0, 1.0, images.TOP_LEFT),
          (get_approve_png(), 0, 0, 1.0, images.CENTER_CENTER)],
         160, 120)
   return base64.encodestring(approvedImage)



