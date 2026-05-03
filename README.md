# 🍛 Curry Company Analytics & ML Pipeline

Este projeto implementa um pipeline completo de Engenharia de Dados e Machine Learning para a **Curry Company**, uma empresa de delivery. O objetivo é prever o tempo de entrega (`time_takenmin`) com base em variáveis climáticas, de tráfego, logísticas e geográficas.

## 🏗️ Arquitetura de Dados (Medalhão)

O projeto segue a arquitetura de camadas para garantir a qualidade e linhagem dos dados dentro do **Google BigQuery**:

1.  **Raw (Bronze):** Dados brutos carregados via Python do dataset original.
2.  **Staging (Silver):** Limpeza inicial, renomeação de colunas e tipagem (Views no dbt).
3.  **Marts (Gold):** Tabela fato de pedidos com engenharia de atributos (Cálculo de distância Haversine).
4.  **ML Ready:** Dataset final otimizado, sem valores nulos e com atributos temporais extraídos (Dia da semana, Hora do pedido) pronto para treinamento de modelos.



## 🛠️ Tecnologias Utilizadas

* **Python 3.13:** Ingestão de dados e scripts auxiliares.
* **Poetry:** Gerenciamento de dependências e ambientes virtuais.
* **dbt (data build tool):** Transformação de dados, testes de qualidade e documentação.
* **Google BigQuery:** Data Warehouse para armazenamento e processamento em larga escala.
* **Git/GitHub:** Versionamento de código e controle de linhagem.
* **Looker Studio:** Dashboard interativo para visualização de KPIs de negócio.

## 🚀 Como Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/lucas-mansur/curry-company-analytics.git](https://github.com/lucas-mansur/curry-company-analytics.git)
    cd curry-company-analytics
    ```

2.  **Instale as dependências:**
    ```bash
    poetry install
    ```

3.  **Configure o dbt:**
    Certifique-se de que seu arquivo `profiles.yml` está configurado para o Google BigQuery na região `us-central1`.

4.  **Execute o Pipeline:**
    ```bash
    # Carregue os pacotes do dbt
    poetry run dbt deps

    # Execute as transformações e crie as tabelas
    poetry run dbt run

    # Valide os dados com os testes configurados
    poetry run dbt test
    ```

## 📊 Insights & Dashboards

O dashboard no **Looker Studio** foca em métricas críticas para a operação:
* **Tempo Médio por Densidade de Tráfego:** Identificação de gargalos em horários de pico.
* **Performance Climática:** Como condições de chuva ou sol impactam a velocidade dos entregadores.
* **Distribuição Geográfica:** Mapa de calor das entregas para otimização de praças.

## 🧠 Machine Learning

A tabela `fct_orders_ml` foi preparada especificamente para algoritmos de regressão, apresentando:
* Remoção rigorosa de nulos para evitar viés.
* Conversão de tipos (String para Time/Date).
* Engenharia de Atributos: Extração de `order_hour` e `day_of_week`.