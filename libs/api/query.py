import urllib.request, urllib.error, urllib.parse
import json

import config

class Query(object):
    def query(self, parameters):
        '''Preform a query to api.php with the dict parameters'''
        url = config.api_path + '?action=query&format=json'
        for parameter in parameters:
            url += '&%s=%s' % (parameter, parameters[parameter])
        
        # Request the URL and parse results
        request = urllib.request.urlopen(url)
        self.data = json.loads(request.read().decode())
        request.close()
