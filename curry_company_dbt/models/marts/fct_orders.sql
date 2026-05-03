with orders as (
    select * from {{ ref('stg_orders') }}
),

compute_metrics as (
    select
        *,
        -- 1. Calculando a distância exata entre os pontos (Em KM)
        -- Usamos ST_DISTANCE que é o padrão de ouro para cálculos geoespaciais
        round(st_distance(
            st_geogpoint(restaurant_longitude, restaurant_latitude),
            st_geogpoint(delivery_location_longitude, delivery_location_latitude)
        ) / 1000, 2) as distance_km,

        -- 2. Criando a coordenada do Restaurante para o Looker
        -- Formato esperado pelo Looker: "Lat,Long" (String)
        concat(
            safe_cast(restaurant_latitude as string), 
            ",", 
            safe_cast(restaurant_longitude as string)
        ) as restaurant_geo_location,

        -- 3. Criando a coordenada da Entrega para o Looker
        -- Formato esperado pelo Looker: "Lat,Long" (String)
        concat(
            safe_cast(delivery_location_latitude as string), 
            ",", 
            safe_cast(delivery_location_longitude as string)
        ) as delivery_geo_location

    from orders
)

select
   *
from compute_metrics