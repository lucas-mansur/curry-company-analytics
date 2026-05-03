# # Objetivo: Deixar o dado impecável para os próximos notebooks.
#### Configurações Iniciais (Imports de pandas, numpy, etc).

import pandas as pd
import numpy as np

#### Carregamento dos Dados.
df = pd.read_csv('data/raw/train.csv')


#### Limpeza de Strings (Remoção de espaços ' ' com strip()).
df['ID'] = df['ID'].str.strip()                                
df['Delivery_person_ID'] = df['Delivery_person_ID'].str.strip()  
df['Delivery_person_Age'] = df['Delivery_person_Age'].str.strip()               
df['Delivery_person_Ratings'] = df['Delivery_person_Ratings'].str.strip()           
df['Order_Date'] = df['Order_Date'].str.strip()                        
df['Time_Orderd'] = df['Time_Orderd'].str.strip()                       
df['Time_Order_picked'] = df['Time_Order_picked'].str.strip()                 
df['Weatherconditions'] = df['Weatherconditions'].str.strip()                 
df['Road_traffic_density'] = df['Road_traffic_density'].str.strip()              
df['Type_of_order'] = df['Type_of_order'].str.strip()                     
df['Type_of_vehicle'] = df['Type_of_vehicle'].str.strip()                   
df['multiple_deliveries'] = df['multiple_deliveries'].str.strip()               
df['Festival'] = df['Festival'].str.strip()                          
df['City'] = df['City'].str.strip()                              
df['Time_taken(min)'] = df['Time_taken(min)'].str.strip()       


#### Tratamento de Dados da coluna 'Time_taken(min)' (Lidar string que contém informação numérica).
df['Time_taken(min)'] = df['Time_taken(min)'].str.extract('(\d+)')

#### Tratamento de Dados da coluna 'Weatherconditions' (Lidar informação repetitiva).
df['Weatherconditions'] = df['Weatherconditions'].str.slice(start=11)

#### Conversão de Tipos (Datas para datetime, números para int/float).
df['ID'] = df['ID'].astype(str) 
df['Delivery_person_ID'] = df['Delivery_person_ID'].astype(str)    
df['Delivery_person_Age'] = pd.to_numeric(df['Delivery_person_Age'], errors='coerce')    
df['Delivery_person_Ratings'] = pd.to_numeric(df['Delivery_person_Ratings'], errors='coerce')    
df['Restaurant_latitude'] = pd.to_numeric(df['Restaurant_latitude'], errors='coerce')
df['Restaurant_longitude'] = pd.to_numeric(df['Restaurant_longitude'], errors='coerce')
df['Delivery_location_latitude'] = pd.to_numeric(df['Delivery_location_latitude'], errors='coerce')
df['Delivery_location_longitude'] = pd.to_numeric(df['Delivery_location_longitude'], errors='coerce')
df['Order_Date'] = pd.to_datetime(df['Order_Date'], format='%d-%m-%Y')
df['Time_Orderd'] = pd.to_datetime(df['Time_Orderd'], format='%H:%M:%S', errors='coerce').dt.strftime('%H:%M:%S') 
df['Time_Order_picked'] = pd.to_datetime(df['Time_Order_picked'], format='%H:%M:%S', errors='coerce').dt.strftime('%H:%M:%S') 
df['Weatherconditions'] = df['Weatherconditions'].astype(str)    
df['Road_traffic_density'] = df['Road_traffic_density'].astype(str)    
df['Vehicle_condition'] = pd.to_numeric(df['Vehicle_condition'], errors='coerce')
df['Type_of_order'] = df['Type_of_order'].astype(str)    
df['Type_of_vehicle'] = df['Type_of_vehicle'].astype(str)    
df['multiple_deliveries'] = pd.to_numeric(df['multiple_deliveries'], errors='coerce')    
df['Festival'] = df['Festival'].astype(str)    
df['City'] = df['City'].astype(str)
df['Time_taken(min)'] = pd.to_numeric(df['Time_taken(min)'], errors='coerce')


#### Tratamento de Dados Ausentes (Lidar com o texto 'NaN ').
df.replace('NaN', np.nan, inplace=True)

#### Padronização de nomes de colunas (Snake Case e sem caracteres especiais)
df.columns = [col.lower().strip().replace('(', '').replace(')', '').replace(' ', '_') for col in df.columns]

#### Visualização completa dos dados antes da exportação
df.head(5)

#### Exportação (Salvar como train_cleaned.csv).


df.to_csv('data/processed/train_clean.csv', index=False)


