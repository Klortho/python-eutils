from eutils import DocumentSummary, requests, _eutils_base
from lxml import etree

class BiosampleDocumentSummary(DocumentSummary):
    sra = None
    sample_name = None
    def __init__(self, xml):
        super(BiosampleDocumentSummary, self).__init__(xml)
        tree = etree.XML(xml)

        sample_data = tree.xpath("//SampleData")
        if len(sample_data) > 0:
            sample_data = sample_data[0].text
            sd_tree = etree.XML(sample_data)

            sra_ns = sd_tree.xpath("//Id[@db='SRA']")
            self.sra = sra_ns[0].text if len(sra_ns) > 0 else None
            sample_name_ns = sd_tree.xpath("//Id[@db_label='Sample name']")
            self.sample_name = sample_name_ns[0].text if len(sample_name_ns) > 0 else None
            


def esummary(id):
    response = requests.get(_eutils_base + 'esummary.fcgi',
                            params={
                                'db': "biosample",
                                 'id': id,
                                 "version": "2.0"
                            })

    return BiosampleDocumentSummary(response.content)
