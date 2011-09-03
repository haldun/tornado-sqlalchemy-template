# Python imports
import os

# Tornado imports
import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
from tornado.web import url

# App imports
import forms
import uimodules

# Options
define("port", default=8888, help="run on the given port", type=int)
define("debug", default=False, type=bool)

class Application(tornado.web.Application):
  def __init__(self):
    handlers = [
      url(r'/', IndexHandler, name='index'),
    ]
    settings = dict(
      debug=options.debug,
      static_path=os.path.join(os.path.dirname(__file__), "static"),
      template_path=os.path.join(os.path.dirname(__file__), 'templates'),
      xsrf_cookies=True,
      # TODO Change this to a random string
      cookie_secret="nzjxcjasduuqwheazmu293nsadhaslzkci9023nsadnua9sdads/Vo=",
      ui_modules=uimodules,
    )
    tornado.web.Application.__init__(self, handlers, **settings)

class BaseHandler(tornado.web.RequestHandler):
  pass


class IndexHandler(BaseHandler):
  def get(self):
    form = forms.HelloForm()
    self.render('index.html', form=form)

  def post(self):
    form = forms.HelloForm(self)
    if form.validate():
      self.write('Hello %s' % form.planet.data)
    else:
      self.render('index.html', form=form)


# Write your handlers here

def main():
  tornado.options.parse_command_line()
  http_server = tornado.httpserver.HTTPServer(Application())
  http_server.listen(options.port)
  tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
  main()
