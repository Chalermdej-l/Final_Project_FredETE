
import requests as re
from config import tags_endpoint_url
from API_helper.util.util import _build_url

class tags:    
    def tags(**kwarg): 
            '''
            ['file_type', 'realtime_start', 'realtime_end', 'tag_names', 'tag_group_id', 'search_text', 'limit', 'offset', 'order_by', 'sort_order']
            '''
            # Define API Parameter
            endpoint = tags_endpoint_url.tags
            endpointpara = tags_endpoint_url.para_tags
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
            ['file_type', 'realtime_start', 'realtime_end', 'tag_names', 'exclude_tag_names', 'tag_group_id', 'search_text', 'limit', 'offset', 'order_by', 'sort_order']
            '''
            # Define API Parameter
            endpoint = tags_endpoint_url.related_tags
            endpointpara = tags_endpoint_url.para_related_tags
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
            ['file_type', 'tag_names', 'exclude_tag_names', 'realtime_start', 'realtime_end', 'limit', 'offset', 'order_by', 'sort_order']
            '''
            # Define API Parameter
            endpoint = tags_endpoint_url.series
            endpointpara = tags_endpoint_url.para_series
            # Contruct the url request    
            url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,kwarg=kwarg)
            try:
                result = re.get(url_requst)
                return result
            except Exception as error:
                print(f"An error occured ''. Please check the parameter pass.")
                return None
                
