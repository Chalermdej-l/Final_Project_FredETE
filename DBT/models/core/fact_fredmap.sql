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
  from {{ref('country')}}
),
series_group as (
    select * 
    from {{ ref('series_group') }}
)

select
m.date,
FORMAT_DATE('%b-%g',m.date) as monthyear,
ifnull(m.region,'Missing') as region,
ifnull(co.continent,'Missing') as continent,
ifnull(co.sub_region,'Missing') as sub_region ,
co.latitude ,
co.longitude,
sg.title as grouptitle,
s.title as seriestitle,
s.frequency,
m.value,
s.units,
s.seasonal_adjustment,
c.name as categoryname,
c.parent_name,
s.popularity,
s.group_popularity,
from map m
inner join series s
on m.series_id = s.id
inner join series_group sg
on m.groupid = sg.series_group
left join category c
on s.category_id = c.id 
left join country co
on m.code = co.code
where m.value != 0 and m.value is not null
and sg.Active = 1