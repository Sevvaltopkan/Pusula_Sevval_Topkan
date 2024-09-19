from src.data_loading import load_data, handle_missing_data
from src.preprocessing import encode_categorical_data, standardize_data
from src.visualization import visualize_data

#Ana Veri İşleme 
def process_data(file_path):
    df = load_data(file_path)
    
    # Eksik verilerin doldurulması
    df = handle_missing_data(df)
    
    # Veriyi görselleştirme (kategorik veriler kodlanmadan önce)
    visualize_data(df)
    
    # Kategorik verileri kodlama
    df = encode_categorical_data(df)
    
    # Sayısal verilerin standardizasyonu
    df = standardize_data(df)
    
    return df

#Ana programın dosya yolu üzerinden çağrı yapılarak başlatılması
if __name__ == "__main__":
    file_path = r'C:\Users\topka\Masaüstü\Pusula\data\side_effect_data 1.xlsx'
    processed_df = process_data(file_path)
