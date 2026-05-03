-- models/ml_ready/fct_orders_ml.sql
with base as (
    select * from {{ ref('fct_orders') }}
),

compute_features as (
    select
        *,
        -- Engenharia de Atributos (Tempo e Espaço)
        -- Convertemos a string '23:00:00' para o tipo TIME antes de extrair a hora
        extract(hour from cast(time_orderd as TIME)) as order_hour,

        -- Convertemos a string da data para o tipo DATE antes de extrair o dia
        extract(dayofweek from cast(order_date as DATE)) as day_of_week,

        -- Convertemos a string '23:05:00' para o tipo TIME antes de extrair a hora
        extract(hour from cast(time_order_picked as TIME)) as order_picked_hour,
    from base
    where 
        -- Limpeza radical para ML: remove linhas onde o essencial está faltando
    delivery_person_ratings is not null
    and delivery_person_age is not null
    and city is not null
    and multiple_deliveries is not null
    and weatherconditions is not null
    and road_traffic_density is not null
    and festival is not null
    and vehicle_condition is not null
    and type_of_order is not null
    and time_order_picked is not null
    and time_orderd is not null
    and type_of_vehicle is not null
    and time_takenmin is not null
)

select * from compute_features