import config
import libs.api.query

class RecentChanges(libs.api.query.Query):
    '''Queries the recent changes feed.'''
    def __init__(self):
        super(RecentChanges, self).__init__()
        self.changes = []
        
        # Set default options
        self.rcprop = 'title'
        self.rclimit = 3
        
    def get(self, rcprop='title'):
        '''Run the query to get the results'''
        self.query({
                'list': 'recentchanges',
                'rcprop': self.rcprop,  # TODO: figure out how to use this
                'rclimit': self.rclimit
                })
        self.changes = self.data['query']['recentchanges']

    
