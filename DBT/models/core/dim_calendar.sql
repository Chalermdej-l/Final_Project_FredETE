{{ config(materialized="table") }}

select
date,
EXTRACT(DAY from date) as day,
EXTRACT(DAYOFWEEK from date) as dow,
EXTRACT(WEEK from date) as week,
EXTRACT(MONTH from date) as month,
EXTRACT(QUARTER from date) as QUARTER,
EXTRACT(YEAR from date) as year,
FORMAT_DATE('%a',date) as dayshort,
FORMAT_DATE('%A',date) as dayfull,
FORMAT_DATE('%b',date) as monthshort,
FORMAT_DATE('%B',date) as monthfull,
FORMAT_DATE('%b-%g',date) as monthyear,
FORMAT_DATE('%B-%G',date) as monthyearfull,
case 
    when FORMAT_DATE('%a',date)  in ('Sat','Sun') then 1
    else 0 end as weekend,
date_diff(current_date(),cast(date as date),day) as offset,
date_diff(current_date(),cast(date as date),month) as monthoffset,
date_diff(current_date(),cast(date as date),year) as yearoffset
from {{ref('calendar')}}