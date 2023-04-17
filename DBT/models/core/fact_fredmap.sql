{{ config(materialized="table") }}

with series as (
    select * 
    from {{ ref('stg_series_dev') }}
),
map as (
    select * 
    from {{ ref('stg_map_dev') }}
),
category as (
    select * 
    from {{ ref('stg_category_dev') }}
),
country as (
    select * 
    from {{ ref('dim_country') }}
)

select
m.date,
FORMAT_DATE('%b-%g',m.date) as monthyear,
m.region,
co.continent,
co.sub_region,
s.title as seriestitle,
s.frequency,
m.value,
s.units,
s.seasonal_adjustment,
c.name as categoryname,
c.parent_name,
s.popularity,
s.group_popularity,
m.series_id
from map m
inner join series s
on m.series_id = s.id
left join category c
on s.category_id = c.id 
left join country co
on m.code = co.code