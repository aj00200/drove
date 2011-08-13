import config
import query

class RecentChanges(query.Query):
    '''Queries the recent changes feed.'''
    def __init__(self):
        super(RecentChanges, self).__init__()
        self.changes = []

    def get(self, rcprop='title'):
        '''Run the query to get the results'''
        self.query({
                'list': 'recentchanges',
                'rcprop': rcprop,  # TODO: figure out how to use this
                'rclimit': 3
                })

    
