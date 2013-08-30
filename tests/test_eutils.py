import unittest
from eutils import eutils, sra

class SimpleTest(unittest.TestCase):

    def test_esearch(self):
        ids = eutils.esearch("pmc", "human")
        self.assertTrue(len(ids) == 20, "ids is " + str(len(ids)))

    def test_esummary_title(self):
        """
        Test that sra esummary returns a title for an existing record.
        """
        summary = sra.esummary("66441")
        self.assertNotEqual(summary.title, None, "Summary title should not be None.")

    def test_esummary_empty_title(self):
        """
        Test that sra esummary returns no title for an empty record.
        """
        summary = sra.esummary("3702208")
        self.assertEqual(summary.title, None, "Summary title should be None.")
