'''Import the necessary modules to preform unit tests on the API
and then define the class to do it with for the unittest module'''

import unittest
import libs.api.query

class TestQuery(unittest.TestCase):
    def setUp(self):
        self.query = libs.api.query.Query()
        
    def test_query(self):
        '''Assuming proper config, should complete without errors'''
        self.query.query({
            'list': 'recentchanges',
            'rcprop': 'title',
            'rclimit': 3
        })
        self.assertIsNotNone(self.query.data,
                'self.data is not being stored in Query()')
        
