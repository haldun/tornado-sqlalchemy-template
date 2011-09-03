import tornado.web

class Form(tornado.web.UIModule):
  """
  Generic form rendering module. Works with wtforms.
  Use this in your template code as:

  {% module Form(form) %}

  where `form` is a wtforms.Form object. Note that this module does not render
  <form> tag and any buttons.
  """

  def render(self, form):
    """docstring for render"""
    return self.render_string('uimodules/form.html', form=form)


# Put your uimodules here
