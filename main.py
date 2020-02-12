import webapp2
import jinja2
from google.appengine.api import users
import os

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        # self.response.write("hello world")
        JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)), extensions=["jinja2.ext.autoescape"],
        autoescape=True)
        url = ""
        url_string = ""
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_string = "logout"
        else:
            url = users.create_login_url(self.request.uri)
            url_string = "login"
        template_values = {
            "url" : url,
            "url_string" : url_string,
            "user" : user
        }
        template = JINJA_ENVIRONMENT.get_template("main.html")
        self.response.write(template.render(template_values))




app = webapp2.WSGIApplication([("/", MainPage)], debug=True)
