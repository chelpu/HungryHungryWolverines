import webapp2
# import sqlalchemy
# import twitter

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hungry Hungry Wolverines')

class SignUp(webapp2.RequestHandler):
    def get(self):
        import twilio.twiml
        resp = twilio.twiml.Response()
        resp.message('THANKS FOR SIGNING UP, d00d')
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(resp)


class Update(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Querying for new food...')


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/signup', SignUp),
    ('/update', Update),
], debug=True)