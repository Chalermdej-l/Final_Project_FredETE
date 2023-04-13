
import requests as re
from config import series_endpoint_url
from API_helper.util.util import _build_url

class series:
    def series(**kwarg): 
            '''
            ['file_type', 'series_id', 'realtime_start', 'realtime_end']
            '''
            # Define API Parameter
            endpoint = series_endpoint_url.series
            endpointpara = series_endpoint_url.para_series
            # Contruct the url request    
            url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,kwarg=kwarg)
            try:
                result = re.get(url_requst)
                return result
            except Exception as error:
                print(f"An error occured ''. Please check the parameter pass.")
                return None
                
    def categories(**kwarg): 
            '''
            ['file_type', 'series_id', 'realtime_start', 'realtime_end']
            '''
            # Define API Parameter
            endpoint = series_endpoint_url.categories
            endpointpara = series_endpoint_url.para_series_categories
            # Contruct the url request    
            url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,kwarg=kwarg)
            try:
                result = re.get(url_requst)
                return result
            except Exception as error:
                print(f"An error occured ''. Please check the parameter pass.")
                return None
                
    def observations(**kwarg): 
            '''
            ['file_type', 'series_id', 'realtime_start', 'realtime_end', 'limit', 'offset', 'sort_order', 'observation_start', 'observation_end', 'units', 'frequency', 'aggregation_method', 'output_type', 'vintage_dates']
            '''
            # Define API Parameter
            endpoint = series_endpoint_url.observations
            endpointpara = series_endpoint_url.para_series_observations
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
            ['file_type', 'series_id', 'realtime_start', 'realtime_end']
            '''
            # Define API Parameter
            endpoint = series_endpoint_url.series
            endpointpara = series_endpoint_url.para_series_series
            # Contruct the url request    
            url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,kwarg=kwarg)
            try:
                result = re.get(url_requst)
                return result
            except Exception as error:
                print(f"An error occured ''. Please check the parameter pass.")
                return None
                
    def search(**kwarg): 
            '''
            ['file_type', 'search_text', 'search_type', 'realtime_start', 'realtime_end', 'limit', 'offset', 'order_by', 'sort_order', 'filter_variable', 'filter_value', 'tag_names', 'exclude_tag_names']
            '''
            # Define API Parameter
            endpoint = series_endpoint_url.search
            endpointpara = series_endpoint_url.para_series_search
            # Contruct the url request    
            url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,kwarg=kwarg)
            try:
                result = re.get(url_requst)
                return result
            except Exception as error:
                print(f"An error occured ''. Please check the parameter pass.")
                return None
                
    def search_tags(**kwarg): 
            '''
            ['file_type', 'series_search_text', 'realtime_start', 'realtime_end', 'tag_names', 'tag_group_id', 'tag_search_text', 'limit', 'offset', 'order_by', 'sort_order']
            '''
            # Define API Parameter
            endpoint = series_endpoint_url.search_tags
            endpointpara = series_endpoint_url.para_series_search_tags
            # Contruct the url request    
            url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,kwarg=kwarg)
            try:
                result = re.get(url_requst)
                return result
            except Exception as error:
                print(f"An error occured ''. Please check the parameter pass.")
                return None
                
    def search_related_tags(**kwarg): 
            '''
            ['file_type', 'series_search_text', 'realtime_start', 'realtime_end', 'tag_names', 'exclude_tag_names', 'tag_group_id', 'tag_search_text', 'limit', 'offset', 'order_by', 'sort_order']
            '''
            # Define API Parameter
            endpoint = series_endpoint_url.search_related_tags
            endpointpara = series_endpoint_url.para_series_search_related_tags
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
            ['file_type', 'series_id', 'realtime_start', 'realtime_end', 'order_by', 'sort_order']
            '''
            # Define API Parameter
            endpoint = series_endpoint_url.tags
            endpointpara = series_endpoint_url.para_series_tags
            # Contruct the url request    
            url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,kwarg=kwarg)
            try:
                result = re.get(url_requst)
                return result
            except Exception as error:
                print(f"An error occured ''. Please check the parameter pass.")
                return None
                
    def updates(**kwarg): 
            '''
            ['file_type', 'realtime_start', 'realtime_end', 'limit', 'offset', 'filter_value', 'start_time', 'end_time']
            '''
            # Define API Parameter
            endpoint = series_endpoint_url.updates
            endpointpara = series_endpoint_url.para_series_updates
            # Contruct the url request    
            url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,kwarg=kwarg)
            try:
                result = re.get(url_requst)
                return result
            except Exception as error:
                print(f"An error occured ''. Please check the parameter pass.")
                return None
                
    def vintagedates(**kwarg): 
            '''
            ['file_type', 'series_id', 'realtime_start', 'realtime_end', 'limit', 'offset', 'sort_order']
            '''
            # Define API Parameter
            endpoint = series_endpoint_url.vintagedates
            endpointpara = series_endpoint_url.para_series_vintagedates
            # Contruct the url request    
            url_requst = _build_url(endpoint=endpoint,endpointpara=endpointpara,kwarg=kwarg)
            try:
                result = re.get(url_requst)
                return result
            except Exception as error:
                print(f"An error occured ''. Please check the parameter pass.")
                return None
                
