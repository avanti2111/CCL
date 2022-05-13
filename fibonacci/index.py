import webapp2

class MainPage(webapp2.RequestHandler):

    def get(self):
        count = 0
        n1 = 0
        n2 = 1
        while count < 8 :
            self.response.out.write(n1)
            self.response.out.write("<br>")
            sum = n1 + n2
            n1 = n2
            n2 =  sum
            count += 1

app = webapp2.WSGIApplication([("/", MainPage)], debug = True)            