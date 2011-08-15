import config
import libs.api.query

class RecentChanges(libs.api.query.Query):
    '''Queries the recent changes feed.'''
    def __init__(self):
        super(RecentChanges, self).__init__()
        self.changes = []
        
        # Set default options
        self.defaults = {
            'list': 'recentchanges',
            'rcprop': 'title|ids|sizes|flags|user',
            'rclimit': 3}
        self.rclimit = 3
        
    def get(self, parameters={}):
        '''Run the query to get the results'''
        self.defaults.update(parameters)
        self.query(self.defaults)
        self.changes = self.data['query']['recentchanges']

    
