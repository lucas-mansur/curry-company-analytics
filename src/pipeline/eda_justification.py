import pandas as pd

def analyze_missing_impact(path):
    df = pd.read_csv(path)
    
    # Total de registros com 'NaN ' string na idade
    total_rows = len(df)
    missing_age = len(df[df['Delivery_person_Age'] == 'NaN ']) # Note o espaço no material original
    
    percent = (missing_age / total_rows) * 100
    
    print(f"--- 📊 Análise de Impacto (EDA) ---")
    print(f"Total de registros: {total_rows}")
    print(f"Registros com Idade Inválida: {missing_age}")
    print(f"Impacto da exclusão: {percent:.2f}% do dataset")
    
    if percent < 5:
        print("💡 Justificativa: Impacto baixo (<5%). A exclusão preserva a integridade sem perda significativa de volume.")
    else:
        print("⚠️ Justificativa: Impacto considerável. Recomenda-se investigar a origem do erro no sistema de cadastro.")

if __name__ == "__main__":
    analyze_missing_impact('data/raw/train.csv')