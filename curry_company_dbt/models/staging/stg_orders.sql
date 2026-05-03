-- Este é o modelo de Staging. Aqui a gente apenas renomeia e tipa os dados.
with source as (
    select * from {{ source('gcp_raw', 'orders_cleaned') }}
),

renamed as (
select
        -- IDs e Chaves
        id as order_id,
        delivery_person_id,

        -- Datas e Tempos
        cast(order_date as date) as order_date,
        time_order_picked,
        time_orderd,
        cast(time_takenmin as int64) as time_takenmin,

        -- Entregador
        cast(delivery_person_age as int64) as delivery_person_age,
        cast(delivery_person_ratings as float64) as delivery_person_ratings,
        vehicle_condition,
        type_of_vehicle,

        -- Localização
        restaurant_latitude,
        restaurant_longitude,
        delivery_location_latitude,
        delivery_location_longitude,

        -- Informações de Contexto
        weatherconditions, -- Verifique se no Python você renomeou para weather_conditions ou se ainda é weatherconditions
        road_traffic_density,
        type_of_order,
        multiple_deliveries,
        festival,
        city,


    from source
)

select * from renamed

