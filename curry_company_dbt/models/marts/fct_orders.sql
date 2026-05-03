with orders as (
    select * from {{ ref('stg_orders') }}
),

compute_metrics as (
    select
        *,
        -- Calculando a distância em KM usando Haversine (Função do BigQuery)
        round(st_distance(
            st_geogpoint(restaurant_longitude, restaurant_latitude),
            st_geogpoint(delivery_location_longitude, delivery_location_latitude)
        ) / 1000, 2) as distance_km
    from orders
)

select
   *
from compute_metrics