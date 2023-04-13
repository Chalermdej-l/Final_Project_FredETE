
import requests as re
from config import sources_endpoint_url
from API_helper.util.util import _build_url

class sources:
        
    def sources(**kwarg): 
            '''
            ['file_type', 'realtime_start', 'realtime_end', 'limit', 'offset', 'order_by', 'sort_order']
            '''
            # Define API Parameter
            endpoint = sources_endpoint_url.sources
            endpointpara = sources_endpoint_url.para_sources
            # Contruct the url request    
            url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,kwarg=kwarg)
            try:
                result = re.get(url_requst)
                return result
            except Exception as error:
                print(f"An error occured ''. Please check the parameter pass.")
                return None
                
    def source(**kwarg): 
            '''
            ['file_type', 'source_id', 'realtime_start', 'realtime_end']
            '''
            # Define API Parameter
            endpoint = sources_endpoint_url.source
            endpointpara = sources_endpoint_url.para_source
            # Contruct the url request    
            url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,kwarg=kwarg)
            try:
                result = re.get(url_requst)
                return result
            except Exception as error:
                print(f"An error occured ''. Please check the parameter pass.")
                return None
                
    def sourcess(**kwarg): 
            '''
            ['file_type', 'source_id', 'realtime_start', 'realtime_end', 'limit', 'offset', 'order_by', 'sort_order']
            '''
            # Define API Parameter
            endpoint = sources_endpoint_url.sourcess
            endpointpara = sources_endpoint_url.para_sourcess
            # Contruct the url request    
            url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,kwarg=kwarg)
            try:
                result = re.get(url_requst)
                return result
            except Exception as error:
                print(f"An error occured ''. Please check the parameter pass.")
                return None
                
