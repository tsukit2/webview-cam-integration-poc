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
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

import image
import utils


class SyncUploadHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write(template.render("syncupload.html", 
           { 'device': utils.get_device_name(self.request) }))


class PostUploadHandler(webapp.RequestHandler):
    def post(self):
        data = { 
           'amount': self.request.get('amount'),
           'frontCheckImageData': image.process(self.request.get('frontCheckImageData')),
           'backCheckImageData': image.process(self.request.get('backCheckImageData'))
        }
        self.response.out.write(template.render("syncupload-done.html", data))


handlers = [('/syncupload', SyncUploadHandler),
            ('/syncupload/upload', PostUploadHandler)
           ]

