import urllib2
import json

import config

class Query(object):
    def query(self, parameters):
        '''Preform a query to api.php with the dict parameters'''
        url = config.api_path + '?action=query&format=json'
        for parameter in parameters:
            url += '&%s=%s' % (parameter, parameters[parameter])
        
        # Request the URL and parse results
        request = urllib2.urlopen(url)
        self.data = json.load(request)
        request.close()
