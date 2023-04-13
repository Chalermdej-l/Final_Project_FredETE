
import requests as re
from config import release_endpoint_url
from API_helper.util.util import _build_url

class releases:

    def multiple_releases(**kwarg):
        '''
        ['file_type','realtime_start','realtime_end','limit','offset','order_by','sort_order']  
        '''
        # Define API Parameter
        endpoint = release_endpoint_url.multiple_releases
        endpointpara = release_endpoint_url.para_multiple_releases
        # Contruct the url request    
        url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,kwarg=kwarg)
        try:
            result = re.get(url_requst)
            return result
        except Exception as error:
            print(f"An error occured '{error}'. Please check the parameter pass.")
            return None

    def multiple_dates(**kwarg):
        '''
        ['file_type','realtime_start','realtime_end','limit','offset','order_by','sort_order','include_release_dates_with_no_data']  
        '''
        # Define API Parameter
        endpoint = release_endpoint_url.multiple_dates
        endpointpara = release_endpoint_url.para_multiple_dates
        # Contruct the url request    
        url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,kwarg=kwarg)
        try:
            result = re.get(url_requst)
            return result
        except Exception as error:
            print(f"An error occured '{error}'. Please check the parameter pass.")
            return None
              
    def one_release(**kwarg): 
            '''
            ['file_type', 'release_id', 'realtime_start', 'realtime_end']
            '''
            # Define API Parameter
            endpoint = release_endpoint_url.one_release
            endpointpara = release_endpoint_url.para_one_release
            # Contruct the url request    
            url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,kwarg=kwarg)
            try:
                result = re.get(url_requst)
                return result
            except Exception as error:
                print(f"An error occured ''. Please check the parameter pass.")
                return None
                
    def one_dates(**kwarg): 
            '''
            ['file_type', 'release_id', 'realtime_start', 'realtime_end', 'limit', 'offset', 'sort_order', 'include_release_dates_with_no_data']
            '''
            # Define API Parameter
            endpoint = release_endpoint_url.one_dates
            endpointpara = release_endpoint_url.para_one_dates
            # Contruct the url request    
            url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,kwarg=kwarg)
            try:
                result = re.get(url_requst)
                return result
            except Exception as error:
                print(f"An error occured ''. Please check the parameter pass.")
                return None
                
    def series(**kwarg): 
            '''
            ['file_type', 'release_id', 'realtime_start', 'realtime_end', 'limit', 'offset', 'order_by', 'sort_order', 'filter_variable', 'filter_value', 'tag_names', 'exclude_tag_names']
            '''
            # Define API Parameter
            endpoint = release_endpoint_url.series
            endpointpara = release_endpoint_url.para_series
            # Contruct the url request    
            url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,kwarg=kwarg)
            try:
                result = re.get(url_requst)
                return result
            except Exception as error:
                print(f"An error occured ''. Please check the parameter pass.")
                return None
                
    def sources(**kwarg): 
            '''
            ['file_type', 'release_id', 'realtime_start', 'realtime_end']
            '''
            # Define API Parameter
            endpoint = release_endpoint_url.sources
            endpointpara = release_endpoint_url.para_sources
            # Contruct the url request    
            url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,kwarg=kwarg)
            try:
                result = re.get(url_requst)
                return result
            except Exception as error:
                print(f"An error occured ''. Please check the parameter pass.")
                return None
                
    def tags(**kwarg): 
            '''
            ['file_type', 'release_id', 'realtime_start', 'realtime_end', 'tag_names', 'tag_group_id', 'search_text', 'limit', 'offset', 'order_by', 'sort_order']
            '''
            # Define API Parameter
            endpoint = release_endpoint_url.tags
            endpointpara = release_endpoint_url.para_tags
            # Contruct the url request    
            url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,kwarg=kwarg)
            try:
                result = re.get(url_requst)
                return result
            except Exception as error:
                print(f"An error occured ''. Please check the parameter pass.")
                return None
                
    def related_tags(**kwarg): 
            '''
            ['file_type', 'release_id', 'realtime_start', 'realtime_end', 'tag_names', 'exclude_tag_names', 'tag_group_id', 'search_text', 'limit', 'offset', 'order_by', 'sort_order']
            '''
            # Define API Parameter
            endpoint = release_endpoint_url.related_tags
            endpointpara = release_endpoint_url.para_related_tags
            # Contruct the url request    
            url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,kwarg=kwarg)
            try:
                result = re.get(url_requst)
                return result
            except Exception as error:
                print(f"An error occured ''. Please check the parameter pass.")
                return None
                
    def tables(**kwarg): 
            '''
            ['file_type', 'release_id', 'element_id', 'include_observation_values', 'observation_date']
            '''
            # Define API Parameter
            endpoint = release_endpoint_url.tables
            endpointpara = release_endpoint_url.para_tables
            # Contruct the url request    
            url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,kwarg=kwarg)
            try:
                result = re.get(url_requst)
                return result
            except Exception as error:
                print(f"An error occured ''. Please check the parameter pass.")
                return None
                

