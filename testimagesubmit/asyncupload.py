#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import time

from google.appengine.ext import webapp
from google.appengine.api import memcache
from google.appengine.ext.webapp import template

import image
import utils


class ASyncUploadHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write(template.render("asyncupload.html", 
           { 'device': utils.get_device_name(self.request) }))

class DepositPictureHandler(webapp.RequestHandler):
   def post(self):
      theImage = image.process(self.request.get('checkImageData'));
      imageKey = str(int(time.time() * 1000));
      memcache.set(imageKey, theImage);
      self.response.out.write(imageKey);

class PostUploadHandler(webapp.RequestHandler):
    def post(self):
        data = { 
           'amount': self.request.get('amount'),
           'frontCheckImageData': memcache.get(self.request.get('frontCheckImageHandle')),
           'backCheckImageData': memcache.get(self.request.get('backCheckImageHandle'))
        }
        self.response.out.write(template.render("asyncupload-done.html", data))


handlers = [('/asyncupload', ASyncUploadHandler),
            ('/asyncupload/deposit', DepositPictureHandler),
            ('/asyncupload/upload', PostUploadHandler)
           ]

