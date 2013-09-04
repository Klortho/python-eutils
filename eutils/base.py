# eutils module

import requests
from lxml import etree

__version__ = '0.2.1'
_eutils_base = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/'


def esearch(db, term):
    response = requests.get(_eutils_base + 'esearch.fcgi',
                            params={
                                'db': db,
                                'term': term,
                            })

    esearch_doc = etree.fromstring(response.content)
    ids = [id_el.text for id_el in etree.XPath('/eSearchResult/IdList/Id')(esearch_doc)]

    return ids

class SummaryNotFoundException(Exception):
    pass

class DocumentSummary(object):
    """
    The DocumentSummary class is a base class that can be
    extended by modules to add data specific to databases
    (such as SRA titles). It just contains a variable, xml,
    that contains a parsed xml tree. Other variables will be
    added by subclasses.
    """
    xml = None
    def __init__(self, xml):
        self.xml = xml

def esummary(db, id, docsum_class=DocumentSummary):
    """
    This takes a single id and returns the results for the first record in the resulting docsum set.
    """
    response = requests.get(_eutils_base + 'esummary.fcgi',
                            params={
                                'db': db,
                                 'id': id,
                                 "version": "2.0"
                            })
    tree = etree.XML(response.content)
    docsums = tree.xpath('//DocumentSummary')
    # TODO: Allow returning multiple docsums
    if len(docsums) == 0:
        raise SummaryNotFoundException
    return docsum_class(docsums[0])
