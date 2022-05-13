import webapp2


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.out.write("<h1> hellow,world!!</h1>")

app = webapp2.WSGIApplication([("/",MainPage)],debug=True)
