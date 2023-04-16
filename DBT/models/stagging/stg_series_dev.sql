{{config(materialized="view")}}

select 
cast(id as string) as id,                                    
cast(realtime_start as TIMESTAMP) as realtime_start,                
cast(realtime_end as TIMESTAMP) as realtime_end,                  
cast(title as string) as title,                                 
cast(observation_start as TIMESTAMP ) as observation_start,                     
cast(observation_end as TIMESTAMP ) as observation_end,                       
cast(frequency as string ) as frequency,                             
cast(frequency_short as string ) as frequency_short,                       
cast(units as string ) as units,                                 
cast(units_short as string ) as units_short,                           
cast(seasonal_adjustment as string ) as seasonal_adjustment,                   
cast(seasonal_adjustment_short as string ) as seasonal_adjustment_short,             
cast(last_updated as TIMESTAMP) as last_updated,                  
cast(popularity as integer ) as popularity,                             
cast(group_popularity as integer ) as group_popularity,                       
cast(category_id as integer ) as category_id                           
 from {{source('stagging','stg_series')}}
