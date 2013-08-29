# Using portal as a proxy for now

from backend.cgi import *
from django.template import Template, Context

class service(cgi):
    def __init__(self, name, db):
        self.name = name
        self.db = db
        self.user_id = "43077D5F1F2BFC41_0026SID"
        self.template = self.requestTemplate()
        return super(service, self).__init__("http://dev.ncbi.nlm.nih.gov/sites/backendProxy@0/")
        
    def request(self, params):
        xml = self.formatRequest(params)
        response = super(service, self).post(self.name+"/", { "db": self.db, "request": xml })
        if (response.status_code != 200):
            return "<error>Internal error</error>"
        
        return response.content


    def formatRequest(self, params):
        tmpl = Template(self.template)
        params["db"] = self.db
        params["user_id"] = self.user_id
        c = Context(params)
        return tmpl.render(c)
    
    
    def requestTemplate(self):
        return "<xml/>" 
    