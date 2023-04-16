class endpoint_url:
    main_url                        = 'https://api.stlouisfed.org/fred'
    main_url_geo                    = 'https://api.stlouisfed.org/geofred'

class category_endpoint_url:
    category                        = '/category?'
    child_category                  = '/category/children?'
    related_category                = '/category/related?'
    series_category                 = '/category/series?'
    tags_category                   = '/category/tags?'
    realted_tag                     = '/category/related_tags?'
    para_category                   = ['file_type','category_id']
    para_child_category             = ['file_type','category_id','realtime_start','realtime_end']
    para_related_category           = ['file_type','category_id','realtime_start','realtime_end']
    para_series_category            = ['file_type','category_id','realtime_start','realtime_end','limit','offset','order_by','sort_order','filter_variable','filter_value','tag_names','exclude_tag_names']
    para_tags_category              = ['file_type','category_id','realtime_start','realtime_end','tag_names','tag_group_id','search_text','limit','offset','order_by','sort_order']
    para_realted_tag                = ['file_type','category_id','realtime_start','realtime_end','tag_names','exclude_tag_names','tag_group_id','search_text','limit','offset','order_by','sort_order']

class release_endpoint_url:
    multiple_releases               = '/releases?'
    multiple_dates                  = '/releases/dates?'
    one_release                     = '/release?'
    one_dates                       = '/release/dates?'
    series                          = '/release/series?'
    sources                         = '/releases/sources?'
    tags                            = '/releases/tags?'
    related_tags                    = '/releases/related_tags?'
    tables                          = '/releases/tables?'
    para_multiple_releases          =  ['file_type','realtime_start','realtime_end','limit','offset','order_by','sort_order']  
    para_multiple_dates             =  ['file_type','realtime_start','realtime_end','limit','offset','order_by','sort_order','include_release_dates_with_no_data']
    para_one_release                =  ['file_type','release_id','realtime_start','realtime_end']
    para_one_dates                  =  ['file_type','release_id','realtime_start','realtime_end','limit','offset','sort_order','include_release_dates_with_no_data']
    para_series                     =  ['file_type','release_id','realtime_start','realtime_end','limit','offset','order_by','sort_order','filter_variable','filter_value','tag_names','exclude_tag_names']
    para_sources                    =  ['file_type','release_id','realtime_start','realtime_end']
    para_tags                       =  ['file_type','release_id','realtime_start','realtime_end','tag_names','tag_group_id','search_text','limit','offset','order_by','sort_order']
    para_related_tags               =  ['file_type','release_id','realtime_start','realtime_end','tag_names','exclude_tag_names','tag_group_id','search_text','limit','offset','order_by','sort_order']
    para_tables                     =  ['file_type','release_id','element_id','include_observation_values','observation_date']

class series_endpoint_url:
    series	                        =	'/series?'
    categories	                    =	'/series/categories?'
    observations	                =	'/series/observations?'
    release	                        =	'/series/release?'
    search	                        =	'/series/search?'
    search_tags	                    =	'/series/search/tags?'
    search_related_tags	            =	'/series/search/related_tags?'
    tags	                        =	'/series/tags?'
    updates	                        =	'/series/updates?'
    vintagedates	                =	'/series/vintagedates?'    
    para_series                     =   ['file_type','series_id','realtime_start','realtime_end']
    para_series_categories          =   ['file_type','series_id','realtime_start','realtime_end']
    para_series_observations        =	['file_type','series_id','realtime_start','realtime_end','limit','offset','sort_order','observation_start','observation_end','units','frequency','aggregation_method','output_type','vintage_dates']
    para_series_release	            =	['file_type','series_id','realtime_start','realtime_end']
    para_series_search	            =	['file_type','search_text','search_type','realtime_start','realtime_end','limit','offset','order_by','sort_order','filter_variable','filter_value','tag_names','exclude_tag_names']
    para_series_search_tags	        =	['file_type','series_search_text','realtime_start','realtime_end','tag_names','tag_group_id','tag_search_text','limit','offset','order_by','sort_order']
    para_series_search_related_tags =	['file_type','series_search_text','realtime_start','realtime_end','tag_names','exclude_tag_names','tag_group_id','tag_search_text','limit','offset','order_by','sort_order']
    para_series_tags	            =	['file_type','series_id','realtime_start','realtime_end','order_by','sort_order']
    para_series_updates	            =	['file_type','realtime_start','realtime_end','limit','offset','filter_value','start_time','end_time']
    para_series_vintagedates        =	['file_type','series_id','realtime_start','realtime_end','limit','offset','sort_order']

class sources_endpoint_url:
    sources	                        =	'/sources?'
    source	                        =	'/source?'
    releases	                    =	'/source/releases?'
    para_sources	                =	['file_type','realtime_start','realtime_end','limit','offset','order_by','sort_order']
    para_source	                    =	['file_type','source_id','realtime_start','realtime_end']
    para_releases	                =	['file_type','source_id','realtime_start','realtime_end','limit','offset','order_by','sort_order']

class tags_endpoint_url:
    tags	                        =	'/tags?'
    related_tags	                =	'/related_tags?'
    series	                        =	'/tags/series?'
    para_tags	                    =	['file_type','realtime_start','realtime_end','tag_names','tag_group_id','search_text','limit','offset','order_by','sort_order']
    para_related_tags	            =	['file_type','realtime_start','realtime_end','tag_names','exclude_tag_names','tag_group_id','search_text','limit','offset','order_by','sort_order']
    para_series	                    =	['file_type','tag_names','exclude_tag_names','realtime_start','realtime_end','limit','offset','order_by','sort_order']

class map_endpoint_url:
    file	                        =	'/shapes/file?'
    series	                        =	'/series/group?'
    series_regional	                =	'/series/data?'
    regional	                    =	'/regional/data?'
    para_file	                    =	['shape']
    para_series	                    =	['file_type','series_id']
    para_series_regional	        =	['file_type','series_id','date','start_date']
    para_regional	                =	['file_type','series_group','region_type','date','start_date','season','units','transformation','frequency','aggregation_method']


class clean_df:
    series_col      = ['id', 'realtime_start', 'realtime_end', 'title', 'observation_start','observation_end', 'frequency', 'frequency_short', 'units','units_short', 'seasonal_adjustment', 'seasonal_adjustment_short','last_updated', 'popularity', 'group_popularity']
    series_str_col  = ['id', 'title', 'observation_start','observation_end', 'frequency', 'frequency_short', 'units','units_short', 'seasonal_adjustment', 'seasonal_adjustment_short','last_updated']
    series_int_col  = ['popularity','group_popularity']
    series_date_col = ['realtime_start','realtime_end','last_updated']



class query_bq:
    query_getseriesPara = '''
        SELECT id FROM `ete-projectdatatalkclub.dbo.Category` where 
    id not in (SELECT distinct parent_id FROM `ete-projectdatatalkclub.dbo.Category`)
    order by id
    '''
    query_getMapPara = '''
    SELECT
      [region_type]
      ,[series_group]
      ,[season]
      ,u.units
      ,[frequency]
      ,EXTRACT(DATE FROM min_date) as mindate
      ,EXTRACT(DATE FROM max_date) as maxdate
 FROM `ete-projectdatatalkclub.dbo.Series_GroupMeta`  g
inner join `ete-projectdatatalkclub.dim.Dim_Unit` u
  on g.unitid	 =u.id
where  Active = 1
order by series_group
    '''