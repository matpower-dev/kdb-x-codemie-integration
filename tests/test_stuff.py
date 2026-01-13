import unittest
import query

class TestKdbClientConnectMethods(unittest.TestCase):

    def test_kdb_client_connect(self): 
       kdb_client = query.KdbClient("localhost", 5896)
       kdb_client.sample_query()
