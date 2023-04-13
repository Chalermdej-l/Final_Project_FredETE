
from API_helper.url_client.category import category
from API_helper.url_client.releases import releases
from API_helper.url_client.series import series
from API_helper.url_client.sources import sources
from API_helper.url_client.tag import tags
from API_helper.url_client.map import map

class url_module(object):   
    '''
    Helper create for calling Fred API
    https://fred.stlouisfed.org/docs/api/fred/#API
    '''
    def __init__(self):
        ## Initiate clients
        self.category = category()
        self.releases = releases()
        self.series = series()
        self.sources = sources()
        self.tags = tags()
        self.map = map()