from base import DocumentSummary, requests, _eutils_base
from base import esummary as base_esummary
from lxml import etree

class SRADocumentSummary(DocumentSummary):
    title = None
    def __init__(self, xml):
        super(SRADocumentSummary, self).__init__(xml)
        tree = etree.XML(xml)
        exp_xml = tree.xpath("//ExpXml")
        if len(exp_xml) > 0:
            text = exp_xml[0].text
            tree2 = etree.XML("<div>" + text + "</div>")
            t = tree2.xpath("//Title")
            self.title = t[0].text if len(t) > 0 else None


def esummary(id):
    return base_esummary("sra", id, SRADocumentSummary)
