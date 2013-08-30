import unittest
from eutils import *

class SimpleTest(unittest.TestCase):

    def test_esearch(self):
        ids = esearch("pmc", "human")
        self.assertTrue(len(ids) == 20, "ids is " + str(len(ids)))

