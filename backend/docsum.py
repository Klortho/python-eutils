from backend.service import *
from lxml import etree

class docsum(service):
    def __init__(self, db):
        return super(docsum, self).__init__("docsum", db)
    
    def request(self, idlist):
        params = { "idlist": idlist }
        return super(docsum, self).request(params)
    
    def requestTemplate(self):
        return """
<DocSumRequest dbname="{{ db }}" version="1.0" userid="{{ user_id }}">
    <IdList>
        {% for id in idlist %}<Id>{{ id }}</Id>{% endfor %}
    </IdList>            
</DocSumRequest>        
"""

    def extractIds(self, xml):
        root = etree.fromstring(xml)
        return (el.text for el in root.xpath('//IdList/Id'))
        #return etree.tostringlist(root.xpath('//IdList/Id'))