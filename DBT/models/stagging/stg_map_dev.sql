{{config(materialized="view")}}

select 
cast(region as string) as region,
cast(code as string) as code,
cast(value as FLOAT64) as value,
cast(series_id as string) as series_id,
cast(date as date) as date,
cast(groupid as string) as groupid
 from {{source('stagging','stg_map')}}

