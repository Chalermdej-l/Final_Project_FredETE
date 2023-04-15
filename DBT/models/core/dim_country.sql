{{ config(materialized="incremental") }}


select
code,
country,
continent,
sub_region
from {{ref('country')}}