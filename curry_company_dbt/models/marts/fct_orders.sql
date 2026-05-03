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
        ) / 1000, 2) as distance_km,



        -- Criando o ponto geográfico do Restaurante
        ST_GEOGPOINT(restaurant_longitude, restaurant_latitude) AS restaurant_geo_location,

        -- Criando o ponto geográfico da Entrega
        ST_GEOGPOINT(delivery_location_longitude, delivery_location_latitude) AS delivery_geo_location,

  



    from orders
)

select
   *
from compute_metrics