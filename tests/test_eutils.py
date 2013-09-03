import unittest
from eutils import eutils, sra, bioproject, biosample

class EutilsTest(unittest.TestCase):

    def test_esearch(self):
        ids = eutils.esearch("pmc", "human")
        self.assertTrue(len(ids) == 20, "ids is " + str(len(ids)))

    def test_esummary_xml(self):
        """
        Test that we get back some xml. TODO: Figure out what this should test.
        """
        summary = eutils.esummary("sra", "66441")
        self.assertNotEqual(summary.xml or None, None, "summary xml should not be empty.")

class SRATest(unittest.TestCase):
    def test_sra_esummary_title(self):
        """
        Test that sra esummary returns a title for an existing record.
        """
        summary = sra.esummary("66441")
        self.assertNotEqual(summary.title, None, "Summary title should not be None.")

    def test_sra_esummary_empty_title(self):
        """
        Test that sra esummary raises an exception for a nonexistent record.
        """
        try:
            summary = bioproject.esummary("0")
        except eutils.SummaryNotFoundException:
            exception_raised = True
        else:
            exception_raised = False
        self.assertTrue(exception_raised, "An exception should be raised.")

class BioProjectTest(unittest.TestCase):
    def test_bioproject_esummary(self):
        """
        Test that bioproject esummary returns an organism and project_data_type.
        """
        summary = bioproject.esummary("105523")
        self.assertNotEqual(summary.organism, None, "organism should not be None.")
        self.assertNotEqual(summary.project_data_type, None, "project_data_type should not be None.")
    
    def test_bioproject_esummary(self):
        """
        Test that bioproject esummary raises an exception for a nonexistent record.
        """
        try:
            summary = bioproject.esummary("0")
        except eutils.SummaryNotFoundException:
            exception_raised = True
        else:
            exception_raised = False
        self.assertTrue(exception_raised, "An exception should be raised.")
        
class BioSampleTest(unittest.TestCase):
    def test_biosample_esummary(self):
        """
        Test that biosample esummary returns sra and a sample_name.
        """
        summary = biosample.esummary("138349")
        self.assertNotEqual(summary.sra, None, "sra should not be None.")
        self.assertNotEqual(summary.sample_name, None, "sample_name should not be None.")