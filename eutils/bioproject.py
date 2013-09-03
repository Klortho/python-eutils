from eutils import DocumentSummary, requests, _eutils_base
from lxml import etree

class BioprojectDocumentSummary(DocumentSummary):
    organism = None
    project_data_type = None
    def __init__(self, xml):
        super(BioprojectDocumentSummary, self).__init__(xml)
        tree = etree.XML(xml)
        orgname = tree.xpath("//Organism_Name")
        self.organism = orgname[0].text if len(orgname) > 0 else None
        proj = tree.xpath("//Project_Data_Type")
        self.project_data_type = proj[0].text if len(proj) > 0 else None


def esummary(id):
    response = requests.get(_eutils_base + 'esummary.fcgi',
                            params={
                                'db': "bioproject",
                                 'id': id,
                                 "version": "2.0"
                            })

    return BioprojectDocumentSummary(response.content)
