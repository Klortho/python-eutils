from backend.service import *
from django.template import Template

class search(service):
    def __init__(self, db):
        
        return super(search, self).__init__("search", db)
    
    def request(self, term, params={}):
        params["term"] = term
        
        return super(search, self).request(params)

    def requestTemplate(self):
        return """
<SearchRequest userid="{{ user_id }}">
<UseHistory>1</UseHistory>
<Db>{{ db }}</Db>
<QueryType>eSearch</QueryType>
<Term>{{ term }}</Term>
{% if activeFilter %}<ActiveFilter>{{ activeFilter }}</ActiveFilter>{% endif %}
{% if page %}<Page>{{ page }}</Page>{% endif %}
{% if pageSize %}<PageSize>{{ pageSize }}</PageSize>{% endif %}
{% if groupBy %}<GroupBy>{{ groupBy }}</GroupBy>{% endif %}
<Mode clipboardcheck="yes" />
</SearchRequest>
"""