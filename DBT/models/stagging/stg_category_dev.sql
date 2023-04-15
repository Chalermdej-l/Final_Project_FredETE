{{ config(materialized="view") }}

select
    cast(name as string) as name,
    cast(id as integer) as id,
    cast(parent_name as string) as parent_name,
    cast(parent_id as integer) as parent_id
from {{ source("stagging", "stg_category") }} 
limit 100
