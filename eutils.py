# eutils module

import requests
from lxml import etree

__version__ = '0.1.1'
_eutils_base = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/'


def esearch(db, id):
    response = requests.get(_eutils_base + 'esearch.fcgi',
                            params={
                                'db': db,
                                'term': id,
                            })

    esearch_doc = etree.fromstring(response.content)
    ids = [id_el.text for id_el in etree.XPath('/eSearchResult/IdList/Id')(esearch_doc)]

    return ids
