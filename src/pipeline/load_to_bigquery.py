import pandas as pd
from google.cloud import bigquery
from dotenv import load_dotenv
import os

# 1. Carrega as variáveis do .env (GCP_PROJECT_ID e GCP_DATASET_ID)
load_dotenv()

def carregar_dados_para_bigquery(caminho_csv, tabela_id):
    """
    Realiza a carga do arquivo limpo para o BigQuery usando ADC (Federação).
    """
    # 2. Instancia o cliente usando o ID do projeto do .env
    projeto_id = os.getenv('GCP_PROJECT_ID')
    client = bigquery.Client(project=projeto_id)
    
    # 3. Lê o CSV processado (o que preservamos as 45k+ linhas)
    print(f"📖 Lendo arquivo: {caminho_csv}")
    df = pd.read_csv(caminho_csv)
    
    # 4. Configuração do Job de Carga
    job_config = bigquery.LoadJobConfig(
        # 'WRITE_TRUNCATE' garante que, se você rodar de novo, 
        # a tabela é limpa e atualizada (evita duplicidade no teste)
        write_disposition="WRITE_TRUNCATE",
        autodetect=True,
    )

    print(f"📤 [ADC] Subindo {len(df)} linhas para {tabela_id} no projeto {projeto_id}...")
    
    try:
        # 5. Executa a carga
        job = client.load_table_from_dataframe(df, tabela_id, job_config=job_config)
        job.result()  # Aguarda a conclusão do processo no Google
        
        print(f"✅ Sucesso total! Os dados agora estão disponíveis no BigQuery.")
        print(f"🔗 Link para consulta: https://console.cloud.google.com/bigquery?project={projeto_id}")
        
    except Exception as e:
        print(f"❌ Erro durante o upload: {e}")
        print("\nDica de Staff: Verifique se o Dataset 'curry_company' foi criado no console do GCP.")

if __name__ == "__main__":
    # Montagem dinâmica do ID da tabela
    dataset = os.getenv('GCP_DATASET_ID')
    projeto = os.getenv('GCP_PROJECT_ID')
    id_final_tabela = f"{projeto}.{dataset}.orders_cleaned"
    
    caminho_dados_limpos = 'data/processed/train_clean.csv'
    
    carregar_dados_para_bigquery(caminho_dados_limpos, id_final_tabela)