import pandas as pd

# Caminho para o arquivo que você moveu para data/raw
path = 'data/raw/train.csv'

def profile_data(file_path):
    # Carregando o dado
    df = pd.read_csv(file_path)
    
    print("--- 🔍 Perfil Inicial dos Dados ---")
    print(f"Total de Linhas: {df.shape[0]}")
    print(f"Total de Colunas: {df.shape[1]}")
    
    print("\n--- ⚠️ Valores Ausentes (NaN) ---")
    print(df.isnull().sum()[df.isnull().sum() > 0])
    
    print("\n--- 📝 Amostra das Colunas (Tipos) ---")
    print(df.dtypes)
    
    return df

if __name__ == "__main__":
    profile_data(path)