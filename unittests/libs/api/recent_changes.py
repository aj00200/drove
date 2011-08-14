'''Import the necessary modules to preform unit tests on the API
and then define the class to do it with for the unittest module'''

import unittest
import libs.api.recent_changes

class TestRecentChanges(unittest.TestCase):
    def setUp(self):
        self.recent_changes = libs.api.recent_changes.RecentChanges()
        
    def test_get(self):
        '''Assuming proper config, should complete without errors'''
        self.recent_changes.get()
        self.assertIsNotNone(self.recent_changes.data,
                'self.data is not being stored in RecentChanges()')